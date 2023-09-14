from fastapi import FastAPI, Query
import yfinance as yf

app = FastAPI()

@app.get("/get_closing_quote")
async def get_closing_quote(
    symbol: str = Query(..., description="Stock symbol"),
    date: str = Query(..., description="Date in YYYY-MM-DD format"),
):
    try:
        # Use yfinance to fetch historical data for the specified date
        stock = yf.Ticker(symbol)
        historical_data = stock.history(period="1d", start=date, end=date)

        if historical_data.empty:
            return {"error": "No data available for the specified date"}

        # Extract the closing quote and number of shares outstanding (market cap)
        closing_quote = historical_data["Close"].iloc[0]
        shares_outstanding = stock.info.get("sharesOutstanding")

        if shares_outstanding is None:
            return {"error": "Shares outstanding data not available"}

        # Calculate market cap
        market_cap = closing_quote * shares_outstanding

        return {
            "symbol": symbol,
            "date": date,
            "closing_quote": closing_quote,
            "shares_outstanding": shares_outstanding,
            "market_cap": market_cap,
        }
    except Exception as e:
        return {"error": str(e)}
