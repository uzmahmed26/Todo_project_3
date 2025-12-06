# Console Interface Contract

**Feature**: Todo In-Memory Python Console Application
**Version**: 1.0.0
**Date**: 2025-12-06
**Type**: Human-Computer Interaction (Console I/O)

## Overview

This document specifies the exact console interface contract for the Todo application, including all prompts, outputs, and error messages per functional requirements.

## Interface Type

- **Medium**: Text-based console (stdin/stdout)
- **Protocol**: Synchronous request-response
- **Encoding**: UTF-8 (Python 3 default)
- **Platform**: Cross-platform (Windows, macOS, Linux)

## Main Menu Interface

### Display Format (FR-004, FR-015)

**Exact Output** (order is mandatory per FR-015):

```
=== Todo List Menu ===
1. Add new task
2. View all tasks
3. Delete a task
4. Exit
Enter your choice (1-4):
```

**Notes**:
- Options MUST appear in exact order: Add (1), View (2), Delete (3), Exit (4)
- Menu MUST repeat continuously (FR-005) until choice 4 selected
- Prompt format is recommended but not mandated (exact text from FR-004)

### Input Specification

**Format**: Integer 1-4
**Validation**:
- Accept: "1", "2", "3", "4" (numeric strings convertible to int)
- Reject: Non-numeric, out of range (0, 5, negative), empty input

**Error Handling**:
```
Invalid choice! Please enter 1, 2, 3, or 4.
```

**Behavior**: Re-display menu after error (return to menu loop)

## Operation 1: Add Task (FR-006)

### Request

**Prompt** (exact text required):
```
Enter new task:
```

**Input Specification**:
- Type: String (any valid Python string)
- Min length: 0 (empty string accepted)
- Max length: 500 characters (assumption)
- Encoding: UTF-8
- Special chars: Allowed (including emojis)

### Response

**Success Output** (exact text required):
```
Task added!
```

**Behavior**: Append task to `todos` list, return to main menu

### Example Interaction

```
Enter new task: Buy groceries
Task added!

=== Todo List Menu ===
...
```

## Operation 2: View Tasks (FR-007, FR-008)

### Request

**Trigger**: Menu choice 2

**No additional input required**

### Response - Empty List (FR-007)

**Exact Output** (when `len(todos) == 0`):
```
No tasks yet!
```

### Response - Tasks Present (FR-008)

**Format** (exact header required):
```
Your Tasks:
1. [task text]
2. [task text]
3. [task text]
...
```

**Requirements**:
- MUST use `enumerate(todos, start=1)` (FR-008 mandate)
- Numbering starts at 1 (not 0)
- Format: `{number}. {task_text}`

**Behavior**: Display tasks, return to main menu

### Example Interaction

```
=== Empty List ===
Your Tasks:
No tasks yet!

=== With Tasks ===
Your Tasks:
1. Buy groceries
2. Call dentist
3. Finish report
```

## Operation 3: Delete Task (FR-009, FR-010, FR-011, FR-012)

### Request - Part 1: Display Tasks (FR-009)

**Behavior**: MUST call `view_tasks()` first
**Output**: Same as Operation 2 (show current tasks before deletion)

### Request - Part 2: Get Task Number (FR-010)

**Prompt** (exact text required):
```
Enter task number to delete:
```

**Input Specification**:
- Type: Integer (1 to len(todos))
- Format: Numeric string convertible to int
- Validation: Check range after conversion

### Response - Success (FR-011)

**Behavior**:
- MUST use `todos.pop(index - 1)` (FR-011 mandate)
- Return to main menu (no confirmation message specified)

**Example**:
```
Your Tasks:
1. Buy groceries
2. Call dentist
3. Finish report

Enter task number to delete: 2

=== Todo List Menu ===
...
```

**Result**: Task "Call dentist" removed, list now ["Buy groceries", "Finish report"]

### Response - Invalid Input (FR-012)

**Exact Error Message** (FR-012 requirement):
```
Invalid number!
```

**Triggers**:
- Non-numeric input ("abc", "", "1.5")
- Zero or negative (0, -1, -5)
- Out of range (num > len(todos))

