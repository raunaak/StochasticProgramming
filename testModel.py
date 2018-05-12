import datetime
import pandas as pd
import numpy as np
import math

dataframe = pd.read_csv('testreturnPricesPerMonth5.csv', index_col=0)
rows, cols = dataframe.shape

weight = [
[0.042409505, 0.125266863, 0.000533702, 0.104495231],
[0.001447582, 0.122846935, 0.146846067, 0.037387058],
[0.225348595, 0.24337832, 0.509333427, 0.29973329],
[0.275083533, 0.289575621, 0.213048959, 0.264337767],
[0.455710786, 0.218932261, 0.130237844, 0.294046654]
]

timePeriod = 4
print weight
return_numpy = dataframe.as_matrix()
data = np.matmul(return_numpy, weight)
returnList = [1]
for i in range(data.shape[0]):
    returnList.append(returnList[-1] * data[i][i%timePeriod])
df = pd.DataFrame(returnList)
df.to_csv('weights.csv')