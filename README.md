
# Smart Portfolio Optimizer

**What is this project about?**

This project is a Smart Portfolio Optimizer that helps investors find the best mix of stocks using Modern Portfolio Theory (MPT). It fetches historical stock data, simulates thousands of portfolios, and identifies the ones with the best risk-return tradeoff. The tool visualizes the efficient frontier and highlights optimal portfolios, making it easy to see how to maximize returns for a given level of risk.

**Developer/Creator:** tubakhxn

## Features
- Fetches historical stock data using yfinance
- Calculates expected returns, covariance matrix, portfolio volatility, Sharpe ratio
- Generates 10,000+ random portfolios
- Identifies maximum Sharpe ratio and minimum volatility portfolios
- Visualizes efficient frontier and portfolio scatter plot
- Highlights optimal portfolios

## Structure
- main.py: Entry point for running the optimizer and visualizations
- optimizer.py: Contains portfolio optimization logic and calculations
- requirements.txt: Lists required Python packages
- README.md: Explains MPT math and project usage

## Modern Portfolio Theory (MPT) Math

Modern Portfolio Theory aims to maximize portfolio return for a given level of risk, or minimize risk for a given level of expected return. Key concepts:

- **Expected Returns ($\mu$):**
  $$\mu = \frac{1}{N} \sum_{i=1}^{N} r_i$$
  Where $r_i$ is the return for period $i$.

- **Covariance Matrix ($\Sigma$):**
  $$\Sigma_{ij} = \text{Cov}(r_i, r_j)$$
  Measures how returns of assets move together.

- **Portfolio Volatility ($\sigma_p$):**
  $$\sigma_p = \sqrt{w^T \Sigma w}$$
  Where $w$ is the vector of asset weights.

- **Sharpe Ratio ($S$):**
  $$S = \frac{\mu_p - r_f}{\sigma_p}$$
  Where $\mu_p$ is portfolio expected return, $r_f$ is risk-free rate, $\sigma_p$ is portfolio volatility.

- **Efficient Frontier:**
  The set of portfolios offering the highest expected return for a given risk.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the optimizer:
   ```bash
   python main.py
   ```

## Clean Finance-Style Visualization
- Efficient frontier plotted
- Portfolios colored by Sharpe ratio
- Optimal portfolios highlighted

---

For more details on MPT, see [Wikipedia](https://en.wikipedia.org/wiki/Modern_portfolio_theory).
