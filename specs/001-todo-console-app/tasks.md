# Implementation Tasks: Todo In-Memory Python Console Application

**Branch**: `001-todo-console-app`
**Date**: 2025-12-06
**Status**: Ready for Implementation

## Task Execution Plan

### Phase 1: Setup
- [x] **TASK-001**: Create project structure and todo.py file
- [x] **TASK-002**: Set up .gitignore for Python project

### Phase 2: Core Implementation
- [x] **TASK-003**: Implement global todos list and helper functions structure
- [x] **TASK-004**: Implement show_menu() function (FR-004, FR-015)
- [x] **TASK-005**: Implement add_task() function (FR-006)
- [x] **TASK-006**: Implement view_tasks() function (FR-007, FR-008)
- [x] **TASK-007**: Implement delete_task() function (FR-009, FR-010, FR-011, FR-012)
- [x] **TASK-008**: Implement main() function with menu loop (FR-002, FR-005)
- [x] **TASK-009**: Add error handling for invalid inputs (FR-013)

### Phase 3: Testing & Validation
- [x] **TASK-010**: Manual testing - Add and view tasks (User Story 1 acceptance scenarios)
- [x] **TASK-011**: Manual testing - Delete tasks (User Story 2 acceptance scenarios)
- [x] **TASK-012**: Manual testing - Exit application (User Story 3 acceptance scenarios)
- [x] **TASK-013**: Manual testing - Edge cases and error handling
- [x] **TASK-014**: Verify all success criteria (SC-001 through SC-007)

---

## Detailed Task Specifications

### TASK-001: Create project structure and todo.py file

**Description**: Initialize the Python file at repository root

**Actions**:
- Create `todo.py` at repository root
- Add Python shebang: `#!/usr/bin/env python3`
- Add module docstring explaining the application

**Files Created**: `todo.py`

**Acceptance Criteria**:
- File exists at correct location (repository root)
- File is executable (chmod +x on Unix/macOS)
- Docstring describes the application purpose

---

### TASK-002: Set up .gitignore for Python project

**Description**: Create .gitignore to exclude Python artifacts

**Actions**:
- Create/update `.gitignore` with Python patterns
- Include: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `*.egg-info/`, `.env*`
- Include universal patterns: `.DS_Store`, `*.swp`, `.vscode/`, `.idea/`

**Files Created/Modified**: `.gitignore`

**Acceptance Criteria**:
- .gitignore exists and contains Python patterns
- Covers common Python development artifacts

---

### TASK-003: Implement global todos list and helper functions structure

**Description**: Set up the global state and function scaffolding

**Actions**:
- Declare `todos = []` at module level (FR-002)
- Create function signatures for: `show_menu()`, `add_task()`, `view_tasks()`, `delete_task()`, `main()`
- Add docstrings for each function

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- `todos` list declared at module level
- All 5 functions defined with proper signatures
- Docstrings explain each function's purpose

---

### TASK-004: Implement show_menu() function

**Description**: Display menu and get user choice (FR-004, FR-015)

**Implementation**:
```python
def show_menu():
    """Display the main menu and return user's validated choice."""
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
```

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- Menu options displayed in exact order (FR-015): Add (1), View (2), Delete (3), Exit (4)
- Input validated for range 1-4
- Error handling for non-numeric input (FR-013)
- Re-prompts on invalid input

---

### TASK-005: Implement add_task() function

**Description**: Add new task to the list (FR-006)

**Implementation**:
```python
def add_task():
    """Prompt for and add a new task to the todos list."""
    task = input("Enter new task: ")
    todos.append(task)
    print("Task added!")
```

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- Exact prompt: "Enter new task: " (FR-006)
- Appends input to `todos` list (FR-006)
- Exact confirmation: "Task added!" (FR-006)
- Accepts any string input (including empty strings)

---

### TASK-006: Implement view_tasks() function

**Description**: Display all tasks or "No tasks yet!" (FR-007, FR-008)

**Implementation**:
```python
def view_tasks():
    """Display all tasks with 1-based numbering, or message if empty."""
    if len(todos) == 0:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")
```

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- Empty list: displays "No tasks yet!" (FR-007)
- Non-empty list: displays "Your Tasks:" followed by numbered list (FR-008)
- Uses `enumerate(todos, start=1)` for numbering (FR-008 mandate)
- Numbering starts at 1, not 0

---

### TASK-007: Implement delete_task() function

**Description**: Delete task by number with validation (FR-009, FR-010, FR-011, FR-012)

