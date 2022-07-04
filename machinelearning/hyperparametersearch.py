#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program demonstrates using the GridSearchCV package to tune the major
hyperparameters in an xgboost model. The data of X,y are taken from the 
familiar iris dataset included in the sklearn. So, the first step should be
replaced by whatever corresponding dataset of your interest.

The code represents a single run of code without defining new functions or
classes. It can be considered a single cell in a Jupyter notebook.

The flow expects the python environment called machinelearning found here:
   https://github.com/michaelbbryan/pyenvironments/tree/main/machinelearning
"""
import pandas as pd
import numpy as np

#
# Sample data Load
#
from sklearn.datasets import load_iris
iris = load_iris()
X = pd.DataFrame(data=iris.data, columns=iris.feature_names)
y = np.where(iris.target == 0, 1, 0)  # detect the setosa species

#
# Sample model algorithm
#
import xgboost as xgb
from xgboost import XGBRegressor
model = xgb.XGBRegressor(seed = 20)

#
# Hyperparameter grid search
#
from sklearn.model_selection import GridSearchCV

params = { 'max_depth': [3,6,10],
           'learning_rate': [0.01, 0.05, 0.1],
           'n_estimators': [100, 500, 1000],
           'colsample_bytree': [0.3, 0.7]}

clf = GridSearchCV(estimator=model, 
                   param_grid=params,
                   scoring='neg_mean_squared_error', 
                   verbose=1)
clf.fit(X, y)
print()
print("Best parameters:", clf.best_params_)