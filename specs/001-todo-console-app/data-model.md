# Data Model: Todo In-Memory Python Console Application

**Feature**: 001-todo-console-app
**Date**: 2025-12-06
**Status**: ✅ COMPLETED

## Overview

This document defines the data model for the Todo Console Application. The model is intentionally minimal per requirements (FR-002, FR-014).

## Entities

### Task

**Type**: `str` (Python string)

**Description**: A single todo item represented as a plain text string.

**Storage**: Element in the `todos` list (Python list)

**Attributes**:
- Value: Free-form text (any valid Python string)
- No metadata (no timestamps, no status, no priority per FR-014)

**Constraints**:
- Minimum length: 0 (empty strings accepted per research.md decision)
- Maximum length: 500 characters (per spec assumption)
- Encoding: UTF-8 (Python 3 default)
- Special characters: Allowed (including emojis, per research.md)

**Examples**:
```python
"Buy groceries"
"Call dentist"
"Finish project report"
""  # empty task (valid but not recommended)
"Review PRs 🔍"  # with emoji (valid)
```

### Todos List

**Type**: `list[str]` (Python list of strings)

**Variable Name**: `todos` (FR-002 requirement)

**Description**: Ordered collection of all tasks, stored in-memory.

**Initialization**: `todos = []` (empty list at program start)

**Operations**:
- **Add**: `todos.append(task)` - Add new task to end (FR-006)
- **View**: `enumerate(todos, start=1)` - Display with 1-based numbering (FR-008)
- **Delete**: `todos.pop(index - 1)` - Remove by 1-based index (FR-011)
- **Check**: `len(todos) == 0` - Determine if empty (FR-007)

**Properties**:
- Order: Insertion order preserved (chronological)
- Indexing: Zero-based internally, presented as 1-based to user
- Persistence: None (data lost on program exit per FR-003)

**Invariants**:
- Always valid Python list (never None, never undefined)
- Contains only strings (no mixed types)
- Can be empty (valid state)

## Data Flow

### Add Task Flow

```
User Input (string)
    ↓
Validation: None (accept any string)
    ↓
todos.append(input_string)
    ↓
Confirmation: "Task added!"
```

### View Tasks Flow

```
Check len(todos)
    ↓
If empty → Display "No tasks yet!"
If not empty → Display "Your Tasks:"
    ↓
enumerate(todos, start=1)
    ↓
Display: "1. Task text"
         "2. Task text"
         ...
```

### Delete Task Flow

```
Display current tasks (call view_tasks)
    ↓
User Input (number as string)
    ↓
Validation:
  - Convert to int (catch ValueError)
  - Check range: 1 <= num <= len(todos)
    ↓
If valid → todos.pop(num - 1)
If invalid → Display "Invalid number!"
```

## State Transitions

```
[Initial State]
todos = []

    ↓ add_task()

[Tasks Present]
todos = ["task1", "task2", ...]

    ↓ delete_task() (until empty)

[Initial State]
todos = []
```

**State Properties**:
- Only two states: Empty or Non-Empty
- No intermediate/loading states (synchronous operations)
- State persists only during program execution

## Data Validation Rules

| Operation | Validation | Error Handling |
|-----------|------------|----------------|
| Add Task | None (accept any string) | N/A |
| View Tasks | Check if list empty | Display "No tasks yet!" |
| Delete Task | Convert to int, check range 1 to len(todos) | Display "Invalid number!" |
| Menu Choice | Convert to int, check range 1-4 | Re-prompt user |

## Data Constraints

### Functional Constraints

- **FR-002**: Must use variable name `todos`
- **FR-003**: No persistence (in-memory only)
- **FR-008**: Must use `enumerate(todos, start=1)` for display
- **FR-011**: Must use `pop(index - 1)` for deletion
- **FR-014**: No additional fields (timestamps, status, priority)

### Performance Constraints

- **SC-001**: Add operation <5 seconds (list append is O(1))
- **SC-002**: View operation <2 seconds (enumerate is O(n))
- **SC-003**: Delete operation <10 seconds (pop is O(n) worst case)

### Scale Constraints

- **Assumption**: "Reasonably short" task descriptions (<500 chars)
- **Expected Scale**: Dozens of tasks (not thousands)
- **Memory**: Negligible (<1MB for realistic usage)

## Schema Evolution

**Status**: N/A (no persistence, no versioning needed)

**Future Considerations** (if requirements change):
- Adding task status would require migration from `list[str]` to `list[dict]` or `list[Task]`
- Adding persistence would require serialization format (JSON, pickle, text file)
- Adding IDs would require `list[tuple[int, str]]` or similar

**Current Decision**: Keep simplest possible model (list of strings) per FR-014

## Relationships

**Status**: N/A (single entity, no relationships)

**Notes**:
- No user entity (single-user app)
- No categories/tags (FR-014 scope limit)
- No task hierarchy (flat list only)

## Data Access Patterns

### Read Operations

| Operation | Pattern | Frequency | Performance |
|-----------|---------|-----------|-------------|
| View all tasks | Iterate entire list | High (every view/delete) | O(n) |
| Check if empty | `len(todos) == 0` | Medium (every view) | O(1) |
| Get task by index | `todos[index]` (via pop) | Low (delete only) | O(1) |

### Write Operations

| Operation | Pattern | Frequency | Performance |
|-----------|---------|-----------|-------------|
| Add task | Append to end | High (primary operation) | O(1) |
| Delete task | Pop by index | Medium (cleanup operation) | O(n) worst case |

### Expected Access Pattern

1. User adds multiple tasks (append operations)
2. User views tasks (enumerate operation)
3. User deletes completed tasks (pop operations)
4. Repeat

**Optimization**: None needed (list operations are efficient for expected scale)

## Testing Data

### Test Fixtures

```python
# Empty state
todos = []

# Single task
todos = ["Buy milk"]

# Multiple tasks
todos = ["Buy milk", "Call dentist", "Finish report"]

# Edge cases
todos = [""]  # empty string task
todos = ["A" * 500]  # max-length task
todos = ["Task with emoji 🎉"]  # special characters
```

### Validation Test Cases

| Test Case | Input | Expected Behavior |
|-----------|-------|-------------------|
| Add to empty list | "Buy milk" | todos = ["Buy milk"] |
| Add multiple | 3 tasks | todos = [task1, task2, task3] |
| View empty | todos = [] | Display "No tasks yet!" |
| View multiple | todos = [3 tasks] | Display numbered 1-3 |
| Delete valid | num = 2 of 3 | Remove middle task |
| Delete invalid | num = 5 of 3 | Display "Invalid number!" |
| Delete non-numeric | "abc" | Display "Invalid number!" |

## Conclusion

The data model is intentionally minimal:
- **Single entity**: Task (as string)
- **Single collection**: todos (as list)
- **No persistence**: In-memory only
- **No metadata**: Plain text only

This simplicity aligns with:
- Functional requirements (FR-002, FR-003, FR-014)
- Success criteria (SC-006: <200 LOC)
- Constitution principles (simplicity, no over-engineering)

**Next**: See [contracts/](contracts/) for interface specifications
