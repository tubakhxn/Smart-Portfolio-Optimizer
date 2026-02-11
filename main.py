import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from optimizer import PortfolioOptimizer

# User configuration
TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
START_DATE = '2020-01-01'
END_DATE = '2025-01-01'
RISK_FREE_RATE = 0.01
NUM_PORTFOLIOS = 10000

# Initialize optimizer
optimizer = PortfolioOptimizer(TICKERS, START_DATE, END_DATE, RISK_FREE_RATE)
results = optimizer.simulate_portfolios(NUM_PORTFOLIOS)
optimal = optimizer.get_optimal_portfolios(results)

# Prepare data for plotting
returns = np.array(results['returns'])
volatility = np.array(results['volatility'])
sharpe = np.array(results['sharpe'])
weights = np.array(results['weights'])

# Plot Efficient Frontier
plt.figure(figsize=(10, 7))
scatter = plt.scatter(volatility, returns, c=sharpe, cmap='viridis', alpha=0.6, edgecolor='k')
plt.colorbar(scatter, label='Sharpe Ratio')

# Highlight optimal portfolios
plt.scatter(optimal['max_sharpe']['volatility'], optimal['max_sharpe']['return'],
            color='red', marker='*', s=300, label='Max Sharpe Ratio')
plt.scatter(optimal['min_volatility']['volatility'], optimal['min_volatility']['return'],
            color='blue', marker='*', s=300, label='Min Volatility')

plt.title('Efficient Frontier - Smart Portfolio Optimizer')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display optimal weights
print("\nOptimal Portfolio Weights:")
print("Max Sharpe Ratio Portfolio:")
for ticker, weight in zip(TICKERS, optimal['max_sharpe']['weights']):
    print(f"  {ticker}: {weight:.2%}")
print("\nMin Volatility Portfolio:")
for ticker, weight in zip(TICKERS, optimal['min_volatility']['weights']):
    print(f"  {ticker}: {weight:.2%}")

plt.show()
