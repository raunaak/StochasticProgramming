import datetime
import pandas as pd
import numpy as np
import math

'''
stockNames = ['NSE/RELIANCE', 'NSE/TCS', 'NSE/HDFCBANK', 'NSE/ITC', 'NSE/HDFC',
            'NSE/HINDUNILVR', 'NSE/MARUTI', 'NSE/INFY', 'NSE/SBIN', 'NSE/ONGC',
            'NSE/KOTAKBANK', 'NSE/LT', 'NSE/ICICIBANK', 'NSE/COALINDIA', 'NSE/IOC',
            'NSE/BHARTIARTL', 'NSE/NTPC', 'NSE/HINDZINC', 'NSE/HCLTECH', 'NSE/WIPRO',
            'NSE/AXISBANK', 'NSE/SUNPHARMA', 'NSE/BAJFINANCE', 'NSE/ASIANPAINT', 'NSE/INDUSINDBK',
            'NSE/ULTRACEMCO', 'BSE/BOM500295', 'NSE/TATAMOTORS', 'NSE/POWERGRID',
            'NSE/MM', 'NSE/BPCL', 'NSE/BAJAJFINSV', 'NSE/TITAN',
            'BSE/BOM505200', 'NSE/NESTLEIND', 'NSE/BAJAJ_AUTO', 'NSE/ADANIPORTS', 'NSE/HEROMOTOCO',
            'NSE/GAIL', 'NSE/JSWSTEEL', 'NSE/GODREJCP', 'NSE/MOTHERSUMI', 'NSE/YESBANK',
            'NSE/GRASIM', 'NSE/TATASTEEL', 'NSE/INFRATEL']
'''
stockNames = ['NSE/RELIANCE', 'EOD/GS', 'NSE/MARUTI', 'EOD/MSFT', 'NSE/TCS']

dataframe = pd.read_csv('monthlyreturnPrices5.csv', index_col=0)
rows, cols = dataframe.shape
index = dataframe.index.values
returnArray = dataframe.values
print(returnArray.shape)
meanArray = returnArray.mean(axis = 0, keepdims = True)
print(meanArray.shape)
varianceMatrix = np.matmul((returnArray.T - meanArray.T), (returnArray - meanArray))/ rows
varianceDataframe = pd.DataFrame(data=varianceMatrix,index=stockNames,columns=stockNames)
varianceDataframe.to_csv('monthlyvarianceSeries5.csv')
meanDataframe = pd.DataFrame(data=meanArray, columns=stockNames)
meanDataframe.to_csv('monthlymeanSeries5.csv')