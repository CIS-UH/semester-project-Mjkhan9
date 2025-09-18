Week 2 — Notes (Homework 2)  
Name: Mohammad Khan  
ID: 2245764  
Date: 09/18/25  

Homework 2 - Step 1 Assumptions and Estimation Approach  
Project name: Investment Portfolio Application  
Environment: Python 3 local machine  
No external APIs in this homework.  
Estimation uses simple person hours with a 25 percent contingency on tasks that are new to me. Durations assume 2-hour work blocks on weekdays.  

Homework 2 - Step 2 Work Breakdown Structure WBS  
1 Initiation and Requirements  
1.1 Review class slides and instructions  
1.2 Collect and refine user stories  
1.3 Define scope and constraints  

2 Design  
2.1 Data model for positions  
2.2 Function interfaces and I/O  

3 Implementation  
3.1 add_stock function  
3.2 add_bond function  
3.3 make_summary function  
3.4 make_text_report function  
3.5 Demo in main  

4 Validation and Testing  
4.1 Manual tests for valid inputs  
4.2 Manual tests for invalid inputs  
4.3 Sample data run and screenshots or logs  

5 Documentation  
5.1 Update README run steps  
5.2 Update SRS with FR and NFR  
5.3 Week 01 log update  

6 Project Management  
6.1 Schedule tracking and adjustments  
6.2 Final packaging and submission  

Homework 2 - Step 3 Activity List with Estimated hours  
A1 Review slides and assignment 2  
A2 Finalize 15 user stories and acceptance criteria 3  
A3 Scope and constraints write-up 1  
A4 Data model decisions 1  
A5 Plan function signatures 1  
A6 Implement add_stock 1  
A7 Implement add_bond 1.5  
A8 Implement make_summary 1  
A9 Implement make_text_report 1  
A10 Main demo script 0.5  
A11 Manual valid input tests 1  
A12 Manual invalid input tests 1  
A13 Sample run and save output 0.5  
A14 Update README 1  
A15 Update SRS 1  
A16 Update Week 01 notes 0.5  
A17 Schedule check and buffer 1  
A18 Package and submit 0.5  
Total estimated effort = 19.5 hours  

Homework 2 - Step 4 Dependencies  
A2 depends on A1  
A3 depends on A1  
A4 depends on A2 and A3  
A5 depends on A4  
A6 depends on A5  
A7 depends on A5  
A8 depends on A6 and A7  
A9 depends on A8  
A10 depends on A6 through A9  
A11 depends on A10  
A12 depends on A10  
A13 depends on A11 and A12  
A14 depends on A10 through A13  
A15 depends on A2 and A3 and A8  
A16 depends on A14 and A15  
A17 depends on A10 through A16  
A18 depends on A17  

Homework 2 - Step 5 Milestones  
M1 Requirements approved after A2 and A3  
M2 Core functions complete after A9  
M3 Demo run complete after A10  
M4 Testing complete after A13  
M5 Documentation complete after A16  
M6 Ready to submit after A18  

Homework 2 - Step 6 Schedule by Day  
Day 1 A1 A2 start 3 hours  
Day 2 A2 finish A3 A4 3 hours  
Day 3 A5 A6 2 hours  
Day 4 A7 A8 2.5 hours  
Day 5 A9 A10 1.5 hours  
Day 6 A11 A12 2 hours  
Day 7 A13 A14 1.5 hours  
Day 8 A15 A16 1.5 hours  
Day 9 A17 A18 1.5 hours  
Buffer: 1 hour spread across Days 6 to 9  

Homework 2 - Step 7 Risk Register summary  
R1 Underestimate coding time. Impact: slip functions not done on schedule. Response: add 25 percent buffer and cut optional formatting if needed.  
R2 Confusing acceptance tests. Impact: rework. Response: Review stories with class notes before coding.  
R3 Tool version issues. Impact: delays. Response: test on lab Python and avoid external packages.  
R4 Last-minute errors. Impact: submission quality. Response: finish one day early and use the buffer to fix issues.  

Homework 2 - Step 8 Sample Code Snippets  
Function to add a stock  
def add_stock(portfolio, ticker, quantity):  
    if not ticker or not ticker.strip():  
        raise ValueError("Please enter a ticker, like AAPL")  
    if quantity <= 0:  
        raise ValueError("Quantity must be positive")  
    t = ticker.strip().upper()  
    portfolio.append({"type": "STOCK", "ticker": t, "qty": float(quantity)})  

Function to add a bond  
def add_bond(portfolio, ticker, quantity, par, coupon):  
    if not ticker or not ticker.strip():  
        raise ValueError("Please enter a bond ticker or name")  
    if quantity <= 0:  
        raise ValueError("Quantity must be positive")  
    if par <= 0:  
        raise ValueError("Par must be positive")  
    if coupon < 0:  
        raise ValueError("Coupon must be non-negative")  
    t = ticker.strip().upper()  
    portfolio.append({  
        "type": "BOND",  
        "ticker": t,  
        "qty": float(quantity),  
        "par": float(par),  
        "coupon": float(coupon)  
    })  

Summary and report  
def make_summary(portfolio):  
    total = len(portfolio)  
    stocks = sum(1 for p in portfolio if p["type"] == "STOCK")  
    bonds = sum(1 for p in portfolio if p["type"] == "BOND")  
    return {  
        "total_items": total,  
        "stocks_only": stocks,  
        "bonds_only": bonds,  
        "positions": portfolio  
    }  

def make_text_report(portfolio):  
    lines = []  
    lines.append("Portfolio Report")  
    lines.append("-----------------")  
    if not portfolio:  
        lines.append("(empty)")  
        return "n".join(lines)  
    stock_count = sum(1 for p in portfolio if p["type"] == "STOCK")  
    bond_count = sum(1 for p in portfolio if p["type"] == "BOND")  
    lines.append(f"Positions: {len(portfolio)} | Stocks: {stock_count} | Bonds: {bond_count}")  
    lines.append("")  
    lines.append("Holdings:")  
    for p in portfolio:  
        if p["type"] == "STOCK":  
            lines.append(f"- STOCK  {p['ticker']:>6}  qty={p['qty']}")  
        else:  
            lines.append(f"- BOND   {p['ticker']:>6}  qty={p['qty']}  par={p.get('par', 0)}  coupon={p.get('coupon', 0)}")  
    return "n".join(lines)  

Demo  
if __name__ == "__main__":  
    data = []  
    add_stock(data, "AAPL", 5)  
    add_stock(data, "MSFT", 2)  
    add_bond(data, "US10Y", 3, 1000, 0.045)  
    print(make_summary(data))  
    print()  
    print(make_text_report(data))  

Homework 2 completion – step 9
Submission Checklist
- Mohammad Khan 2245764 at the top of the documents
- SRS updated with FR and NFR, and user stories
- README updated with run steps
- Week 01 notes updated with delivered items
- Code runs with python3 and prints a summary and a report

