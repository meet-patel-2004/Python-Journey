Personal Expense Tracker 💰

A command-line Personal Expense Tracker built using Core Python and Object-Oriented Programming (OOP).

This application helps users record and manage their daily expenses. Users can add, view, update, delete, and categorize expenses. It also generates monthly expense reports and category-wise spending summaries.

The application uses JSON for persistent data storage, allowing expense records to remain saved even after the program is closed.

🚀 Features

- Add Expenses: Record expenses with a title, amount, category, date, and description.
- View All Expenses: Display all recorded expenses.
- Update Expenses: Modify existing expense details.
- Delete Expenses: Remove unwanted expense records.
- Search by Category: Filter expenses based on categories.
- Monthly Expense Report: Calculate total spending for a selected month.
- Total Expenses: Calculate the total amount spent.
- Category-wise Report: Display spending across different categories.
- Date Validation: Validate expense dates using Python's datetime module.
- Input Validation: Handle invalid amounts, dates, and menu selections.
- Persistent Storage: Automatically save and load expense records using JSON.

🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling
- Datetime Module
- Collections Module ("defaultdict")

External Dependencies: None. This project uses only Python's built-in modules.

📂 Project Structure

expense_tracker/
│
├── main.py
├── expenses.json
└── README.md

File| Description
"main.py"| Contains the complete application logic.
"expenses.json"| Stores expense records in JSON format.
"README.md"| Project documentation.

Note: "expenses.json" is automatically created when the application runs if it doesn't already exist.

⚙️ Installation and Setup

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Navigate to the project directory

cd expense_tracker

3. Run the application

python main.py

Make sure Python 3 is installed on your computer.

💻 Application Menu

After running the application, you will see the following menu:

========================================
       PERSONAL EXPENSE TRACKER
========================================
1. Add Expense
2. View All Expenses
3. Update Expense
4. Delete Expense
5. Search Expenses by Category
6. Monthly Expense Report
7. Total Expenses
8. Category-wise Report
9. Exit
========================================
Enter your choice (1-9):

Select an option by entering its corresponding number.

📸 Example Usage

Adding an Expense:

========== ADD EXPENSE ==========

Enter expense title: Lunch
Enter amount: ₹150

Available Categories:
1. Food
2. Travel
3. Shopping
4. Bills
5. Entertainment
6. Health
7. Education
8. Other

Select category number: 1

Enter date (YYYY-MM-DD) or press Enter for today:

Enter description (optional): Lunch with friends

Expense added successfully!

Stored Data (expenses.json):

[
    {
        "expense_id": 1,
        "title": "Lunch",
        "amount": 150.0,
        "category": "Food",
        "date": "2026-11-05",
        "description": "Lunch with friends"
    }
]

📊 Available Expense Categories

The application currently supports the following categories:

- Food
- Travel
- Shopping
- Bills
- Entertainment
- Health
- Education
- Other

🧠 Concepts Learned

This project helped me practice and understand:

- Classes and Objects
- Constructors ("_init_")
- Object-Oriented Programming
- Encapsulation
- Methods and Functions
- Lists and Dictionaries
- List Comprehensions
- Lambda Functions
- JSON Serialization and Deserialization
- File Handling
- Exception Handling
- Datetime Module
- Collections ("defaultdict")
- CRUD Operations
- Data Filtering and Calculations

🔮 Future Improvements

Some features I plan to add in future versions:

- Add income tracking.
- Calculate remaining balance.
- Set monthly spending limits.
- Create category-wise budgets.
- Search expenses by date range.
- Export expense records to CSV.
- Add sorting by date and amount.
- Display highest, lowest, and average expenses.
- Replace JSON storage with SQLite.
- Add graphical reports and charts.

👨‍💻 Author

Meet Patel