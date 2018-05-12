import quandl
import datetime
import pandas as pd
import numpy as np
import time

quandl.ApiConfig = 'YOUR API KEY'

stockNames = ['NSE/RELIANCE', 'EOD/GS', 'NSE/MARUTI', 'EOD/MSFT', 'NSE/TCS']
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
            'NSE/GRASIM', 'NSE/TATASTEEL', 'NSE/INFRATEL']'''

i = 0
for stock in stockNames:
    print i
    try:
        data = quandl.get(stockNames[i], start_date='2017-01-01', end_date='2018-04-30', authtoken = 'YOUR API KEY', collapse='monthly')
        if i==0:
            index = data.index
            df_ = pd.DataFrame(index=index, columns=stockNames)
            df_ = df_.fillna(0)
            df_[stock] = data['Close']
        else:
            df_[stock] = data['Close']
        i = i + 1
    except:
        print("Again trying")
    time.sleep(5)
df_.to_csv('testStockPrices5.csv')
