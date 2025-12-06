# Research: Todo In-Memory Python Console Application

**Feature**: 001-todo-console-app
**Date**: 2025-12-06
**Status**: ✅ COMPLETED

## Overview

This document captures research decisions for the Todo Console Application. Since requirements are prescriptive and technology choices are explicitly specified, minimal research was needed.

## Technology Choices

### Python Version

**Decision**: Python 3.x (minimum 3.6 recommended, though 3.3+ works)

**Rationale**:
- Requirements specify Python without version constraints
- Python 3.6+ provides f-strings for cleaner string formatting (optional)
- Python 3.x is universally available across platforms
- Backwards compatibility not a concern (simple standard library features)

**Alternatives Considered**:
- Python 2.x: Deprecated, end-of-life January 2020
- Specific version pinning (3.11, 3.12): Unnecessary for this simple app

**Recommendation**: Target Python 3.6+ for widest compatibility while maintaining modern Python practices

### Standard Library Features

**Decision**: Use only Python standard library (no pip dependencies)

**Rationale**:
- FR-003 explicitly forbids external dependencies
- All required features available in stdlib:
  - `input()` for user input
  - `print()` for output
  - `list` for task storage
  - `enumerate()` for numbered display (FR-008 requirement)
  - Try-except for error handling

**Alternatives Considered**:
- External libraries (rich, click): Forbidden by requirements
- File I/O modules: Explicitly forbidden (FR-003)

**Recommendation**: Pure Python 3 standard library implementation

## Design Patterns

### Control Flow

**Decision**: While-loop with break for menu system

**Rationale**:
- FR-005 requires continuous menu repetition until exit
- Standard Python pattern: `while True:` with conditional `break`
- Clear, readable, no stack overflow risk
- Easy to test and debug

**Alternatives Considered**:
- **Recursive menu calls**: Could cause stack overflow with many iterations, less clear control flow
- **State machine pattern**: Over-engineered for 4 simple menu options
- **Event-driven architecture**: Unnecessary complexity for synchronous console I/O

**Recommendation**: Simple while-True loop with break on exit choice

### Error Handling

**Decision**: Try-except blocks for input validation

**Rationale**:
- FR-013 requires graceful handling of invalid inputs
- Try-except is Pythonic (EAFP: Easier to Ask Forgiveness than Permission)
- Handles both non-numeric input (ValueError) and out-of-range integers
- Cleaner than extensive pre-validation logic

**Alternatives Considered**:
- **Pre-validation with `.isdigit()`**: Doesn't handle negative numbers, less Pythonic
- **Regex validation**: Over-engineered for simple integer input
- **Assert statements**: Wrong tool (for debugging, not user input validation)

**Recommendation**: Try-except ValueError for input conversion, explicit range checks for valid values

### Function Organization

**Decision**: Separate functions for each operation (add, view, delete, main)

**Rationale**:
- Single Responsibility Principle (Constitution Check requirement)
- Each function independently testable
- Clear mapping to functional requirements (FR-006, FR-007-008, FR-009-012)
- Easy to understand and maintain (<200 LOC constraint)

**Alternatives Considered**:
- **Single monolithic main()**: Violates SRP, harder to test, less readable
- **Class-based OOP design**: Over-engineered for simple stateless operations
- **Separate modules**: Violates FR-001 (single file requirement)

**Recommendation**: 4-5 functions in single file:
- `add_task(todos)` - handles FR-006
- `view_tasks(todos)` - handles FR-007, FR-008
- `delete_task(todos)` - handles FR-009, FR-010, FR-011, FR-012
- `show_menu()` - displays menu, handles input (FR-004, FR-015)
- `main()` - initialization and control loop (FR-002, FR-005)

## Input Validation Strategy

### Menu Selection Validation

**Decision**: Convert to int, check range 1-4, catch ValueError

```python
try:
    choice = int(input("Choice: "))
    if 1 <= choice <= 4:
        # valid
    else:
        # invalid range
except ValueError:
    # non-numeric input
```

**Rationale**:
- Handles both non-numeric and out-of-range inputs
- FR-013 compliance (basic error handling)
- Re-prompts user by returning to menu loop

### Task Number Validation (Delete)

**Decision**: Convert to int, check range 1 to len(todos), catch ValueError

```python
try:
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(todos):
        todos.pop(num - 1)  # FR-011 requirement
    else:
        print("Invalid number!")  # FR-012 requirement
except ValueError:
    print("Invalid number!")  # FR-012 requirement
```

