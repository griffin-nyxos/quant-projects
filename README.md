# S&P500 Behavior Analysis

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