Week 1 — Notes (Homework 1)  
Name: Mohammad Khan  
ID: 2245764  
Date: 09/11/25  

Homework 1  Step 1 Project Research  
I looked into various personal finance apps and portfolio trackers. Most tools seem to emphasize trading and short-term price fluctuations, but they often lack a straightforward, beginner-friendly method to monitor both stocks and basic bonds in a single interface. Users frequently express frustration over complicated screens, excessive menus, and struggles with understanding risk or diversification. For teaching and student projects, an easy-to-use app that enables users to add their positions and view clear summaries would be beneficial. Research indicates that an effective initial version should allow users to input stocks and bonds with minimal fields, generate a comprehensible summary, and produce a text-based report while offering simple diversification visuals in later updates. This project is aimed at individual learners, students, and new investors who seek basic tracking without the clutter of complex features.

Homework 1  Step 2 Project Acquisition  
This project was chosen due to the apparent gap between basic stock trackers and more advanced professional tools. Conversations with classmates and a teaching assistant revealed a common desire for a simple app that merely records positions and provides a clear summary. The success criteria include the ability to add stocks and bonds, validation against obvious bad inputs, and generating a straightforward report that can be printed or shared. Constraints include limited time during the semester, the absence of live price feeds for this assignment, and the need to keep the code concise and easy to comprehend. I plan to use Python, ensuring compatibility with most student laptops, and will incorporate pricing and reporting in subsequent homework assignments.

Homework 1  Step 3 Vision and Scope  
Vision  
The goal is to develop a simple portfolio tool that allows a new investor to log stocks and bonds while providing a clear summary and text report. It should be user-friendly, easy to grade, and capable of being enhanced later with pricing and chart features.

In Scope for HW1  
- Ability to add stocks with ticker symbols and quantities  
- Ability to add bonds with ticker symbols, quantities, par values, and coupon rates  
- Basic validation for empty ticker entries and non-positive numeric fields  
- Summary output that includes totals and positions  
- Plain text report for straightforward reading  

Out of Scope for HW1  
- User accounts  
- Real-time price quotes  
- Tax lots  
- CSV import/export  
- Charts  
- Bank integrations  

Stakeholders  
- Student developer: Mohammad Khan, ID 2245764  
- Instructor and grader  
- Classmates who will review the demo   

Homework 1 - Step 4 User Stories with Acceptance Criteria

1. As a user, I want to add a stock so I can keep track of my investments.  
   Acceptance Criteria (AC): When I enter "AAPL" and the quantity "5," the system should store this stock position and display it in my list of holdings. The quantity must be greater than 0, and the stock ticker should be in uppercase letters.

2. As a user, I want an error message if I try to add a stock with a non-positive quantity, so I can avoid inputting incorrect data.  
   AC: If I input a quantity of 0 or a negative number, the system should generate a clear error message and prevent the stock position from being added.

3. As a user, I want an error message if the stock ticker is empty, so I can avoid entering invalid data.  
   AC: If I provide an empty ticker or just spaces, the system should show a clear error message and not add the stock position.

4. As a user, I want to add a bond so I can track my fixed income investments.  
   AC: If I enter "US10Y," with a quantity of "3," par value of "1000," and a coupon rate of "0.045," the system should save this bond position with all relevant details. Both the quantity and par value must be greater than 0, and the coupon rate must be non-negative.

5. As a user, I want an error message if the bond par value is not positive, so I can prevent bad data entry.  
   AC: If I input a par value of 0 or a negative number, the system should display a clear error message and not add the bond position.

6. As a user, I want an error message if the bond coupon rate is negative, so I can avoid incorrect data entry.  
   AC: If the coupon rate I enter is less than 0, the system should generate a clear error message and prevent the bond position from being added.

7. As a user, I want a portfolio summary so I can see the totals quickly.  
**Acceptance Criteria:** The summary should return the total number of items, which counts positions for both stocks and bonds, and it should also display the list of positions.

8. As a user, I want a plain text report so I can easily copy and share it.  
**Acceptance Criteria:** The report needs to have a header line that shows counts by type and one line for each holding. For stocks, it should list the ticker and quantity. For bonds, it should show the ticker, quantity, par, and coupon.

9. As a user, I want tickers stored in uppercase to keep my data consistent.  
**Acceptance Criteria:** When I add a ticker in lowercase, it should be saved as uppercase in the positions list and also in the report.

10. As a user, I want to run a demo from the main function so I can see an example output.  
**Acceptance Criteria:** When I run the script, it should print a summary dictionary and a text report that includes at least two stocks or one stock and one bond.

11. As a user, I want basic input validation messages to let me know what needs fixing.  
**Acceptance Criteria:** If there’s any invalid input, it should raise a message that names the field and explains the problem, without crashing the program apart from the exception message.

12. As a user, I want the code to be small and easy to read so I can learn from it.  
**Acceptance Criteria:** Functions should be short and clearly named like add_stock, add_bond, make_summary, and make_text_report, with simple parameters and clear returns.

13. As a user, I want consistent numeric types so the math will work later.  
**Acceptance Criteria:** Quantities, par, and coupon should be stored as floats, allowing them to be used in calculations without any conversion errors.

14. As a user, I want no external dependencies so that it can run on lab computers.  
**Acceptance Criteria:** The script should only use the standard Python library and should run with the python3 command.

15. As a user, I want safe handling of empty portfolios to avoid errors.  
**Acceptance Criteria:** If the portfolio is empty, the summary should return zero counts, and the report should display the header along with the word "empty." 
