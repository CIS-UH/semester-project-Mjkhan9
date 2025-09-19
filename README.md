Stocks and Bonds Management Software  
Homework 1  
Name: Mohammad Khan  
ID: 2245764  
Date: 09/11/25  

Overview  
This project is the first step of a semester-long assignment. The purpose is to build a simple tool for managing a basic investment portfolio. Homework 1 focuses on the ability to add stock positions and produce a summary that is easy to read. The goal is to provide a foundation that can be extended in later homework with bonds, reports, and pricing. The project was created to give students a chance to learn simple portfolio tracking concepts without the complexity of professional financial software.  

Files Included  
The document docs/SRS.MD contains the Software Requirements Specification. It explains the purpose, scope, requirements, and one use case for Homework 1. The file src/portfolio.py contains the Python code that can add a stock and return a summary. The file weekly logs/Week 01.md contains my notes describing what I planned, what I delivered, what issues I faced, and what I will do next.  

How to Run  
First, confirm that Python 3 is installed on the computer. Open a terminal in the project folder. Run the command python3 src/portfolio.py. The program will print a dictionary summary showing the total number of items, the number of stock positions, and the positions themselves. In Homework 1 the demo uses the tickers AAPL and MSFT.  

What I Completed  
I created the repository and organized the folders into 'docs', 'src', and 'weekly logs'. I wrote the first version of the SRS with a goal, functional requirements, non-functional requirements, and a use case. I created the Python file that includes the add_stock function and the make_summary function. I ran the program with two example tickers and confirmed that the output matched expectations.  

Next Steps  
I will expand the program to add support for bonds with a ticker, quantity, par value, and coupon rate. I will add a plain-text portfolio report that lists all positions in a simple format. I will expand the SRS to include more requirements and acceptance criteria. I will continue to update the weekly logs to document progress.  
