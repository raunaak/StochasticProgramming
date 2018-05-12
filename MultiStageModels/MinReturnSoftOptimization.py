import numpy as np
import pandas as pd
import math

mean = pd.read_csv('monthlymeanSeries5.csv', index_col=0)
variance = pd.read_csv('monthlyvarianceSeries5.csv', index_col=0)
returns = pd.read_csv('monthlyreturnPrices5.csv', index_col=0)

months = 1
meanNumpy = months * mean.as_matrix()
varianceNumpy = months * variance.as_matrix()
returnsNumpy = (months * months) * returns.as_matrix()
[observations, numStocks] = returnsNumpy.shape

mu = 0.05
weightList = []
returnList = []
sampleSize = 1000
timeHorizon = 4
initialWealth = 1
alpha = 0.95
'''CHANGE BETA'''
beta = 0.1

while len(weightList) != sampleSize:
    weight = np.random.random((numStocks, timeHorizon))
    weight = weight/sum(weight)
    expectedReturn = 0
    loss_distribution = []
    for i in range(observations - timeHorizon + 1):
        currentReturnMatrix = returnsNumpy[i:i+timeHorizon, :]
        expectedReturn += np.matmul(currentReturnMatrix, weight).diagonal().prod()
        loss_distribution.append(1 - np.matmul(currentReturnMatrix, weight).diagonal().prod())
    loss_distribution.sort()
    expectedReturn /= (observations - timeHorizon + 1)
    varMeasure = loss_distribution[int(math.ceil(alpha * (observations - numStocks + 1)))]
    print varMeasure
    if varMeasure <= beta:
        returnList.append(expectedReturn)
        weightList.append(weight)

bestWeights = weightList[np.argmax(returnList)]
print bestWeights
df = pd.DataFrame(bestWeights)
df.to_csv("multiStageMinReturnSoftOptimization.csv")
print np.max(returnList)
