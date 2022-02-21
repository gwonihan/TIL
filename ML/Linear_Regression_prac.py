import pandas as pd
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from mlxtend.plotting import scatterplotmatrix
import numpy as np


boston = load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['MEDV'] = boston.target

# # feature 상관관계
# cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
# scatterplotmatrix(df[cols].values, figsize=(10,8), names=cols, alpha=0.5)
# plt.tight_layout()
# plt.show()

class LinearRegressionGD(object):
  def __init__(self, eta=0.001, n_iter=20):
    self.eta = eta
    self.n_iter = n_iter

  def fit(self, X, y):
    self.w_ = np.zeros(1 + X.shape[1])
    self.cost_ = []

    for i in range(self.n_iter):
      output = self.net_input(X)
      errors = (y - output)
      self.w_[1:] += self.eta * X.T.dot(errors)
      self.w_[0] += self.eta * errors.sum()
      cost = (errors**2).sum() / 2.0
      self.cost_.append(cost)
    return self

  def net_input(self,X):
    return np.dot(X, self.w_[1:] + self.w_[0])

  def predict(self,X):
    return self.net_input(X)


X = df[['RM']].values
y = df['MEDV'].values
from sklearn.preprocessing import StandardScaler # 표준화
sc_x = StandardScaler()
sc_y = StandardScaler()
X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()
Ir = LinearRegressionGD()
Ir.fit(X_std, y_std)

def lin_regplot(X_std, y_std, model):
  plt.scatter(X, y, c='steelblue', edgecolors='white', s=70)
  plt.plot(X, model.predict(X), color='black', lw=2)
  return None

lin_regplot(X_std, y_std, Ir)
plt.xlabel('Average number of rooms[RM] (standardized)')
plt.ylabel('Price in $1000s [MEDV] (standardized)')
plt.show()

from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(X,y)

print('기울기: %.3f' % slr.coef_[0])
print('절편: %.3f' % slr.intercept_)

lin_regplot(X, y, slr)
plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000s [MEDV]')
plt.show()

from sklearn.linear_model import RANSACRegressor
ransac = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss = 'absolute_loss', residual_threshold=5.0, random_state=0)
ransac.fit(X,y)                           
# max_trials : 최대반복횟수
# min_samples : 랜덤 샘플의 최소 갯수
# loss : 알고리즘이 학습한 직선과 샘플 포인트 간 수직 거리의 절대값
# residual_threshold : 매개변수를 설정하여 학습한 직선과 수직 거리가 5 이내에 있는 정상 샘플만 포함

inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
line_X = np.arange(3, 10, 1)
line_y_ransac = ransac.predict(line_X[:, np.newaxis])
plt.scatter(X[inlier_mask], y[inlier_mask], c = 'steelblue', edgecolor = 'white', marker='o',label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], c = 'limegreen', edgecolor = 'white', marker='s', label='Outliers')
plt.plot(line_X, line_y_ransac, color = 'black', lw=2)
plt.xlabel('Average number of rooms[RM]')
plt.ylabel('Price in $1000s[MEDV]')
plt.legend(loc='upper left')
plt.show()