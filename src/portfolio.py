# Stocks and Bonds Management Software
# Name Mohammad Khan | ID 2245764 | Date 09/18/25

def _normalize_ticker(ticker):
    if ticker is None or not str(ticker).strip():
        raise ValueError("ticker must not be empty")
    return str(ticker).strip().upper()

def _as_positive(name, value):
    try:
        v = float(value)
    except Exception:
        raise ValueError(f"{name} must be a number")
    if v <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return v

def _as_non_negative(name, value):
    try:
        v = float(value)
    except Exception:
        raise ValueError(f"{name} must be a number")
    if v < 0:
        raise ValueError(f"{name} must be non negative")
    return v

def add_stock(portfolio, ticker, quantity):
    t = _normalize_ticker(ticker)
    qty = _as_positive("quantity", quantity)
    portfolio.append({"type": "STOCK", "ticker": t, "qty": float(qty)})

def add_bond(portfolio, ticker, quantity, par, coupon):
    t = _normalize_ticker(ticker)
    qty = _as_positive("quantity", quantity)
    par_val = _as_positive("par", par)
    coupon_val = _as_non_negative("coupon", coupon)
    portfolio.append({
        "type": "BOND",
        "ticker": t,
        "qty": float(qty),
        "par": float(par_val),
        "coupon": float(coupon_val)
    })

def make_summary(portfolio):
    total = len(portfolio)
    stocks = sum(1 for p in portfolio if p.get("type") == "STOCK")
    bonds = sum(1 for p in portfolio if p.get("type") == "BOND")
    return {
        "total_items": total,
        "stocks_only": stocks,
        "bonds_only": bonds,
        "positions": portfolio
    }

def make_text_report(portfolio):
    lines = []
    lines.append("Portfolio Report")
    lines.append("---------------")
    if not portfolio:
        lines.append("empty")
        return "\n".join(lines)
    stock_count = sum(1 for p in portfolio if p.get("type") == "STOCK")
    bond_count = sum(1 for p in portfolio if p.get("type") == "BOND")
    lines.append(f"Positions: {len(portfolio)}  Stocks: {stock_count}  Bonds: {bond_count}")
    lines.append("")
    lines.append("Holdings")
    for p in portfolio:
        if p.get("type") == "STOCK":
            lines.append(f"STOCK {p['ticker']} qty={float(p['qty'])}")
        elif p.get("type") == "BOND":
            lines.append(f"BOND {p['ticker']} qty={float(p['qty'])} par={float(p['par'])} coupon={float(p['coupon'])}")
    return "\n".join(lines)

if __name__ == "__main__":
    data = []
    add_stock(data, "AAPL", 5)
    add_stock(data, "MSFT", 2)
    add_bond(data, "US10Y", 3, 1000, 0.045)
    print(make_summary(data))
    print()
    print(make_text_report(data))
