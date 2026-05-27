import csv
import os

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer= csv.writer(file)
            writer.writerow(["Category", "Amount", "Description"])

def add_expenses(category, amount, Description):
    with open(FILE_NAME, "a", newline="") as file:
        writer= csv.writer(file)
        writer.writerow([category, amount, Description])

def get_expenses():
    expenses=[]
    with open(FILE_NAME, newline="") as file:
        reader= csv.DictReader(file)

        for row in reader:
            expenses.append(
                {
                    "category": row["Category"],
                    "amount": float(row["Amount"]),
                    "description": row["Description"]

                }
            )
    return expenses

def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

def category_summary(expenses):
    summary={}
    for expense in expenses:
        category= expense["category"]

        if category not in summary:
            summary[category]=0

        summary[category] += expense["amount"]

    return summary

def budget_exceeded(total, budget):
    return total>budget

def display_expenses():
    expenses= get_expenses()

    if not expenses:
        print("No expenses found.")
        return
    print("\nExpenses")
    print("-" * 50)

    for expense in expenses:
        print(
            f"{expense['category']:15}"
            f"{expense['amount']:8.2f}        "
            f"{expense['description']}"
        )

def main():
   initialize_file()

   while True:
       print("\n====SMART EXPENSE TRACKER======")
       print("1. Add Expense")
       print("2. View Expenses")
       print("3. Show Total Spendings")
       print("4. Category Summary")
       print("5. Check Budget")
       print("6. Exit")

       choice= input("choose an option: ").strip()

       if choice=="1":
           category= input("Category: ")
           amount= float(input("Amount: "))
           Description= input("Description: ")

           add_expenses(category, amount, Description)
           print("Expense added successfully")

       elif choice=="2":
           display_expenses()

       elif choice== "3":
           expenses= get_expenses()
           total=  calculate_total(expenses)
           print(f"Total Spendings: ₹{total: .2f}")

       elif choice=="4":
           expenses= get_expenses()

           summary= category_summary(expenses)

           print("\nCategory Summary")

           for category, amount in summary.items():
               print(f"{category}: ₹{amount:.2f}")

       elif choice=="5":
           budget= float(input("Enter Budget: "))

           expenses= get_expenses()
           total= calculate_total(expenses)

           if budget_exceeded(total,budget):
               print(
                   f"Warning! Budget exceeded by"
                   f"₹{total-budget:.2f}"
               )
           else:
            print(
                f"Within Budget"
                f"₹{budget-total:.2f} remaining. "
            )
       elif choice=="6":
           print("Goodbyee")
           break

       else:
           print("Invalid choice.")

if __name__== "__main__":
    main()
