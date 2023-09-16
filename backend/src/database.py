from pymongo import MongoClient
from decouple import config
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

class MarketCapDatabase:
    def __init__(self):
        db_url = config("DB_URL")
        db_name = config("DB_NAME")
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]

    def update_daily_data(self):
        # Load tickers from the CSV file
        tickers = pd.read_csv("tickers/tickers.csv")["Symbol"]

        # Calculate yesterday's date
        yesterday = datetime.now() - timedelta(days=1)
        date = yesterday.strftime("%Y-%m-%d")

        for symbol in tickers:
            # Create a Ticker object for the stock
            stock = yf.Ticker(symbol)

            # Get historical market data for yesterday
            stock_price = stock.history(period="1d", start=date)
            if not stock_price.empty:
                closing_price = stock_price["Close"].iloc[0]
            else:
                closing_price = None

            # Get number of shares from yesterday
            num_shares = stock.get_shares_full(start="2022-01-01", end=None)
            df = pd.DataFrame(num_shares)

            # Extract the last value
            if not df.empty:
                last_column = df.iloc[:, -1]
                last_value = last_column.iloc[-1]
            else:
                last_value = None

            # Calculate market cap
            market_cap = (
                closing_price * last_value
                if closing_price is not None and last_value is not None
                else None
            )

            # Update or insert data into the database
            self.db.stock_data.update_one(
                {"symbol": symbol},
                {
                    "$set": {
                        "closing_price": closing_price,
                        "market_cap": market_cap,
                        "last_update": datetime.now(),
                    }
                },
                upsert=True,
            )

if __name__ == "__main__":
    db = MarketCapDatabase()
    db.update_daily_data()