**Implementation**:
```python
def delete_task():
    """Display tasks, prompt for number, and delete if valid."""
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
```

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- Calls `view_tasks()` first (FR-009)
- Exact prompt: "Enter task number to delete: " (FR-010)
- Uses `todos.pop(index - 1)` for deletion (FR-011 mandate)
- Displays "Invalid number!" for any invalid input (FR-012)
- Handles non-numeric, zero, negative, and out-of-range inputs

---

### TASK-008: Implement main() function with menu loop

**Description**: Main loop that drives the application (FR-002, FR-005)

**Implementation**:
```python
def main():
    """Main application loop."""
    while True:
        choice = show_menu()

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            break  # Exit application

if __name__ == "__main__":
    main()
```

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- Continuous loop until exit choice (FR-005)
- Routes to correct function for each choice
- Clean exit on choice 4 (no confirmation prompt)
- Includes `if __name__ == "__main__"` guard

---

### TASK-009: Add error handling for invalid inputs

**Description**: Ensure graceful error handling throughout (FR-013)

**Actions**:
- Review all input points for try-except blocks
- Ensure ValueError is caught for int() conversions
- Verify range validation for all numeric inputs
- Test with various invalid inputs (non-numeric, empty, special chars)

**Files Modified**: `todo.py`

**Acceptance Criteria**:
- All `int()` conversions wrapped in try-except
- Range validation present for menu choices and task numbers
- Application never crashes on invalid input (FR-013)
- Error messages are clear and helpful

---

### TASK-010: Manual testing - Add and view tasks

**Description**: Test User Story 1 acceptance scenarios

**Test Cases**:
1. Add task to empty list → verify storage
2. View tasks with 3 items → verify numbering 1, 2, 3
3. View empty list → verify "No tasks yet!" message
4. Add multiple tasks in succession → verify order preserved

**Acceptance Criteria**:
- All 4 acceptance scenarios from User Story 1 pass
- Task addition takes <5 seconds (SC-001)
- Task viewing takes <2 seconds (SC-002)

---

### TASK-011: Manual testing - Delete tasks

**Description**: Test User Story 2 acceptance scenarios

**Test Cases**:
1. Delete task #3 from 5-item list → verify removal and remaining tasks
2. Delete with invalid number (0, 10, -1) → verify "Invalid number!" message
3. Delete with non-numeric input ("abc") → verify graceful error handling

**Acceptance Criteria**:
- All 3 acceptance scenarios from User Story 2 pass
- Task deletion takes <10 seconds (SC-003)
- Invalid inputs handled gracefully (SC-004)

---

### TASK-012: Manual testing - Exit application

**Description**: Test User Story 3 acceptance scenarios

**Test Cases**:
1. Select Exit option → verify clean termination
2. Exit with unsaved tasks → verify no confirmation prompt

**Acceptance Criteria**:
- Both acceptance scenarios from User Story 3 pass
- Application exits cleanly with code 0
- No errors or hanging processes

---

### TASK-013: Manual testing - Edge cases

**Description**: Test edge cases identified in specification

**Test Cases**:
1. Invalid menu choice (5, 0, "abc") → verify error handling
2. Empty task input (just Enter) → verify accepted as valid
3. Delete from single-item list → verify correct behavior
4. Very long task description (100+ chars) → verify accepted
5. Special characters and emojis in tasks → verify UTF-8 support

**Acceptance Criteria**:
- All edge cases handled gracefully
- No crashes or unexpected behavior (SC-004)
- Application remains usable after errors

---

### TASK-014: Verify all success criteria

**Description**: Final validation against all success criteria

**Success Criteria Checklist**:
- [ ] **SC-001**: Add task <5 seconds
- [ ] **SC-002**: View tasks <2 seconds
- [ ] **SC-003**: Delete task <10 seconds
- [ ] **SC-004**: 100% graceful error handling
- [ ] **SC-005**: All 4 menu options functional
- [ ] **SC-006**: Code <200 LOC
- [ ] **SC-007**: Full workflow (add 3, view, delete 1, exit) <30 seconds

**Acceptance Criteria**:
- All 7 success criteria verified and passing
- Application meets all functional requirements (FR-001 through FR-015)
- Ready for delivery

---

## Execution Notes

**Dependencies**:
- TASK-001 and TASK-002 can run in parallel [P]
- TASK-003 depends on TASK-001
- TASK-004 through TASK-008 depend on TASK-003
- TASK-004 through TASK-008 can be implemented in any order (parallel [P])
- TASK-009 depends on TASK-004 through TASK-008
- TASK-010 through TASK-013 depend on TASK-009 (all code complete)
- TASK-010 through TASK-013 can run in parallel [P]
- TASK-014 depends on TASK-010 through TASK-013

**Estimated Time**: 1-2 hours for full implementation and testing

**Code Size Estimate**: 80-120 lines (well under 200 LOC limit)
