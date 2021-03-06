# -*- coding: utf-8 -*-
"""2.mnist(conv1d).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uONPZb2HL07RpJ1QapEQ3_H9z7FetMJa
"""

# CNN 예시 : 1D convolution을 이용하여 mnist 이미지를 분석한다.
from tensorflow.keras.layers import Input, Dense, Conv1D, MaxPooling1D, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# 저장된 mnist 데이터를 읽어온다.
DATA_PATH = '/content/drive/MyDrive/Colab Notebooks/data/'
with open(DATA_PATH + 'mnist.pkl', 'rb') as f:
        mnist = pickle.load(f)

# mnist['data'] 숫자의 범위를 변환한다 (표준화) : 0 ~ 255 --> 0 ~ 1.0
# target = ['1', '2',...] 문자로 돼있음. --> 숫자로 변환해야 함.
x_feat = np.array(mnist['data']).reshape(-1, 28, 28) / 255
y_target = np.array(mnist['target'].to_numpy().astype('int8')).reshape(-1,1)

# 학습 데이터와 시험 데이터를 생성한다.
x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# Convolutional 1D 모델을 생성한다.
n_row = x_train.shape[1]
n_col = x_train.shape[2]
n_class = len(set(y_train[:, 0]))

x_input = Input(batch_shape = (None, n_row, n_col))
h_conv = Conv1D(filters=30, kernel_size=6, strides=1, padding = 'same', activation='relu')(x_input)
h_pool = MaxPooling1D(pool_size=4, strides=1, padding='valid')(h_conv)
h_flat = Flatten()(h_pool)
y_output = Dense(n_class, activation='softmax')(h_flat)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer = optimizers.Adam(learning_rate=0.001))
model.summary(line_length=80)

hist = model.fit(x_train, y_train, 
                 batch_size=1024, 
                 epochs=50, 
                 validation_data = (x_test, y_test))

# Loss history를 그린다
plt.plot(hist.history['loss'], color='blue', label='train')
plt.plot(hist.history['val_loss'], color='red', label='test')
plt.legend()
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

y_prob = model.predict(x_test)
y_pred = np.argmax(y_prob, axis=1).reshape(-1,1)
acc = (y_test == y_pred).mean()
print('정확도 ={:.4f}'.format(acc))

import pandas as pd
df = pd.DataFrame({'y_test': y_test.reshape(-1,), 'y_pred': y_pred.reshape(-1,)})
df.head(10)

# 잘못 분류한 이미지 몇개를 확인해 본다.
# 어떤 이미지를 잘 맞추지 못할까? 사람이라면 아래 이미지를 잘 맞출 수 있을까?
n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(14,4))
for i, miss in enumerate(miss_sam):
    x = x_test[miss] * 255  # 표준화 단계에서 255로 나누었으므로, 여기서는 곱해준다.
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_test[miss]) + ' / ' + str(y_pred[miss]))

