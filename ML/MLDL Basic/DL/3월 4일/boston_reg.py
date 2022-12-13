from sklearn.datasets import load_boston
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

boston = load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df["PRICE"] = boston.target

# 데이터 스케일 조정
df['ZN'] /= 10
df['AGE'] /= 10
df['TAX'] /= 100
df['PTRATIO'] /= 10
df['B'] /= 100
df['PRICE'] /= 10

x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target.reshape(-1,1), test_size = 0.15)
x_train.shape, x_test.shape

xInput = Input(batch_shape=(None, x_train.shape[1]))
hLayer = Dense(10, activation = "relu")(xInput)
yOutput = Dense(y_train.shape[1])(hLayer)
model = Model(xInput, yOutput)
model.compile(loss = "mean_squared_error", optimizer="adam")
hist = model.fit(x_train, y_train, batch_size=50, epochs=200, validation_data=(x_test,y_test))

# 표준화 0, batch_size=50, epochs=200
y_pred = model.predict(x_test)
R2 = r2_score(y_test, y_pred)
print("%.4f"%R2)
# 0.8495
# 실행할 때마다 r2가 다르게 나오는 것은 데이터가 작기 때문이고 코드 문제는 아니다


# 표준화 O
# error가 감소하는 모습을 관찰한다.
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 표준화 X
y_pred = model.predict(x_test)
R2 = r2_score(y_test, y_pred)
print("%.4f"%R2)
# 0.4776

# 표준화 X
# error가 감소하는 모습을 관찰한다.
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()