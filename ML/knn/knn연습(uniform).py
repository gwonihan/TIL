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

# distance를 오름차순 (ascending)으로 정렬한다
df.sort_values(by='distance', inplace=True)

# distance가 큰 상위 K를 선택하고, target의 majority를 찾는다
K = 10
candidates = df[:K]['target'].to_numpy().astype('int')
counts = np.bincount(candidates)
majority = np.argmax(counts)
print(majority)

from sklearn.neighbors import KNeighborsClassifier

# KNN 모델을 생성한다.
knn = KNeighborsClassifier(n_neighbors = K)
knn.fit(x_train, y_train)

# 시험 데이터의 target을 추정한다.
y_pred = knn.predict(x_test)
print(y_pred)

