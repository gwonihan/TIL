# -*- coding: utf-8 -*-
"""1.NBayes(iris).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14GA0Ca6ntZGcq1jSIxM02J9gQypY7d_M
"""

# Naive Bayes로 iris 데이터를 학습한다.
# feature들이 모두 실숫값이므로 gaussian model을 사용한다.
# ------------------------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# iris data set을 읽어온다
iris = load_iris()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x_train, x_test, y_train, y_test = \
    train_test_split(iris.data, iris.target, test_size = 0.2)

# Gaussian model로 Train 데이터 세트를 학습한다.
model = GaussianNB()
model.fit(x_train, y_train)

print("\n* Gaussian model :")
print("* 학습용 데이터로 측정한 정확도 = %.2f" % model.score(x_train, y_train))
print("* 시험용 데이터로 측정한 정확도 = %.2f" % model.score(x_test, y_test))

