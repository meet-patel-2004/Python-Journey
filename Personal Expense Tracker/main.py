import json
import os
from datetime import datetime
from collections import defaultdict


class Expense:
    """Represents a single expense."""

    def __init__(self, expense_id, title, amount, category, date, description=""):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def update_expense(self, title, amount, category, date, description):
        """Update expense information."""
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        """Convert expense object into dictionary."""
        return {
            "expense_id": self.expense_id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }


class ExpenseTracker(Expense):
    """Manages all expenses."""

    CATEGORIES = [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment",
        "Health",
        "Education",
        "Other"
    ]

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def save_expenses(self):
        """Save expenses to JSON file."""
        try:
            data = [expense.to_dict() for expense in self.expenses]

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            print(f"Error saving expenses: {error}")

    def load_expenses(self):
        """Load expenses from JSON file."""

        if not os.path.exists(self.filename):
            self.save_expenses()
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.expenses = [
                Expense(
                    item["expense_id"],
                    item["title"],
                    item["amount"],
                    item["category"],
                    item["date"],
                    item.get("description", "")
                )
                for item in data
            ]

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Error loading expenses: {error}")
            self.expenses = []

        except OSError as error:
            print(f"Error opening file: {error}")

    def generate_id(self):
        """Generate unique expense ID."""

        if not self.expenses:
            return 1

        return max(expense.expense_id for expense in self.expenses) + 1

    def get_valid_amount(self):
        """Get a valid positive expense amount."""

        while True:
            try:
                amount = float(input("Enter amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero!")
                    continue

                return round(amount, 2)

            except ValueError:
                print("Please enter a valid numeric amount!")

    def get_valid_date(self):
        """Get a valid date from the user."""

        while True:
            date_input = input(
                "Enter date (YYYY-MM-DD) or press Enter for today: "
            ).strip()

            if not date_input:
                return datetime.today().strftime("%Y-%m-%d")

            try:
                date = datetime.strptime(date_input, "%Y-%m-%d")
                return date.strftime("%Y-%m-%d")

            except ValueError:
                print("Invalid date! Use YYYY-MM-DD format.")

    def select_category(self):
        """Display categories and allow user to select one."""

        print("\nAvailable Categories:")

        for index, category in enumerate(self.CATEGORIES, start=1):
            print(f"{index}. {category}")

        while True:
            try:
                choice = int(input("Select category number: "))

                if 1 <= choice <= len(self.CATEGORIES):
                    return self.CATEGORIES[choice - 1]

                print("Invalid category number!")

            except ValueError:
                print("Please enter a valid number!")

    def find_expense(self, expense_id):
        """Find expense using its ID."""

        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense

        return None

    def add_expense(self):
        """Add a new expense."""

        print("\n========== ADD EXPENSE ==========")

        title = input("Enter expense title: ").strip()

        if not title:
            print("Title cannot be empty!")
            return

        amount = self.get_valid_amount()
        category = self.select_category()
        date = self.get_valid_date()

        description = input("Enter description (optional): ").strip()

        expense_id = self.generate_id()

        expense = Expense(
            expense_id,
            title,
            amount,
            category,
            date,
            description
        )

        self.expenses.append(expense)
        self.save_expenses()

        print("\nExpense added successfully!")

    def view_expenses(self):
        """Display all expenses."""

        print("\n========== ALL EXPENSES ==========")

        if not self.expenses:
            print("No expenses found!")
            return

        sorted_expenses = sorted(
            self.expenses,
            key=lambda expense: (expense.date, expense.expense_id),
            reverse=True
        )

        for expense in sorted_expenses:
            print(f"\nExpense ID: {expense.expense_id}")
            print(f"Title: {expense.title}")
            print(f"Amount: ₹{expense.amount:.2f}")
            print(f"Category: {expense.category}")
            print(f"Date: {expense.date}")
            print(f"Description: {expense.description}")
            print("-" * 35)

        print(f"\nTotal Records: {len(self.expenses)}")

    def update_expense(self):
        """Update an existing expense."""

        print("\n========== UPDATE EXPENSE ==========")

        if not self.expenses:
            print("No expenses available to update!")
            return

        self.view_expenses()

        try:
            expense_id = int(input("\nEnter expense ID to update: "))

        except ValueError:
            print("Invalid expense ID!")
            return

        expense = self.find_expense(expense_id)

        if expense is None:
            print("Expense not found!")
            return

        print("\nEnter new expense details:")

        title = input("Enter new title: ").strip()

        if not title:
            print("Title cannot be empty!")
            return

        amount = self.get_valid_amount()
        category = self.select_category()
        date = self.get_valid_date()

        description = input("Enter new description: ").strip()

        expense.update_expense(
            title,
            amount,
            category,
            date,
            description
        )

        self.save_expenses()

        print("\nExpense updated successfully!")

    def delete_expense(self):
        """Delete an expense."""

        print("\n========== DELETE EXPENSE ==========")

        if not self.expenses:
            print("No expenses available to delete!")
            return

        self.view_expenses()

        try:
            expense_id = int(input("\nEnter expense ID to delete: "))

        except ValueError:
            print("Invalid expense ID!")
            return

        expense = self.find_expense(expense_id)

        if expense is None:
            print("Expense not found!")
            return

        confirmation = input(
            f"Are you sure you want to delete '{expense.title}'? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            self.expenses.remove(expense)
            self.save_expenses()
            print("Expense deleted successfully!")

        else:
            print("Deletion cancelled.")

    def search_by_category(self):
        """Search expenses by category."""

        print("\n========== SEARCH BY CATEGORY ==========")

        category = self.select_category()

        filtered_expenses = [
            expense for expense in self.expenses
            if expense.category == category
        ]

        if not filtered_expenses:
            print(f"No expenses found in {category} category!")
            return

        total = 0

        for expense in filtered_expenses:
            print(
                f"\nID: {expense.expense_id} | "
                f"Title: {expense.title} | "
                f"Amount: ₹{expense.amount:.2f} | "
                f"Date: {expense.date}"
            )

            total += expense.amount

        print("-" * 35)
        print(f"Total {category} Expenses: ₹{total:.2f}")

    def monthly_report(self):
        """Generate report for a particular month."""

        print("\n========== MONTHLY REPORT ==========")

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")

        except ValueError:
            print("Invalid month! Use YYYY-MM format.")
            return

        monthly_expenses = [
            expense for expense in self.expenses
            if expense.date.startswith(month)
        ]

        if not monthly_expenses:
            print(f"No expenses found for {month}!")
            return

        total = sum(
            expense.amount for expense in monthly_expenses
        )

        print(f"\nReport for: {month}")
        print(f"Total Transactions: {len(monthly_expenses)}")
        print(f"Total Monthly Expenses: ₹{total:.2f}")

        print("\nCategory-wise Breakdown:")

        category_totals = defaultdict(float)

        for expense in monthly_expenses:
            category_totals[expense.category] += expense.amount

        for category, amount in sorted(category_totals.items()):
            print(f"{category}: ₹{amount:.2f}")

    def total_expenses(self):
        """Calculate total expenses."""

        print("\n========== TOTAL EXPENSES ==========")

        if not self.expenses:
            print("No expenses recorded!")
            return

        total = sum(
            expense.amount for expense in self.expenses
        )

        print(f"Total Transactions: {len(self.expenses)}")
        print(f"Total Money Spent: ₹{total:.2f}")

    def category_report(self):
        """Generate category-wise expense report."""

        print("\n========== CATEGORY REPORT ==========")

        if not self.expenses:
            print("No expenses recorded!")
            return

        category_totals = defaultdict(float)

        for expense in self.expenses:
            category_totals[expense.category] += expense.amount

        for category in sorted(category_totals):
            print(
                f"{category}: ₹{category_totals[category]:.2f}"
            )

        print("-" * 35)

        total = sum(category_totals.values())

        print(f"Grand Total: ₹{total:.2f}")


def display_menu():
    """Display main menu."""

    print("\n" + "=" * 40)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 40)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses by Category")
    print("6. Monthly Expense Report")
    print("7. Total Expenses")
    print("8. Category-wise Report")
    print("9. Exit")

    print("=" * 40)


def main():
    tracker = ExpenseTracker()

    while True:

        display_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.update_expense()

        elif choice == "4":
            tracker.delete_expense()

        elif choice == "5":
            tracker.search_by_category()

        elif choice == "6":
            tracker.monthly_report()

        elif choice == "7":
            tracker.total_expenses()

        elif choice == "8":
            tracker.category_report()

        elif choice == "9":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select between 1 and 9.")


if __name__ == "__main__":
    main()