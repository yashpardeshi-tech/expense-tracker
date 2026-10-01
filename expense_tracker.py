import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount (₹): "))

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("\n✅ Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n========== EXPENSES ==========")

        found = False

        for row in reader:
            found = True
            print(
                f"{row['Date']} | "
                f"{row['Category']} | "
                f"{row['Description']} | "
                f"₹{row['Amount']}"
            )

        if not found:
            print("No expenses found.")


def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\n💰 Total Expenses: ₹{total:.2f}")


def category_summary():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n====== CATEGORY SUMMARY ======")

    if not categories:
        print("No expenses found.")
        return

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    initialize_file()

    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker! 👋")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()