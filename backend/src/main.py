from fastapi import FastAPI
from database import MarketCapDatabase
from pymongo import MongoClient

app = FastAPI()
db_url = "mongodb://localhost:27017/"
db_name = "market_cap_db"
db = MarketCapDatabase(db_url, db_name)

@app.get("/get_stock_data")
async def get_stock_data(symbol: str):
    stock_data = db.db.stock_data.find_one({"symbol": symbol})
    if stock_data:
        return {
            "symbol": stock_data["symbol"],
            "closing_price": stock_data["closing_price"],
            "market_cap": stock_data["market_cap"],
            "last_update": stock_data["last_update"],
        }
    else:
        return {"error": "Symbol not found"}
