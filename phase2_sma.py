import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Download data
df = yf.download("^GSPC", start="2010-01-01", end="2024-12-31")

# Calculate SMA
df["SMA50"] = df["Close"].rolling(window=50).mean()
df["SMA200"] = df["Close"].rolling(window=200).mean()

# Plot
plt.figure(figsize=(14, 6))
df["Close"].plot(label="S&P500", alpha=0.7)
df["SMA50"].plot(label="SMA 50")
df["SMA200"].plot(label="SMA 200")
plt.legend()
plt.title("S&P500 with SMA50 and SMA200")
plt.show()

# ── ต่อจากนี้ ──

# สร้าง Signal
df["Signal"] = np.where(df["SMA50"] > df["SMA200"], 1, 0)

# คำนวณ Daily Return
df["Market Return"] = df["Close"].pct_change()

# คำนวณ Strategy Return
df["Strategy Return"] = df["Market Return"] * df["Signal"].shift(1)

print(df[["Market Return", "Signal", "Strategy Return"]].tail(10))

# Cumulative Return ของทั้งคู่
df["Cumulative Market"] = (1 + df["Market Return"]).cumprod()
df["Cumulative Strategy"] = (1 + df["Strategy Return"]).cumprod()

# Plot เปรียบเทียบ
plt.figure(figsize=(14, 6))
df["Cumulative Market"].plot(label="Buy & Hold")
df["Cumulative Strategy"].plot(label="SMA Strategy")
plt.legend()
plt.title("SMA Strategy vs Buy & Hold")
plt.ylabel("Growth of $1")
plt.show()