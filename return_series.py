import datetime
import pandas as pd
import numpy as np
import math

stockNames = ['NSE/RELIANCE', 'EOD/GS', 'NSE/MARUTI', 'EOD/MSFT', 'NSE/TCS']

dataframe = pd.read_csv('teststockPrices5.csv', index_col=0)
rows, cols = dataframe.shape
index = dataframe.index.values[0:-1]
returnSeries = pd.DataFrame(index=index, columns=stockNames)
returnSeries = returnSeries.fillna(0.0)

for row in range(rows-1):
    for col in range(cols):
        value = dataframe.iloc[row + 1][col] / dataframe.iloc[0][col]
        returnSeries.iloc[row][col] = value

print(returnSeries.to_string())
