To-Do List Application 

A simple command-line To-Do List application built using Core Python and Object-Oriented Programming (OOP).

This project allows users to manage their daily tasks by adding, viewing, updating, deleting, and completing tasks. It uses JSON for persistent data storage, so tasks remain saved even after the application is closed.

🚀 Features

- Add Tasks: Create new tasks with a title and description.
- View All Tasks: Display all saved tasks with their details and status.
- Update Tasks: Modify the title and description of existing tasks.
- Delete Tasks: Remove tasks from the list.
- Complete Tasks: Mark pending tasks as completed.
- View Pending Tasks: Display only unfinished tasks.
- Persistent Storage: Automatically save and load tasks using a JSON file.
- Unique Task IDs: Assign a unique ID to every task.
- Error Handling: Handle invalid inputs and common file errors.

🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling
- Lists and Dictionaries

External Dependencies: None. This project uses only Python's built-in modules.

📂 Project Structure

todo_app/
│
├── main.py
├── tasks.json
└── README.md

File| Description
"main.py"| Contains the complete application logic.
"tasks.json"| Stores task data in JSON format.
"README.md"| Project documentation.

Note: "tasks.json" is automatically created when the application runs if it doesn't already exist.

⚙️ Installation and Setup

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Navigate to the project directory

cd todo_app

3. Run the application

python main.py

Make sure Python 3 is installed on your computer.

💻 Application Menu

After running the application, you will see the following menu:

===================================
       TO-DO LIST APPLICATION
===================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task as Completed
6. View Pending Tasks
7. Exit
===================================
Enter your choice (1-7):

Select an option by entering its corresponding number.

📸 Example Usage

Adding a Task:

--- Add New Task ---
Enter task title: Learn Python
Enter task description: Practice OOP concepts

Task added successfully!

Stored Data (tasks.json):

[
    {
        "task_id": 1,
        "title": "Learn Python",
        "description": "Practice OOP concepts",
        "completed": false
    }
]

🧠 Concepts Learned

This project helped me practice and understand:

- Classes and Objects
- Constructors ("_init_")
- Object-Oriented Programming
- Methods and Encapsulation
- Lists and Dictionaries
- List Comprehensions
- JSON Serialization and Deserialization
- File Handling
- Exception Handling
- CRUD Operations (Create, Read, Update, Delete)

🔮 Future Improvements

Some features I plan to add in future versions:

- Add task priorities (Low, Medium, High).
- Add task deadlines and due dates.
- Search tasks by title.
- Add task categories.
- Display completed tasks separately.
- Add task statistics.
- Improve the user interface.

👨‍💻 Author

Meet Patel