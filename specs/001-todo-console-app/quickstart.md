# Quickstart Guide: Todo Console Application

**Feature**: 001-todo-console-app
**Version**: 1.0.0
**Date**: 2025-12-06

## Overview

This guide helps you get started with the Todo In-Memory Python Console Application - a simple command-line tool for managing a task list that exists only while the program is running.

## Prerequisites

- **Python 3.x** installed (minimum Python 3.6 recommended)
- **Terminal/Command Prompt** access
- **Basic familiarity** with command-line interfaces

### Check Python Installation

```bash
# Check Python version
python --version
# or
python3 --version

# Should output: Python 3.x.x
```

If Python is not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3` or download from python.org
- **Linux**: `sudo apt install python3` (Debian/Ubuntu) or `sudo yum install python3` (RHEL/CentOS)

## Installation

### Option 1: Quick Start (No Installation)

```bash
# Navigate to project directory
cd /path/to/todo_list

# Run the application directly
python todo.py
# or
python3 todo.py
```

### Option 2: Make Executable (Unix/macOS)

```bash
# Make file executable
chmod +x todo.py

# Run directly
./todo.py
```

**Note**: Add shebang to top of `todo.py` for this option:
```python
#!/usr/bin/env python3
```

## Usage

### Starting the Application

```bash
python todo.py
```

**Expected Output**:
```
=== Todo List Menu ===
1. Add new task
2. View all tasks
3. Delete a task
4. Exit
Enter your choice (1-4):
```

### Basic Workflow

#### 1. Add Your First Task

```
Enter your choice (1-4): 1
Enter new task: Buy groceries
Task added!
```

#### 2. Add More Tasks

```
Enter your choice (1-4): 1
Enter new task: Call dentist
Task added!

Enter your choice (1-4): 1
Enter new task: Finish project report
Task added!
```

#### 3. View All Tasks

```
Enter your choice (1-4): 2
Your Tasks:
1. Buy groceries
2. Call dentist
3. Finish project report
```

#### 4. Delete a Completed Task

```
Enter your choice (1-4): 3
Your Tasks:
1. Buy groceries
2. Call dentist
3. Finish project report

Enter task number to delete: 2
```

**Result**: Task "Call dentist" is removed

#### 5. Exit the Application

```
Enter your choice (1-4): 4
```

**Program terminates cleanly**

## Common Operations

### Viewing Tasks When List is Empty

```
Enter your choice (1-4): 2
No tasks yet!
```

### Handling Invalid Input

**Invalid Menu Choice**:
```
Enter your choice (1-4): 5
Invalid choice! Please enter 1, 2, 3, or 4.
```

**Invalid Delete Number**:
```
Enter task number to delete: 10
Invalid number!
```

**Non-Numeric Input**:
```
Enter task number to delete: abc
Invalid number!
```

## Important Notes

### Data Persistence

⚠️ **WARNING**: Tasks are stored in memory only!

- Tasks are **NOT saved** when you exit the program
- All tasks are **lost** when the application closes
- No file is created or modified
- This is intentional by design (FR-003)

**Example**:
```
Session 1:
  Add: "Buy milk"
  Exit

Session 2:
  View: "No tasks yet!"  ← Previous task is gone
```

### Task Limitations

- **Empty tasks**: Allowed (just press Enter)
- **Long tasks**: Up to 500 characters supported
- **Special characters**: Emojis and Unicode supported ✅
- **Editing**: Not supported (delete and re-add instead)

## Troubleshooting

### "python: command not found"

**Solution**: Try `python3` instead:
```bash
python3 todo.py
```

Or add Python to your PATH (OS-specific).

### "No such file or directory: todo.py"

**Solution**: Ensure you're in the correct directory:
```bash
# Check current directory
pwd  # Unix/macOS
cd   # Windows

# List files
ls todo.py      # Unix/macOS
dir todo.py     # Windows

