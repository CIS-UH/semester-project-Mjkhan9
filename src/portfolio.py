# Homework 1
# Name: Mohammad Khan | ID: 2245764 | Date: 09/18/25

def add_stock(portfolio, ticker, quantity):
    """Add a stock with ticker and quantity"""
    if not ticker or not ticker.strip():
        raise ValueError("Ticker cannot be empty. Example: AAPL")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    ticker = ticker.strip().upper()
    portfolio.append({"type": "STOCK", "ticker": ticker, "qty": float(quantity)})

def make_summary(portfolio):
    """Return a summary of the portfolio"""
    total = len(portfolio)
    stocks = sum(1 for p in portfolio if p["type"] == "STOCK")
    return {
        "total_items": total,
        "stocks_only": stocks,
        "positions": portfolio
    }

def make_text_report(portfolio):
    """Return a plain text report (stub for Homework 2)"""
    lines = []
    lines.append("Portfolio Report")
    lines.append("---------------")
    if not portfolio:
        lines.append("empty")
        return "\n".join(lines)
    for p in portfolio:
        if p["type"] == "STOCK":
            lines.append(f"STOCK {p['ticker']} qty={p['qty']}")
    return "\n".join(lines)

if __name__ == "__main__":
    data = []
    add_stock(data, "AAPL", 5)
    add_stock(data, "MSFT", 2)
    print(make_summary(data))
    print()
    print(make_text_report(data))
