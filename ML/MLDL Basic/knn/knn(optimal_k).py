import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# iris 데이터를 읽어온다
iris = load_iris()

# 8:2 비율로 학습 데이터와 시험 데이터를 분리한다.
# 문제점?
n = int(iris['data'].shape[0] * 0.8)

x_train = iris['data'][:n]
y_train = iris['target'][:n]
x_test = iris['data'][n:]
y_test = iris['target'][n:]

# x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size=0.2)

# k를 변화시켜가면서 정확도를 측정해 본다
acc_test = []
acc_train = []
k_max = 30
for k in range(1, k_max):
    # KNN 으로 학습 데이터 세트를 학습한다.
    knn = KNeighborsClassifier(n_neighbors=k, p=2, weights='uniform')
    knn.fit(x_train, y_train)
    
    # 시험 데이터의 Feature에 대한 정확도
    y_pred = knn.predict(x_test)
    acc_test.append((y_test == y_pred).mean())
    
    # 학습 데이터의 Feature에 대한 정확도
    y_pred = knn.predict(x_train)
    acc_train.append((y_train == y_pred).mean())

    # 아래처럼해도 된다.
    # acc_test.append(knn.score(x_test, y_test))
    # acc_train.append(knn.score(x_train, y_train))

plt.figure(figsize=(8, 5))
plt.plot(acc_test, marker='o', label="Test Data")
plt.plot(acc_train, marker='o', label="Train Data")
plt.legend()
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.xticks(np.arange(k_max), np.arange(1, k_max + 1))
plt.show()

opt_k = np.argmax(acc_test)
opt_acc = acc_test[opt_k]

print("optimal k = {}, accuracy = {:.3f}".format(opt_k + 1, opt_acc))

