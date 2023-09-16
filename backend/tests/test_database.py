import pytest
from pymongo import MongoClient
from datetime import datetime
from database import MarketCapDatabase

@pytest.fixture
def test_db():
    # Set up a temporary test database
    client = MongoClient("mongodb://localhost:27017/")
    db_name = "test_market_cap_db"
    test_db = client[db_name]
    yield test_db
    client.drop_database(db_name)

def test_update_daily_data(test_db, monkeypatch):
    # Mock the datetime function to always return a fixed date
    fixed_date = datetime(2023, 9, 14)  # Replace with the desired date
    monkeypatch.setattr("database.datetime", lambda: fixed_date)

    # Initialize the MarketCapDatabase with the test database
    db = MarketCapDatabase()
    db.client = test_db

    # Define a sample symbol and test data
    symbol = "AAPL"
    test_data = {
        "symbol": symbol,
        "closing_price": 150.0,
        "market_cap": 2000000000000.0,
        "last_update": datetime(2023, 9, 13),
    }

    # Insert the sample data into the test database
    test_db.stock_data.insert_one(test_data)

    # Run the update_daily_data method
    db.update_daily_data()

    # Retrieve the updated data from the test database
    updated_data = test_db.stock_data.find_one({"symbol": symbol})

    # Check if the data was updated correctly
    assert updated_data is not None
    assert updated_data["symbol"] == symbol
    assert updated_data["last_update"] == fixed_date
    # Add more assertions for other fields as needed

if __name__ == "__main__":
    pytest.main()
