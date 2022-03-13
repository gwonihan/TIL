# -*- coding: utf-8 -*-
"""3.lstm(mnist-m2m).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cgiO_gHgqKMiC3vn1VAmLIF7OVz7S-CW
"""

# LSTM으로 mnist 데이터를 분류한다.
from tensorflow.keras.layers import Input, Dense, LSTM, Bidirectional, TimeDistributed
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pickle

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

# classification은 many-to-many로 구성할 수 없다. 굳이 하려면 중간 
# target을 아래와 같이 만들어 주어야 한다.
y_train_rep = np.repeat(y_train, 28, axis=1).reshape(-1, 28, 1)
y_test_rep = np.repeat(y_test, 28, axis=1).reshape(-1, 28, 1)

# 그래프 모델을 생성한다
n_hNeuron = 50
n_class = len(set(mnist['target']))

xInput = Input(batch_shape=(None, x_train.shape[1], x_train.shape[2]))
hLayer1 = Bidirectional(LSTM(n_hNeuron, return_sequences = True), merge_mode = 'concat')(xInput)
hLayer2 = Bidirectional(LSTM(n_hNeuron, return_sequences = True), merge_mode = 'concat')(hLayer1)
yOutput = TimeDistributed(Dense(n_class, activation='softmax'))(hLayer2)

model = Model(xInput, yOutput)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.summary()

hist = model.fit(x_train, y_train_rep, 
                 batch_size=1024, 
                 epochs=50, 
                 validation_data = (x_test, y_test_rep))

# error가 감소하는 모습을 관찰한다.
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

y_prob = model.predict(x_test)[:, -1, :]
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

