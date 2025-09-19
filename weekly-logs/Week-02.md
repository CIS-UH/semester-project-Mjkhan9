Week 2 Notes Homework 2
Name: Mohammad Khan
ID: 2245764
Date: 09/18/25

Homework 2: Step 1 - Assumptions and Estimation Approach

The project is titled "Investment Portfolio Application." The program will run on a local machine with Python 3 installed. No external libraries or APIs will be used for this assignment. The estimation method relies on person-hours, with a contingency of twenty-five percent allocated for tasks that are new to me. Durations are segmented into two-hour blocks on weekdays.

Homework 2: Step 2 - Work Breakdown Structure

The initiation and requirements phase includes reviewing the slides and instructions, collecting and refining user stories, and defining the project scope and constraints.

The design phase entails creating the data model for positions and defining the function interfaces.

The implementation phase involves coding the functionalities to add stocks, add bonds, generate summaries, create text reports, and writing a demo in the main function.

The validation and testing phase consists of running manual tests for both valid and invalid inputs, as well as saving a sample run with the output.

The documentation phase requires updating the README with the run steps, revising the Software Requirements Specification (SRS) with functional and non-functional requirements, and updating the Week 1 log.

The project management phase includes tracking the schedule, making necessary adjustments, and packaging the project for submission.

Homework 2: Step 3 - Activity List with Estimated Hours

- Reviewing slides and assignment: 3 hours
- Finalizing user stories and acceptance criteria: 3 hours
- Writing scope and constraints: 1 hour
- Designing the data model: 1 hour
- Planning function signatures: 1 hour
- Coding the "add stock" function: 1 hour
- Coding the "add bond" function: 1.5 hours
- Coding the "make summary" function: 1 hour
- Coding the "make text report" function: 1 hour
- Writing the demo: 0.5 hours
- Running tests for valid inputs: 1 hour
- Running tests for invalid inputs: 1 hour
- Saving a sample run and output: 0.5 hours
- Updating the README: 1 hour
- Updating the SRS: 1 hour
- Updating the Week 1 notes: 0.5 hours
- Checking the schedule and buffer: 1 hour
- Packaging the final submission: 0.5 hours

The total estimated effort is 19.5 hours.
- A2 depends on A1  
- A3 depends on A1  
- A4 depends on A2 and A3  
- A5 depends on A4  
- A6 depends on A5  
- A7 depends on A5  
- A8 depends on A6 and A7  
- A9 depends on A8  
- A10 depends on A6 through A9  
- A11 depends on A10  
- A12 depends on A10  
- A13 depends on A11 and A12  
- A14 depends on A10 through A13  
- A15 depends on A2, A3, and A8  
- A16 depends on A14 and A15  
- A17 depends on A10 through A16  
- A18 depends on A17
Homework 2: Step 5 - Milestones

- Requirements are approved after the user stories and scope are complete.
- Core functions are completed after the text report is coded.
- The demo is complete once the program runs with example data.
- Testing is complete after running both valid and invalid inputs.
- Documentation is complete after updating the README, SRS, and weekly log.
- The project is ready for submission after packaging is complete.

Homework 2: Step 6 - Schedule by Day

The timeline Gantt chart screenshot can be found here - weekly_logs.timeline_gantt.png - In the weekly folder!

Homework 2: Step 7 - Risk Register

1. Risk: Underestimating coding time, which may lead to incomplete functions.  
   Response: Utilize the buffer and reduce optional formatting.

2. Risk: Confusion with acceptance tests, potentially leading to rework.  
   Response: Review user stories with class notes before beginning coding.

3. Risk: Version issues with Python, which may cause delays.  
   Response: Test on lab machines and avoid using external packages.

4. Risk: Last-minute errors, which could diminish submission quality.  
   Response: Aim to finish one day early and use the buffer to rectify any errors.

Homework 2: Step 8 - Sample Code Snippets

- The "add stock" function verifies that the ticker is not empty and that the quantity is positive, storing the position with the ticker in uppercase and the quantity as a float.
- The "add bond" function checks that the ticker is not empty, that both the quantity and par value are positive, and that the coupon is non-negative, storing the position with numeric fields as floats.
- The "make summary" function counts the total number of items, stocks, and bonds, returning these counts along with the positions.
- The "make text report" function prints a header followed by a list of holdings or prints "empty" if the portfolio has no positions.
- The demo script adds two stocks and one bond, then prints the summary and the text report.

Homework 2: Step 9 - Submission Checklist

My name is Mohammad Khan, and my ID (2245764) is included at the top of the documents. The SRS has been updated with requirements and user stories, the README contains run steps, and the Week 1 notes reflect what was delivered. The program runs in Python 3 and prints both a summary and a report. The timeline Gantt chart screenshot is saved as `weekly_logs/timeline_gantt.png` and is included in this document.
