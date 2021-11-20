# 这个ipython notebook主要是我解决Kaggle Titanic问题的思路和过程

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame

data_train = pd.read_csv("Train.csv")
print(data_train.columns)
#data_train[data_train.Cabin.notnull()]['Survived'].value_counts()