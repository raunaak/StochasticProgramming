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
#print np.random.random(meanNumpy.shape).shape
mu = 0.05
weightList = []
lossList = []
expectedReturnList = []
sampleSize = 1000
timeHorizon = 4
initialWealth = 1
alpha = 0.95

while len(weightList) != sampleSize:
    weight = np.random.random((numStocks, timeHorizon))
    weight = weight/sum(weight)
    #R = (np.transpose(weight), returnsNumpy)
    #[m, n] = R.shape
    expectedReturn = 0
    loss_distribution = []
    for i in range(observations - timeHorizon + 1):
        currentReturnMatrix = returnsNumpy[i:i + timeHorizon, :]
        #currentReturnMatrix = returnsNumpy[i:i+numStocks, :]
        expectedReturn += np.matmul(currentReturnMatrix,weight).diagonal().prod()
        loss_distribution.append(1 - np.matmul(currentReturnMatrix, weight).diagonal().prod())
    expectedReturn /= (observations - timeHorizon + 1)
    print expectedReturn
    if expectedReturn - 1>= mu:
        print expectedReturn
        weightList.append(weight)
        loss_distribution.sort()
        varMeasure = loss_distribution[int(math.ceil(alpha * (observations - numStocks + 1)))]
        lossList.append(varMeasure)
        expectedReturnList.append(expectedReturn)

bestWeights = weightList[np.argmin(lossList)]
print bestWeights
df = pd.DataFrame(bestWeights)
df.to_csv("multiStageVarMinSoftOptimization.csv")

print expectedReturnList[np.argmin(lossList)]
