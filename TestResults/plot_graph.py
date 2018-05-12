import matplotlib.pyplot as plt
import pandas as pd

headers = ['Month','expectation maximization','variance minimization', 'utility', 'var as constraint', 'cvar', 'multi stage variance minimization', 'multi stage exp maximization']

df = pd.read_csv('RESULT1.csv')

print df

plt.plot(df['Month'], df['expectation maximization'], label='Exp Max (0.032603)')
plt.plot(df['Month'], df['variance minimization'], label='Variance Min (0.013746)')
plt.plot(df['Month'], df['utility'], label='Utility (0.044802)')
plt.plot(df['Month'], df['var as constraint'], label='Chance Constraint (0.010751)')
plt.plot(df['Month'], df['cvar'], label='CVAR (0.014164)')
plt.plot(df['Month'], df['multi stage variance minimization'], label='Multi stage Min Return (0.033784)')
plt.plot(df['Month'], df['multi stage exp maximization'], label='Multi stage Controlled VaR (0.021486)')
plt.legend(loc='upper left')
plt.xlabel('Month')
plt.ylabel('Total Return')
plt.show()