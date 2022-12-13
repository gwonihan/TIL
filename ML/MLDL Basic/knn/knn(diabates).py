# -*- coding: utf-8 -*-
"""KNN(diabates).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xwkHiZAOvjpZF654ZUsLVSNz3L1vWoZ1
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

# diabetes 데이터를 읽어온다
DATA_PATH = '/content/drive/MyDrive/Colab Notebooks/data/'
data = pd.read_csv(DATA_PATH + 'diabetes.csv')
data.head()

# 학습 데이터와 시험 데이터로 분리한다.
x_feat = np.array(data.drop('Outcome', axis=1))
y_target = np.array(data['Outcome'])

x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)

# K를 변화시켜가면서 정확도를 측정해 본다
acc_test = []
acc_train = []
k_max = 20
for k in range(1, k_max):
    # Decision Tree로 학습 데이터 세트를 학습한다.
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    
    # 시험 데이터와 학습 데이터의 정확도를 측정한다.
    acc_test.append(knn.score(x_test, y_test))
    acc_train.append(knn.score(x_train, y_train))

plt.figure(figsize=(6, 4))
plt.plot(acc_test, marker='o', label="Test Data")
plt.plot(acc_train, marker='o', label="Train Data")
plt.legend()
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.xticks(np.arange(k_max), np.arange(1, k_max + 1))
plt.show()

opt_k = np.argmax(acc_test)
opt_acc = acc_test[opt_k]

print("optimal depth = {}, accuracy = {:.3f}".format(opt_k + 1, opt_acc))

# 활용
x_new = np.array([3, 127, 85, 25, 473, 27, 25, 37]).reshape(-1,8)
y_pred = knn.predict(x_new)

if y_pred[0] == 0:
    print('"이 환자는 당뇨병이 아님"으로 진단함')
else:
    print('"이 환자는 당뇨병임"으로 진단함')

print("추정의 정확도 = {:.2f}%".format(opt_acc * 100))
