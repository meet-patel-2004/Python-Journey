import json
import os


class Task:
    """Represents a single task."""

    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def update_task(self, title, description):
        self.title = title
        self.description = description

    def to_dict(self):
        """Convert Task object into dictionary."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }


class TodoList(Task):
    """Manages all tasks."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            data = [task.to_dict() for task in self.tasks]

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            print(f"Error saving tasks: {error}")

    def load_tasks(self):
        """Load tasks from JSON file."""
        if not os.path.exists(self.filename):
            self.save_tasks()
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.tasks = [
                Task(
                    item["task_id"],
                    item["title"],
                    item["description"],
                    item["completed"]
                )
                for item in data
            ]

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"Error loading tasks: {error}")
            self.tasks = []

        except OSError as error:
            print(f"Error opening file: {error}")

    def generate_id(self):
        """Generate a unique task ID."""
        if not self.tasks:
            return 1

        return max(task.task_id for task in self.tasks) + 1

    def add_task(self):
        """Add a new task."""
        print("\n--- Add New Task ---")

        title = input("Enter task title: ").strip()

        if not title:
            print("Task title cannot be empty!")
            return

        description = input("Enter task description: ").strip()

        task_id = self.generate_id()

        task = Task(task_id, title, description)

        self.tasks.append(task)
        self.save_tasks()

        print("Task added successfully!")

    def view_tasks(self):
        """Display all tasks."""
        print("\n--- All Tasks ---")

        if not self.tasks:
            print("No tasks found!")
            return

        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"

            print(f"\nTask ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {status}")
            print("-" * 30)

    def update_task(self):
        """Update an existing task."""
        print("\n--- Update Task ---")

        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_id = int(input("Enter task ID to update: "))

        except ValueError:
            print("Please enter a valid numeric ID!")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task not found!")
            return

        title = input("Enter new title: ").strip()

        if not title:
            print("Title cannot be empty!")
            return

        description = input("Enter new description: ").strip()

        task.update_task(title, description)
        self.save_tasks()

        print("Task updated successfully!")

    def delete_task(self):
        """Delete an existing task."""
        print("\n--- Delete Task ---")

        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_id = int(input("Enter task ID to delete: "))

        except ValueError:
            print("Please enter a valid numeric ID!")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task not found!")
            return

        self.tasks.remove(task)
        self.save_tasks()

        print("Task deleted successfully!")

    def complete_task(self):
        """Mark a task as completed."""
        print("\n--- Complete Task ---")

        self.view_tasks()

        if not self.tasks:
            return

        try:
            task_id = int(input("Enter task ID to complete: "))

        except ValueError:
            print("Please enter a valid numeric ID!")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task not found!")
            return

        if task.completed:
            print("This task is already completed!")
            return

        task.mark_completed()
        self.save_tasks()

        print("Task marked as completed!")

    def view_pending_tasks(self):
        """Display only pending tasks."""
        print("\n--- Pending Tasks ---")

        pending_tasks = [
            task for task in self.tasks
            if not task.completed
        ]

        if not pending_tasks:
            print("No pending tasks!")
            return

        for task in pending_tasks:
            print(f"\nTask ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print("Status: Pending")
            print("-" * 30)

    def find_task(self, task_id):
        """Find a task using its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task

        return None


def display_menu():
    """Display the application menu."""

    print("\n" + "=" * 35)
    print("       TO-DO LIST APPLICATION")
    print("=" * 35)

    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. View Pending Tasks")
    print("7. Exit")

    print("=" * 35)


def main():
    todo = TodoList()

    while True:

        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            todo.add_task()

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.update_task()

        elif choice == "4":
            todo.delete_task()

        elif choice == "5":
            todo.complete_task()

        elif choice == "6":
            todo.view_pending_tasks()

        elif choice == "7":
            print("\nThank you for using To-Do List!")
            break

        else:
            print("Invalid choice! Please select between 1 and 7.")


if __name__ == "__main__":
    main()