**Rationale**:
- FR-012 mandates "Invalid number!" message for any invalid input
- FR-011 mandates `pop(index - 1)` method
- Handles zero, negative, too-large, and non-numeric inputs

### Empty Task Input

**Decision**: Accept empty strings as valid tasks

**Rationale**:
- Specification doesn't forbid empty tasks
- Edge case list mentions it but doesn't specify rejection
- User can delete empty tasks if unwanted
- Simpler implementation (no special case code)

**Alternatives Considered**:
- Reject empty input: Requires additional validation, spec doesn't mandate
- Prompt for confirmation: Over-engineered, spec doesn't require

**Recommendation**: Accept empty strings (principle of least surprise, spec doesn't forbid)

## Edge Cases Resolution

| Edge Case | Decision | Rationale |
|-----------|----------|-----------|
| Invalid menu choice (5, 0, -1) | Display error, re-show menu | FR-013 graceful error handling |
| Empty task input | Accept as valid | Spec doesn't forbid, user can delete if unwanted |
| Delete from single-item list | Standard pop() handles correctly | Python list.pop() works for any valid index |
| Long task descriptions (100+ chars) | Accept without truncation | Assumption allows up to 500 chars, no UI constraint |
| Non-numeric input for menu | Catch ValueError, re-show menu | FR-013 graceful error handling |
| Special characters/emojis in tasks | Accept without sanitization | Python 3 UTF-8 support, no security risk in console app |
| Invalid task number (0, -1, >length) | Display "Invalid number!" | FR-012 explicit requirement |
| Delete when list is empty | Show "No tasks yet!" first (via view) | FR-009 requires showing tasks first |

## Code Organization

### File Structure (todo.py)

```python
# Global list (FR-002 requirement)
todos = []

# Helper functions
def show_menu():
    # FR-004, FR-015: Display menu, return validated choice
    pass

def add_task():
    # FR-006: Prompt, append, confirm
    pass

def view_tasks():
    # FR-007, FR-008: Display or "No tasks yet!"
    pass

def delete_task():
    # FR-009-012: View, prompt, validate, delete or error
    pass

def main():
    # FR-005: While loop until exit
    pass

if __name__ == "__main__":
    main()
```

**Estimated LOC**: 80-120 lines (well under 200 LOC constraint SC-006)

## Performance Considerations

**Decision**: No optimization needed

**Rationale**:
- In-memory list operations are O(1) for append, O(n) for enumerate/pop
- Expected scale: Dozens of tasks, not thousands
- All operations complete in <1ms for realistic task counts
- Success criteria (SC-001, SC-002, SC-003) easily met without optimization

## Testing Approach

### Manual Testing (Primary)

**Decision**: Console-based manual testing against acceptance scenarios

**Rationale**:
- Console application requires interactive testing
- Specification provides detailed acceptance scenarios (Given-When-Then)
- Success criteria include time-based metrics (requires manual verification)
- No automated test requirement in spec

**Test Plan**: Execute all acceptance scenarios from spec (User Stories 1-3)

### Optional Automated Testing

**Decision**: Unit tests optional, not required for initial implementation

**Rationale**:
- Spec doesn't mandate automated tests
- Functions are pure enough to unit test (pass `todos` as parameter)
- Could add pytest later for regression testing
- Manual testing sufficient for MVP

**If implemented later**:
```python
def test_add_task():
    todos = []
    # simulate input, verify append
    assert len(todos) == 1

def test_view_tasks_empty():
    # capture output, verify "No tasks yet!"
    pass
```

## Security Considerations

**Decision**: No special security measures needed

**Rationale**:
- Local console app, no network exposure
- No persistent storage (FR-003)
- No sensitive data handling
- No injection risk (console output, not shell execution)
- Python 3 handles UTF-8 safely

## Deployment

**Decision**: Single-file distribution

**Rationale**:
- FR-001: Single file (`todo.py`)
- No build step required
- No dependencies to install
- Cross-platform (Windows, macOS, Linux)

**Distribution**: Direct file sharing, version control, or inline documentation

## Next Steps

1. ✅ Research complete - all decisions documented
2. → Proceed to Phase 1: Create data-model.md
3. → Proceed to Phase 1: Create contracts/
4. → Proceed to Phase 1: Create quickstart.md
5. → Proceed to Phase 2: Generate tasks.md with `/sp.tasks`
