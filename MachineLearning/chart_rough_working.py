import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

quandl.ApiConfig.api_key = "g2ZYgdP4oxssaqw5HW9v"

df = quandl.get('WIKI/GOOGL')

#df = df.reset_index()

#print(df.head())
#df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
#df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100.0

#df = df[['Adj. Close', 'HL_PCT', 'PCT_change','Adj. Volume']]
#df = df[['Adj. Close', 'HL_PCT', 'PCT_change','Adj. Volume']]

#df.set_index('Date', inplace=True)
#df.index = pd.to_datetime(df.index)

#df = df[['Date','Adj. Close']]
#print(df.head())

plt.plot(df.index, df['Adj. Close'])

plt.legend(loc=4)
plt.xlabel('date')
plt.ylabel('price')
plt.show()