**Behavior**: Display error, return to main menu (no retry loop)

### Example Error Interactions

```
=== Non-numeric ===
Enter task number to delete: abc
Invalid number!

=== Out of range ===
Enter task number to delete: 10
Invalid number!

=== Zero ===
Enter task number to delete: 0
Invalid number!
```

## Operation 4: Exit (Implied)

### Request

**Trigger**: Menu choice 4

**No additional input required**

### Response

**Behavior**:
- Break menu loop
- Terminate program cleanly
- No confirmation prompt (per acceptance scenario: exits without prompting)

**Exit Code**: 0 (success)

**Example**:
```
Enter your choice (1-4): 4

[Program terminates]
```

## Error Handling Summary

| Error Condition | User Action | Response | Next State |
|-----------------|-------------|----------|------------|
| Invalid menu choice | Enter 0, 5, "abc" | "Invalid choice! Please enter 1, 2, 3, or 4." | Re-show menu |
| Delete: non-numeric | Enter "abc" for task number | "Invalid number!" | Return to menu |
| Delete: out of range | Enter 10 when only 3 tasks | "Invalid number!" | Return to menu |
| Delete: zero/negative | Enter 0 or -1 | "Invalid number!" | Return to menu |
| Delete: empty list | Attempt delete with no tasks | "No tasks yet!" (from view step) | Return to menu |

## State Machine

```
[Start Program]
    ↓
[Show Menu] ←──────────────────┐
    ↓                           │
[Get Choice]                    │
    ↓                           │
Choice 1: Add Task → Confirm ──┘
Choice 2: View Tasks ──────────┘
Choice 3: Delete Task ─────────┘
Choice 4: Exit
    ↓
[End Program]
```

## Data Flow

### Input Flow

```
Console (stdin)
    ↓
input() function
    ↓
Validation (try-except, range check)
    ↓
Action (append, pop, display)
```

### Output Flow

```
Action result
    ↓
print() function
    ↓
Console (stdout)
```

## Testing Contract

### Test Cases

| Test ID | Operation | Input | Expected Output | Pass Criteria |
|---------|-----------|-------|-----------------|---------------|
| TC-01 | Menu | "1" | Prompt for new task | Exact prompt match |
| TC-02 | Menu | "5" | "Invalid choice!" | Error message match |
| TC-03 | Add | "Buy milk" | "Task added!" | Exact message match |
| TC-04 | View (empty) | - | "No tasks yet!" | Exact message match |
| TC-05 | View (3 tasks) | - | Numbered list 1-3 | Uses enumerate, start=1 |
| TC-06 | Delete | "2" (of 3) | Task removed | Middle task gone |
| TC-07 | Delete | "10" (of 3) | "Invalid number!" | Exact message match |
| TC-08 | Delete | "abc" | "Invalid number!" | Exact message match |
| TC-09 | Exit | "4" | Program ends | Clean exit, code 0 |

### Acceptance Criteria

1. ✅ All prompts match exact text from FR-006, FR-007, FR-008, FR-010, FR-012
2. ✅ Menu options appear in exact order (FR-015)
3. ✅ Error messages are exact matches (FR-012)
4. ✅ `enumerate(todos, start=1)` used for display (FR-008)
5. ✅ `pop(index - 1)` used for deletion (FR-011)
6. ✅ Invalid input doesn't crash program (FR-013)

## Integration Points

- **Input**: Python `input()` function (blocking, synchronous)
- **Output**: Python `print()` function (immediate, stdout)
- **Encoding**: UTF-8 (Python 3 default for console I/O)
- **Platform**: Console abstraction layer (works on all OSes)

## Non-Functional Requirements

- **Performance**: SC-001-003 (operations complete in <2-10 seconds)
- **Reliability**: SC-004 (100% graceful error handling)
- **Usability**: SC-007 (full workflow <30 seconds)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-06 | Initial contract based on FR-004 through FR-015 |

## Notes

- This is a human-facing interface, not a machine API
- Exact text prompts are mandatory per functional requirements
- No REST/GraphQL/RPC - pure console I/O contract
- Interface is synchronous (blocking input/output)
