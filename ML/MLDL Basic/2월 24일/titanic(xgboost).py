import numpy as np
import pandas as pd
from xgboost import XGBRegressor, XGBClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

MY_PATH = '/content/drive/My Drive/Colab Notebooks/data/'

df = pd.read_csv(MY_PATH + 'titanic_train.csv')
df.head(3)
# df.info()
# df.isnull().sum()   # 결측치 개수 확인

df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', \
                                   'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Others')
df['Title'] = df['Title'].replace('Mlle', 'Miss')
df['Title'] = df['Title'].replace('Ms', 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')
df['Title'].value_counts()

df['Fare'] = df['Fare'] / (df['SibSp'] + df['Parch'] + 1)

df.head()

# 결측치 처리. Cabin은 결측치가 너무 많아서 drop.
df['Embarked'].fillna('N', inplace = True)
# df.isnull().sum()   # 결측치 개수 확인

# 불필요한 feature를 제거한다.
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df.head()

# One-hot encoding
# dh = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title'])
# Label encoding
# Tree 계열인 XGBRegressor를 사용할 것이므로 nominal feature들을
# one-hot encoding이 아닌 label encoding을 사용해도 된다.
# SVM, Deep Learning 등 Tree 계열이 아닌 것을 사용하려면 
# one-hot encoding을 사용해야 한다.
# 라벨 인코더 생성
for col in ['Sex', 'Embarked', 'Title']:
  enc = LabelEncoder()
  df[col] = enc.fit_transform(df[col])


# XGBoost를 이용해서 Age의 결측치를 추정해 보자
# Age feature는 177개가 결측치이다 (NaN).
# 다른 feature들을 이용해서 regression으로 Age를 추정한다.
x_normal = dh.dropna()          # Age가 정상인 데이터
x_nan = dh[dh['Age'].isnull()]  # Age가 NaN인 데이터

# 학습 데이터 생성
x_train = np.array(x_normal.drop(['Age', 'Survived'], axis=1))
y_train = np.array(x_normal['Age'])
x_test = np.array(x_nan.drop(['Age', 'Survived'], axis=1))

# regression tree를 생성한다.
reg_model = XGBRegressor(objective='reg:squarederror')
reg_model.fit(x_train, y_train)

# Age = NaN인 데이터를 추정하고, 정상 데이터와 추정 데이터를 합친다.
x_nan = x_nan.drop('Age', axis=1)
x_nan['Age'] = reg_model.predict(x_test)

dfp = pd.concat([x_normal, x_nan])

# Age가 정상인 분포와 추정한 분포를 육안으로 비교한다.
plt.hist(x_normal['Age'], bins=30, alpha=0.7)
plt.hist(x_nan['Age'], bins=30, alpha=0.7)
plt.show()

# 최종 학습 : 생존자 추정 성능 평가
x_feat = np.array(dfp.drop('Survived', axis=1))
x_target = np.array(dfp['Survived'])

x_train, x_test, y_train, y_test = train_test_split(x_feat, x_target, test_size=0.2)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# XGBoost (classifier)로 Train 데이터 세트를 학습한다.
clf_model = XGBClassifier(objective='binary:logistic')
clf_model.fit(x_train, y_train)

# 정확도를 측정한다.
acc = clf_model.score(x_test, y_test)
print('정확도 = {:.3f}'.format(acc))

