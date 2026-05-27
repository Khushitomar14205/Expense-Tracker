# SMART EXPENSE TRACKER

#### Video demo:

#### Description:
Smart Expense Tracker is a python command-line application that helps users manage their expenses efficiently.
Users can:
- Add expenses
- View all expenses
- Calculate total spendings
- View category-wise spendings summaries
- Check whether they have exceeded budget or not

Expense data is stored in a CSV file so that records persist between program executions.

#### Features:

### Add Expenses
Users can record expenses by entering:
- Category
- Amount
- Description

### View Expenses
Display all saved expenses.

### Total Spending
Calculate total money spent.

### Category Summary
Groups expenses by category and show totals.

### Budget Check
Allow users to compare spending against a budget and receive warnings if exceeded.

#### Files:
- project.py
- test_project.py
- requirements.txt
- expenses.csv

#### Running:
python project.py

#### Testing:
pytest test_project.py

#### Design Choices:
CSV files were chosen because they are simple, lightweight, and suitable for small personal finance records.
Functions were seperated to improve maintanibility and allow unit testing with pytest.
The program usea a menu-driven interface to make navigation straightforward for users.


