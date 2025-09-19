Week 1 Notes - Homework 1  

Name: Mohammad Khan  
ID: 2245764  
Date: 09/18/25  

Homework 1 Step 1: Project Research  
I researched personal finance apps and portfolio trackers. Many existing tools focus on trading and short-term price changes, which can be complex for beginners. For this student project, I believe a simple tool that allows users to add their positions and view a clear summary will be more beneficial.  

Homework 1 Step 2: Project Acquisition  
I chose this project after discussing it with classmates and a teaching assistant, who expressed a need for a straightforward app that records investment positions and generates a clear summary. Success for this project means the program can add stocks and bonds, validate obvious erroneous inputs, and produce a simple report. Constraints include limited time, the absence of live price feeds for this assignment, and the necessity to keep the code simple and easy to read. I plan to use Python and will consider adding price features and reporting later.  

Homework 1 Step 3: Vision and Scope  
The vision is to create a basic portfolio tool that allows new investors to log stocks and bonds and view a clear summary and text report. It should be easy to grade and simple to extend with pricing and charts in the future.  

In scope for Homework 1 are the following features:  
- The ability to add stocks with a ticker symbol and quantity.  
- The ability to add bonds with a ticker symbol, quantity, par value, and coupon rate.  
- Basic validation for empty tickers and non-positive numbers.  
- A summary that displays totals and positions.  
- A plain text report.  

Out of scope for Homework 1 are:  
- User accounts  
- Real-time price quotes  
- Tax lot management  
- CSV import/export  
- Charts  
- Bank integrations  

The stakeholders for this project include the student developer, Mohammad Khan (ID: 2245764), the instructor and grader, and classmates who will review the demo.  

Homework 1 Step 4: User Stories with Acceptance Criteria  
1. User Story: As a user, I want to add a stock so I can keep track of my investments.  
   Acceptance Criteria: When I enter "AAPL" and the quantity "5," the system stores the stock and shows it in the holdings list. The quantity must be greater than zero, and the ticker must be stored in uppercase.  

2. User Story: As a user, I want an error if I add a stock with a non-positive quantity.  
   Acceptance Criteria: If I enter zero or a negative number, the system displays a clear error message and does not add the position.  

3. User Story: As a user, I want an error if the stock ticker is empty.  
   Acceptance Criteria: If I provide an empty ticker or use spaces, the system will show a clear message and will not add the position.  

4. User Story: As a user, I want to add a bond so I can track fixed income.  
   Acceptance Criteria: If I enter "US10Y" with quantity "3," par value "1000," and coupon rate "0.045," the system saves the bond. Both quantity and par value must be greater than zero, and the coupon rate must be non-negative.  

5. User Story: As a user, I want a portfolio summary so I can quickly see totals.  
   Acceptance Criteria: The summary should return the total number of items, along with the counts of stocks and bonds, and should display the list of positions.  

6. User Story: As a user, I want a plain text report so that it is easy to copy and share.  
   Acceptance Criteria: The report should include a header with counts and one line per holding. For stocks, it should show the ticker and quantity. For bonds, it should display the ticker, quantity, par value, and coupon rate.  

7. User Story: As a user, I want safe handling of an empty portfolio.  
   Acceptance Criteria: If the portfolio is empty, the summary should return zero counts, and the report should indicate that it is empty.
