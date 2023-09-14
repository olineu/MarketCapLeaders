import yfinance as yf
from datetime import datetime, timedelta

# Create a Ticker object for the stock you want to retrieve data for
ticker_symbol = "MSFT"  # Replace with the symbol of the stock you're interested in
stock = yf.Ticker(ticker_symbol)

# Calculate yesterday's date
yesterday = datetime.now() - timedelta(days=1)
date = yesterday.strftime("%Y-%m-%d")

# Get historical market data for yesterday's date
historical_data = stock.history(period="1d", start=date)

# Extract the closing price for yesterday's date
closing_price = historical_data["Close"].iloc[0]

print(f"Closing price on {date}: ${closing_price}")
