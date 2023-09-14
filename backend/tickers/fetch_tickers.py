import pandas as pd

# Read the CSV file
df = pd.read_csv("nasdaq_screener.csv")

# Extract the "Symbol" column
tickers = df["Symbol"]

# Save the tickers to a new CSV file
tickers.to_csv("tickers.csv", index=False, header=False)
