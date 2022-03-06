import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# mnist 데이터를 다운로드하고 나중에 사용하기 위해 저장해 둔다.
# 시간이 오래 걸리기 때문.
mnist = fetch_openml('mnist_784')
with open('mnist.pkl', 'wb') as f:
       pickle.dump(mnist, f)

# 저장된 mnist 데이터를 읽어온다.
with open('mnist.pkl', 'rb') as f:
        mnist = pickle.load(f)

print(mnist.keys())

# target이 str 이므로 int 형으로 바꿔준다.
x_feat = np.array(mnist['data']/ 255)
y_target = mnist.target.to_numpy().astype('int8').reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)
n_class = len(set(mnist['target']))


# Network 생성
xInput = Input(batch_shape=(None, x_train.shape[1]))

# 은닉층 구조
hlayer = Dense(10, activation="relu")(xInput)

# 출력층 구조
yOutput = Dense(n_class, activation="softmax")(hlayer)

# 모델 구축
model = Model(xInput, yOutput)
model.compile(loss = "sparse_categorical_crossentropy", optimizer="adam")
hist = model.fit(x_train, y_train, batch_size = 300, epochs=10, validation_data=(x_test, y_test))

# summary 를 통해 형태 파악
model.summary()

# acc 측정
y_prob = model.predict(x_test)
y_pred = np.argmax(y_prob, axis=1).reshape(-1,1)
acc = (y_test == y_pred).mean()
print("%.4f" % acc)

# error 가 감소하는 모습을 관찰한다
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()