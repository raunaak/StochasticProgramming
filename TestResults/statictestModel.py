import datetime
import pandas as pd
import numpy as np
import math

dataframe = pd.read_csv('testreturnPricesPerMonth5.csv', index_col=0)
rows, cols = dataframe.shape

weight = np.array([
0.20643,
0.01576,
0.08016,
0.24773,
0.44990
])

timePeriod = 1
print weight
print len(weight)
return_numpy = dataframe.as_matrix()
data = np.matmul(return_numpy, weight)
returnList = [1]
for i in range(data.shape[0]):
    returnList.append(returnList[-1] * data[i])
df = pd.DataFrame(returnList)
df.to_csv('weights.csv')