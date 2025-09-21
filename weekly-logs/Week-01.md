Name: Mohammad Khan
ID: 2245764
Date: September 21, 2025

Homework 1: Project Initiation - Vision, Scope, and Requirements

1.1 Project Acquisition and Vision
Software Corp was chosen because we have a proven track record of creating small, reliable finance tools. Our goal is to build a straightforward Stocks and Bonds tracker that is easy to use and simple to maintain. We will keep the work focused and avoid scope growth. This tracker is for individual investors who want a clear way to monitor their holdings.

1.2 Software Requirements Specification (SRS)

Purpose
State what the product will do and what is included in the first release. This document guides design, development, testing, and acceptance.

Scope
A web-based tracker for one user. The user records stocks and bonds, manages a watchlist, and views basic summaries. No trading. No advice.

Overall Description
The target user is an individual investor. The app shows simple forms and tables. It stores data and keeps it consistent. A short help page explains each field.

Constraints
Keep the feature set small in the first release. Favor clarity over complexity. Use common, well-understood patterns.

Assumptions
This is a class project. The priority is a clean scope, working features, and a straightforward handoff.

Functional Requirements
FR1 Add a stock with a ticker, quantity, price, and date.
FR2 Edit a stock record.
FR3 Delete a stock record.
FR4 Add a bond with face value, coupon, and maturity date.
FR5 Edit a bond record.
FR6 Delete a bond record.
FR7 Create and manage a watchlist of tickers.
FR8 Search by ticker across holdings and watchlist.
FR9 Import holdings from a CSV file.
FR10 Export holdings to a CSV file.

Non-Functional Requirements
NFR1 The UI is consistent across pages.
NFR2 Input validation blocks empty tickers and negative quantities.
NFR3 Errors show short messages that explain what to fix.
NFR4 The system saves and loads data without loss.
NFR5 The design is simple enough that a new developer can read it quickly.

User Stories
US1: As a user, I can add a stock so I can track it.
US2: As a user, I can edit a stock so I can correct mistakes.
US3: As a user, I can delete a stock so I can clean up my list.
US4: As a user, I can add a bond so I can track income.
US5: As a user, I can edit a bond so I can correct values.
US6: As a user, I can delete a bond so I can remove outdated data.
US7: As a user, I can search by ticker so I can find items quickly.
US8: As a user, I can sort tables so I can review data efficiently.
US9: As a user, I can create a watchlist so I can monitor investment ideas.
US10: As a user, I can import a CSV so I can add multiple records at once.
US11: As a user, I can export a CSV so I can back up my data.
US12: As a user, I can see a summary count so I understand my portfolio’s scope.
US13: As a user, I can view simple totals so I know the overall value.
US14: As a user, I can read concise help text so I enter data accurately.
US15: As a user, I can undo the last delete so I can recover information quickly.

Use Case - Add Stock
Actor: user
Precondition: app is open
Main flow
1 enter ticker, quantity, price, and date
2 system validates input
3 system saves the record
4 system shows it in the table
Alternate flow
2a invalid input shows a short message and keeps the form
   Acceptance Criteria: If the portfolio is empty, the summary should return zero counts, and the report should indicate that it is empty.