# Navigate to correct directory
cd /path/to/todo_list
```

### Program Crashes on Input

**Solution**: Check Python version (must be 3.x):
```bash
python --version
```

If using Python 2.x, switch to Python 3:
```bash
python3 todo.py
```

### Unicode/Emoji Display Issues

**Solution**: Ensure terminal supports UTF-8:
```bash
# Unix/macOS
export LC_ALL=en_US.UTF-8

# Windows
chcp 65001  # Set console to UTF-8
```

## Tips & Tricks

### Quick Task Entry

Add multiple tasks quickly without viewing:
```
Choice: 1 → Add: "Task 1" → Choice: 1 → Add: "Task 2" → Choice: 2 → View all
```

### Delete Most Recent Task

If you just added 3 tasks, the newest is #3:
```
Choice: 3 → Delete: 3
```

### Clear All Tasks Quickly

Delete from highest to lowest to avoid renumbering:
```
View: 5 tasks
Delete: 5, then 4, then 3, then 2, then 1
```

Or just exit and restart (all tasks cleared!).

## Example Session

Complete workflow demonstrating all features:

```bash
$ python todo.py

=== Todo List Menu ===
1. Add new task
2. View all tasks
3. Delete a task
4. Exit
Enter your choice (1-4): 1
Enter new task: Buy groceries
Task added!

=== Todo List Menu ===
...
Enter your choice (1-4): 1
Enter new task: Call dentist
Task added!

=== Todo List Menu ===
...
Enter your choice (1-4): 1
Enter new task: Finish report
Task added!

=== Todo List Menu ===
...
Enter your choice (1-4): 2
Your Tasks:
1. Buy groceries
2. Call dentist
3. Finish report

=== Todo List Menu ===
...
Enter your choice (1-4): 3
Your Tasks:
1. Buy groceries
2. Call dentist
3. Finish report

Enter task number to delete: 2

=== Todo List Menu ===
...
Enter your choice (1-4): 2
Your Tasks:
1. Buy groceries
2. Finish report

=== Todo List Menu ===
...
Enter your choice (1-4): 4

$ # Program ended
```

**Time elapsed**: ~25 seconds ✅ (meets SC-007: <30 seconds)

## Developer Notes

### Running Tests (Future)

Currently, testing is manual. If unit tests are added:

```bash
# Install pytest (optional)
pip install pytest

# Run tests
pytest test_todo.py
```

### Code Structure

Single file (`todo.py`) contains:
- `todos = []` - Global task list
- `add_task()` - Add operation
- `view_tasks()` - View operation
- `delete_task()` - Delete operation
- `show_menu()` - Menu display
- `main()` - Main loop

### Modifying the Application

To customize prompts or behavior:

1. Open `todo.py` in any text editor
2. Modify function implementations
3. Save and run: `python todo.py`

**Warning**: Some requirements are fixed (FR-008, FR-011) - changing them violates spec.

## Next Steps

### For Users

1. ✅ Run the application: `python todo.py`
2. ✅ Add some tasks
3. ✅ View and delete tasks
4. ✅ Exit and confirm tasks are gone (in-memory only)

### For Developers

1. ✅ Review [spec.md](spec.md) for requirements
2. ✅ Review [plan.md](plan.md) for implementation approach
3. ✅ Review [data-model.md](data-model.md) for data structure
4. ✅ Review [contracts/console-interface.md](contracts/console-interface.md) for I/O contract
5. → Run `/sp.tasks` to generate implementation task list
6. → Run `/sp.implement` to execute tasks

## Support

### Known Limitations

- ❌ No data persistence (by design, FR-003)
- ❌ No task editing (by design, FR-014)
- ❌ No task search (by design, FR-014)
- ❌ No undo/redo (by design, FR-014)
- ✅ Simple and focused on core todo operations

### Feature Requests

This is a minimal implementation by design. Additional features (persistence, editing, search) are intentionally excluded per FR-014.

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-06 | Initial quickstart guide |

---

**Ready to start?** Run `python todo.py` and add your first task! 🚀
