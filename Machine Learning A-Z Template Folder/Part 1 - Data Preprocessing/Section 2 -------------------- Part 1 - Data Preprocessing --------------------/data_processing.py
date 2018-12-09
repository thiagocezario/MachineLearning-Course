# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:24:30 2018

@author: Thiago
"""

import numpy as np
import matplotlib.pyplot as plb
import pandas as pd

dataset = pd.read_csv('Data.csv')
independents = dataset.iloc[:, :-1].values
dependents = dataset.iloc[:, 3].values
df = pd.DataFrame(independents)
df2 = pd.DataFrame(dependents)