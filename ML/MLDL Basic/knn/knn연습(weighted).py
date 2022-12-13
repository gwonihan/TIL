from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# iris 데이터를 읽어온다
iris = load_iris()

# 학습 데이터와 시험 데이터로 분리한다
x_train = iris['data'][:-1]
y_train = iris['target'][:-1]
x_test = iris['data'][-1:]

# 시험 데이터와 학습 데이터의 거리를 모두 계산한다.
distance = np.sqrt(((x_train - x_test) ** 2).sum(axis=1))

# 거리와 target을 dataframe으로 저장한다.
df = pd.DataFrame(data= np.c_[distance, y_train], columns= ['distance', 'target'])

# distance를 오름차순 (ascending)으로 정렬하고, 상위 K개를 선택한다
K = 10
df.sort_values(by='distance', inplace=True)
top_k = df[:K].copy()

# 거리 가중치를 계산한다. (inverse weighting)
top_k['weight'] = 1 / top_k['distance']

# 가중평균 거리를 계산한다.
w_distance = []
for t in [0, 1, 2]:
    w_distance.append(top_k.loc[top_k['target'] == t]['weight'].sum())

w_distance /= top_k['weight'].sum()

# w_distance가 가장 큰 class를 출력한다.
majority = np.argmax(w_distance)
print(majority)

from sklearn.neighbors import KNeighborsClassifier

# KNN 모델을 생성한다.
knn = KNeighborsClassifier(n_neighbors = K, weights='distance')
knn.fit(x_train, y_train)

# 시험 데이터의 target을 추정한다.
y_pred = knn.predict(x_test)
print(y_pred)

