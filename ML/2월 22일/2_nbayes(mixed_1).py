# -*- coding: utf-8 -*-
"""2.NBayes(mixed_1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bWxSRap3iyPRM5N44cYWkDAboppsYFBt
"""

# Naive Bayes 분류기로 income 데이터 세트를 학습한다.
# categorical과 gaussian feature가 섞여 있는 경우, 각 feature를 분리하여 MultinomialNB와
# GaussianNB로 나눠서 학습하고 추정 확률을 곱한 값으로 시험 데이터의 label을 추정한다.
# ------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB

# income 데이터를 읽어온다
# https://www.kaggle.com/wenruliu/adult-income-dataset?select=adult.csv
DATA_PATH = '/content/drive/MyDrive/Colab Notebooks/data/'
income = pd.read_csv(DATA_PATH + 'income.csv')
income.head()

# categorical feature를 숫자로 변환한다.
cat_features = ["workclass", "marital_status", "occupation", "relationship", 
                "race", "sex","native_country", "income"]

for c in cat_features:
    income[c] = pd.Categorical(income[c]).codes

# Train 데이터 세트와 Test 데이터 세트를 구성한다
x = np.array(income)[:, :-1]
y = np.array(income)[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# categorical feature를 multinomial naive bayes로 학습한다.
# --------------------------------------------------------
cat_n = [1, 3, 4, 5, 6, 7, 9]
catx_train = x_train[:, cat_n]
catx_test = x_test[:, cat_n]

# Multinomial model로 categorical Train 데이터 세트를 학습한다.
model_m = MultinomialNB(alpha=1.0)  # alpha = 1.0 : Laplace smoothing (default)
model_m.fit(catx_train, y_train)

# gaussian feature를 gaussian naive bayes로 학습한다.
# --------------------------------------------------
gau_n = [0, 2, 8]
gaux_train = x_train[:, gau_n]
gaux_test = x_test[:, gau_n]

# Gaussian model로 gaussian Train 데이터 세트를 학습한다.
model_g = GaussianNB()
model_g.fit(gaux_train, y_train)

# 시험 데이터를 이용하여 정확도를 측정한다. 시험데이터도 categorical과 gaussian으로
# 분리돼 있다. 각각의 모형에 따라 확률을 추정한다.
cat_prob = model_m.predict_proba(catx_test)
gau_prob = model_g.predict_proba(gaux_test)

# 두 확률을 곱한다.
mix_prob = np.multiply(cat_prob, gau_prob)

# 두 확률의 곱으로 정확도를 측정한다.
mix_label = np.argmax(mix_prob, 1)
accuracy = (y_test == mix_label).mean()

print("\n* 시험용 데이터로 측정한 정확도 = %.2f" % accuracy)

