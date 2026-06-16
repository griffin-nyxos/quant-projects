# Quant Projects

## Phase 1 — S&P500 Behavior Analysis

Exploratory analysis of S&P500 historical price data using Python.

## What This Project Does
- Downloads historical S&P500 data via yfinance
- Calculates daily returns
- Plots cumulative return (growth of $1 invested in 2020)

## How to Run
1. Clone this repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install pandas numpy matplotlib yfinance`
5. Run: `python main.py`

## Key Concepts
- **Daily Return** = % price change day-over-day
- **Cumulative Return** = growth of $1 if held from start date

## Tech Stack
- Python, pandas, matplotlib, yfinance

---

## Phase 2 — SMA Strategy vs Buy & Hold

Backtest comparing a Simple Moving Average (SMA) crossover 
strategy against Buy & Hold on S&P500 (2010–2024).

## Strategy Logic
- Buy when SMA50 crosses above SMA200 (Golden Cross)
- Exit when SMA50 crosses below SMA200 (Death Cross)

## How to Run
1. Clone this repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Mac) 
   or `venv\Scripts\activate` (Windows)
4. Install: `pip install pandas numpy matplotlib yfinance`
5. Run: `python phase2_sma.py`

## Result
Buy & Hold outperformed SMA Strategy over 14 years.
Active switching caused missed updays and signal noise.

## Key Lesson
Simple long-term investing beats most active strategies
over sufficient time horizons.

## Tech Stack
Python, pandas, numpy, matplotlib, yfinance


## Test Commit Command
This part is irrelevant with all of these above project It's just Test