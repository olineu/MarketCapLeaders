from database import MarketCapDatabase

if __name__ == "__main__":
    db_url = "mongodb://localhost:27017/"
    db_name = "market_cap_db"
    db = MarketCapDatabase(db_url, db_name)
    db.update_daily_data()
