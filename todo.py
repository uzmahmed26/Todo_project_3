#!/usr/bin/env python3
"""
Todo In-Memory Python Console Application

A simple command-line todo list manager that stores tasks in memory.
Tasks are lost when the application exits (no persistent storage).

Features:
- Add new tasks
- View all tasks
- Delete tasks by number
- Exit application

Usage:
    python todo.py
"""

# Global task list (FR-002: Must use variable name 'todos')
todos = []


def show_menu():
    """Display the main menu and return user's validated choice.

    Returns:
        int: User's menu choice (1-4)
    """
    print("\n=== Todo List Menu ===")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


def add_task():
    """Prompt for and add a new task to the todos list.

    Implements FR-006: Exact prompts and confirmation message.
    """
    task = input("Enter new task: ")
    todos.append(task)
    print("Task added!")


def view_tasks():
    """Display all tasks with 1-based numbering, or message if empty.

    Implements FR-007 (empty list message) and FR-008 (enumerate with start=1).
    """
    if len(todos) == 0:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")


def delete_task():
    """Display tasks, prompt for number, and delete if valid.

    Implements FR-009 through FR-012: Show tasks first, prompt for number,
    use pop(index-1), display "Invalid number!" for errors.
    """
    view_tasks()  # FR-009: Must show tasks first

    if len(todos) == 0:
        return  # Nothing to delete

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todos):
            todos.pop(num - 1)  # FR-011: Must use pop(index - 1)
        else:
            print("Invalid number!")  # FR-012
    except ValueError:
        print("Invalid number!")  # FR-012


def main():
    """Main application loop.

    Implements FR-005: Continuous menu loop until user exits.
    """
    while True:
        choice = show_menu()

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Goodbye!")
            break  # Exit application


if __name__ == "__main__":
    main()
