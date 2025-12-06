#!/usr/bin/env python3
"""
Automated tests for todo.py

Tests the core functionality without manual interaction.
"""

import sys
import io
from contextlib import redirect_stdout
from unittest.mock import patch

# Import the todo module
import todo


def test_add_task():
    """Test adding tasks to the list."""
    print("TEST: Add task functionality")

    # Reset todos
    todo.todos.clear()

    # Simulate adding a task
    with patch('builtins.input', return_value="Buy groceries"):
        output = io.StringIO()
        with redirect_stdout(output):
            todo.add_task()
        result = output.getvalue()

    assert len(todo.todos) == 1, "Task list should have 1 item"
    assert todo.todos[0] == "Buy groceries", "Task should be 'Buy groceries'"
    assert "Task added!" in result, "Should show confirmation message"
    print("  PASS Add task test passed")


def test_view_tasks_empty():
    """Test viewing empty task list."""
    print("TEST: View empty tasks")

    # Reset todos
    todo.todos.clear()

    output = io.StringIO()
    with redirect_stdout(output):
        todo.view_tasks()
    result = output.getvalue()

    assert "No tasks yet!" in result, "Should show 'No tasks yet!' for empty list"
    print("  PASS View empty tasks test passed")


def test_view_tasks_with_items():
    """Test viewing tasks with items."""
    print("TEST: View tasks with items")

    # Setup
    todo.todos.clear()
    todo.todos.extend(["Task 1", "Task 2", "Task 3"])

    output = io.StringIO()
    with redirect_stdout(output):
        todo.view_tasks()
    result = output.getvalue()

    assert "Your Tasks:" in result, "Should show 'Your Tasks:' header"
    assert "1. Task 1" in result, "Should show task 1 with correct numbering"
    assert "2. Task 2" in result, "Should show task 2 with correct numbering"
    assert "3. Task 3" in result, "Should show task 3 with correct numbering"
    print("  PASS View tasks with items test passed")


def test_delete_task_valid():
    """Test deleting a valid task."""
    print("TEST: Delete valid task")

    # Setup
    todo.todos.clear()
    todo.todos.extend(["Task 1", "Task 2", "Task 3"])

    # Delete task 2
    with patch('builtins.input', return_value="2"):
        output = io.StringIO()
        with redirect_stdout(output):
            todo.delete_task()

    assert len(todo.todos) == 2, "Should have 2 tasks remaining"
    assert "Task 2" not in todo.todos, "Task 2 should be deleted"
    assert todo.todos == ["Task 1", "Task 3"], "Remaining tasks should be correct"
    print("  PASS Delete valid task test passed")


def test_delete_task_invalid_number():
    """Test deleting with invalid number."""
    print("TEST: Delete with invalid number")

    # Setup
    todo.todos.clear()
    todo.todos.extend(["Task 1", "Task 2"])

    # Try to delete task 5 (out of range)
    with patch('builtins.input', return_value="5"):
        output = io.StringIO()
        with redirect_stdout(output):
            todo.delete_task()
        result = output.getvalue()

    assert len(todo.todos) == 2, "No tasks should be deleted"
    assert "Invalid number!" in result, "Should show 'Invalid number!' message"
    print("  PASS Delete invalid number test passed")


def test_delete_task_non_numeric():
    """Test deleting with non-numeric input."""
    print("TEST: Delete with non-numeric input")

    # Setup
    todo.todos.clear()
    todo.todos.extend(["Task 1", "Task 2"])

    # Try to delete with text
    with patch('builtins.input', return_value="abc"):
        output = io.StringIO()
        with redirect_stdout(output):
            todo.delete_task()
        result = output.getvalue()

    assert len(todo.todos) == 2, "No tasks should be deleted"
    assert "Invalid number!" in result, "Should show 'Invalid number!' message"
    print("  PASS Delete non-numeric test passed")


def test_menu_validation():
    """Test menu input validation."""
    print("TEST: Menu input validation")

    # Test valid input
    with patch('builtins.input', return_value="1"):
        output = io.StringIO()
        with redirect_stdout(output):
            choice = todo.show_menu()

    assert choice == 1, "Should return choice 1"
    print("  PASS Menu validation test passed")


def test_empty_task():
    """Test adding empty task."""
    print("TEST: Add empty task")

    # Reset todos
    todo.todos.clear()

    # Add empty task
    with patch('builtins.input', return_value=""):
        output = io.StringIO()
        with redirect_stdout(output):
            todo.add_task()

    assert len(todo.todos) == 1, "Empty task should be added"
    assert todo.todos[0] == "", "Task should be empty string"
    print("  PASS Empty task test passed")


def run_all_tests():
    """Run all tests and report results."""
    print("\n" + "="*50)
    print("Running Automated Tests for todo.py")
    print("="*50 + "\n")

    tests = [
        test_add_task,
        test_view_tasks_empty,
        test_view_tasks_with_items,
        test_delete_task_valid,
        test_delete_task_invalid_number,
        test_delete_task_non_numeric,
        test_menu_validation,
        test_empty_task,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  FAIL FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  FAIL ERROR: {e}")
            failed += 1

    print("\n" + "="*50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*50 + "\n")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
