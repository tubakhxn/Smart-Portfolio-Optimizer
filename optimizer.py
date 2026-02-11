import pandas as pd
import numpy as np
import yfinance as yf

class PortfolioOptimizer:
    def __init__(self, tickers, start_date, end_date, risk_free_rate=0.01):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.risk_free_rate = risk_free_rate
        self.data = self._fetch_data()
        self.returns = self._calculate_returns()
        self.expected_returns = self.returns.mean()
        self.cov_matrix = self.returns.cov()

    def _fetch_data(self):
        df = yf.download(self.tickers, start=self.start_date, end=self.end_date)
        # Try to get 'Adj Close' if available, else fallback to 'Close'
        if ('Adj Close' in df.columns.get_level_values(0)):
            price = df['Adj Close']
        else:
            price = df['Close']
        return price.dropna()

    def _calculate_returns(self):
        return self.data.pct_change().dropna()

    def simulate_portfolios(self, num_portfolios=10000):
        results = {
            'returns': [],
            'volatility': [],
            'sharpe': [],
            'weights': []
        }
        for _ in range(num_portfolios):
            weights = np.random.dirichlet(np.ones(len(self.tickers)), size=1)[0]
            port_return = np.dot(weights, self.expected_returns)
            port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
            sharpe = (port_return - self.risk_free_rate) / port_volatility
            results['returns'].append(port_return)
            results['volatility'].append(port_volatility)
            results['sharpe'].append(sharpe)
            results['weights'].append(weights)
        return results

    def get_optimal_portfolios(self, results):
        max_sharpe_idx = np.argmax(results['sharpe'])
        min_vol_idx = np.argmin(results['volatility'])
        return {
            'max_sharpe': {
                'return': results['returns'][max_sharpe_idx],
                'volatility': results['volatility'][max_sharpe_idx],
                'sharpe': results['sharpe'][max_sharpe_idx],
                'weights': results['weights'][max_sharpe_idx]
            },
            'min_volatility': {
                'return': results['returns'][min_vol_idx],
                'volatility': results['volatility'][min_vol_idx],
                'sharpe': results['sharpe'][min_vol_idx],
                'weights': results['weights'][min_vol_idx]
            }
        }
