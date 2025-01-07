import os
import csv
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Initialize the file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])  # Header


# Add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    description = input("Enter a description (optional): ")
    amount = input("Enter the amount: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")


# View expenses
def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Delete an expense
def delete_expense():
    view_expenses()
    expense_to_delete = input("Enter the line number of the expense to delete: ")

    with open(FILE_NAME, mode="r") as file:
        lines = list(csv.reader(file))

    if 0 < int(expense_to_delete) <= len(lines):
        del lines[int(expense_to_delete) - 1]
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        print("Expense deleted successfully!")
    else:
        print("Invalid line number!")


# Show summary
def show_summary():
    totals = {}
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[3])
            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    print("Expense Summary:")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")


# Main menu
def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main_menu()
