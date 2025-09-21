Software Requirements Specification
Homework 1
Name: Mohammad Khan
ID: 2245764
Date: September 18, 2025

Purpose
This document outlines the requirements for a user-friendly portfolio management tool designed for individual investors. The primary function of this tool is to allow users to add stock holdings while providing a clear summary of their investment portfolio. Future updates will include features for managing bond investments and generating detailed plain text reports for tracking purposes.

Scope
The system will enable users to efficiently add stocks to their portfolios by providing key details such as the ticker symbol and the number of shares. After adding stocks, the system will create a summary that includes total counts for stocks and bonds, along with a detailed list of each stock position. Future enhancements will add functionality for bond management, including relevant attributes like par value and coupon rates, as well as the generation of reports for comprehensive analysis.

Functional Requirements

FR1: The system shall include a user interface that allows users to enter stock information, with fields for the ticker symbol (representing the company’s stock) and the quantity of shares owned.
FR2: The system shall generate a portfolio summary that displays the total count of stock holdings, total count of bond holdings (once implemented), and a detailed list of individual stock positions, including their ticker symbols and associated quantities.
FR3: The system shall allow users to add bonds in future assignments, requiring the input of fields such as the ticker symbol, quantity, par value (the bond’s face value), and the coupon rate (the interest payment rate).
FR4: The system shall generate a plain text report summarizing the portfolio holdings and their performance, to be developed in later assignments.

Non-Functional Requirements

NFR1: The code must be clearly written to ensure that it is easy to read and understand, facilitating future maintenance and updates. Appropriate naming conventions and documentation will be required.
NFR2: The program must include robust error handling to manage invalid user inputs gracefully. It should provide clear feedback without crashing or failing unexpectedly.
NFR3: The program must be developed using Python 3 standards and utilize only the standard library, ensuring compatibility and minimizing external dependencies.

Use Case: Adding a Stock

Actor: User
Precondition: The program is fully operational and the user has launched the application.
Steps:
The user displays the user interface and enters the desired ticker symbol of the stock, along with a positive integer representing the number of shares.
The system checks the inputs for correctness and validity (for example, ensuring the ticker symbol is correctly formatted and the quantity is a positive integer). If the inputs are valid, the system converts the ticker symbol to uppercase, records the stock position, and updates the overall summary.
Postcondition: The newly added stock will be reflected in the list of investment positions, and the portfolio summary will accurately display the updated totals, providing the user with an overview of their investments.

Constraints
Features related to user accounts, real-time price feeds, capabilities for importing and exporting CSV files, chart generation, and bank integrations are not included in this assignment’s scope.

Stakeholders
The primary stakeholder is Mohammad Khan, the student developer (ID: 2245764). Additional stakeholders include the instructor and grader, as well as classmates who will participate in the review and demonstration of the project.

Assumptions and Dependencies
The successful implementation of this system relies on the availability of Python 3 on lab computers and student laptops. It is assumed that no third-party packages or libraries will be needed for basic functionality, streamlining the development process.
