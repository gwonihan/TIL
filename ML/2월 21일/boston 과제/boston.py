# Linear Regression, Ridge, Lasso, ElastikNet 비교
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler

boston = load_boston()

x = boston.data
y = boston.target

f_scale = StandardScaler()                    
t_scale = StandardScaler()                    

f_scaled = f_scale.fit_transform(boston.data)
t_scaled = t_scale.fit_transform(boston.target.reshape(-1,1))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

pipe = Pipeline(steps=[('model', LinearRegression())])
grid_params = [
              {'model' : [LinearRegression()]},
               
              {'model' : [Ridge()],
                'model__alpha' : np.arange(0.01, 1.1, 0.1)},
              
              {'model' : [Lasso()],
                'model__alpha' : np.arange(0.01, 1.1, 0.1)},
              
              {'model' : [ElasticNet()],
                'model__alpha' : np.arange(0.01, 10, 0.1),
                'model__l1_ratio' : np.arange(0.1, 1.1, 0.1)}
              ]

grid = GridSearchCV(estimator=pipe, param_grid=grid_params, cv=10, refit=True)
grid.fit(x_train, y_train)

best_model = grid.best_estimator_
print("Best parameter = ", grid.best_params_)
print("Best test score = ", best_model.score(x_test, y_test))