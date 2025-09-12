# Homework 1
# Name: Mohammad Khan | ID: 2245764 | Date: 09/11/25

def add_stock(portfolio, ticker, quantity):
    if not ticker:
        raise ValueError("Please enter a ticker, like AAPL")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    ticker = ticker.strip().upper()
    portfolio.append({"type": "STOCK", "ticker": ticker, "qty": float(quantity)})

def make_summary(portfolio):
    total = len(portfolio)
    stocks = sum(1 for p in portfolio if p["type"] == "STOCK")
    return {"total_items": total, "stocks_only": stocks, "positions": portfolio}

if __name__ == "__main__":
    data = []
    add_stock(data, "AAPL", 5)
    add_stock(data, "MSFT", 2)
    print(make_summary(data))

