import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

mean = pd.read_csv('monthlymeanSeries5.csv', index_col=0)
variance = pd.read_csv('monthlyvarianceSeries5.csv', index_col=0)
mean_numpy = mean.as_matrix()
variance_numpy = variance.as_matrix()

one, num_assets = mean_numpy.shape
#print num_assets
num_portfolios = 500000

port_returns = []
port_volatility = []
stock_weights = []

for single_portfolio in range(num_portfolios):
    weights = np.random.random((num_assets, 1))
    weights /= np.sum(weights)
    #print weights.shape
    returns = np.dot(mean_numpy, weights)
    volatility = np.sqrt(np.dot(weights.T, np.dot(variance_numpy, weights)))
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

plt.scatter(x = port_volatility, y = port_returns)
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
plt.show()
