import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

# Define the stock symbol and create a Ticker object
symbol = "MSFT"
stock = yf.Ticker(symbol)

# Calculate yesterday's date
date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# Get stock price from yesterday and extract the closing price (rounded to 2 decimal places)
closing_price = round(stock.history(period="1d", start=date)["Close"].iloc[0], 2)

# Get the number of shares from a specific date
num_shares = stock.get_shares_full(start="2022-01-01", end=None)

# Extract the last value (rounded to 2 decimal places) and date from the Series
last_value = round(num_shares.iloc[-1], 2)
last_date = num_shares.index[-1].date()

# Calculate market cap (rounded to 2 decimal places)
market_cap = round(closing_price * last_value, 2)

# Print the results
print(f"Closing price on {date}: ${closing_price}")
print(f"No. of shares on {last_date}: ${last_value}")
print(f"Market cap on {date}: ${market_cap}")
