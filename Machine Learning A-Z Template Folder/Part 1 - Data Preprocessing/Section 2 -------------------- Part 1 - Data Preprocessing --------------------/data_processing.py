# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:24:30 2018

@author: Thiago
"""

import numpy as np
import matplotlib.pyplot as plb
import pandas as pd

#importing data
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
"""
indep = pd.DataFrame(x)
dep = pd.DataFrame(y)
"""
#missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

# Separate in columns with numbers instead of strings
onehotencoder = OneHotEncoder(categorical_features= [0])
x = onehotencoder.fit_transform(x).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Splitting datasets into training and test
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 51)