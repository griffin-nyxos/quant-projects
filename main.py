import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download S&P500 data
sp500 = yf.download("^GSPC", start="2020-01-01", end="2024-12-31")

# Calculate Daily Return
sp500["Daily Return"] = sp500["Close"].pct_change()

# Plot Cumulative Return
(1 + sp500["Daily Return"]).cumprod().plot(title="S&P500 Cumulative Return")
plt.ylabel("Growth of $1")
plt.show()

print(sp500.head())
print(type(sp500))