# Implementation Plan: Todo In-Memory Python Console Application

**Branch**: `001-todo-console-app` | **Date**: 2025-12-06 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-todo-console-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a single-file Python console application that manages a todo list in memory. The application provides a menu-driven interface with four operations: add tasks, view all tasks, delete tasks by number, and exit. All tasks are stored in an in-memory list and are lost when the application terminates. The implementation must follow strict requirements for exact prompts, error messages, and use of specific Python constructs (e.g., `enumerate(todos, start=1)`, `pop(index - 1)`).

## Technical Context

**Language/Version**: Python 3.x (minimum 3.6 for f-strings if used, though not required)
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory list (variable name: `todos`)
**Testing**: Manual testing via console interaction; optional unit tests using pytest if desired
**Target Platform**: Cross-platform (Windows, macOS, Linux) - any system with Python 3.x
**Project Type**: Single file console application
**Performance Goals**: Instant response (<100ms for all operations given in-memory storage)
**Constraints**:
  - Single file (`todo.py`)
  - Under 200 lines of code (SC-006)
  - No external dependencies
  - No persistent storage
  - Exact text prompts and messages as specified
**Scale/Scope**: Single-user, local execution, minimal complexity

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Assessment**: This is a simple learning/demonstration project with no constitution file defined. Creating minimal quality gates:

### Quality Gates

- ✅ **Simplicity**: Single file, no external dependencies, minimal abstractions
- ✅ **Testability**: Each function (add, view, delete) is independently testable
- ✅ **Scope Control**: FR-014 explicitly prevents scope creep (no editing, timestamps, persistence)
- ✅ **Error Handling**: FR-013 requires basic error handling for invalid inputs
- ✅ **Code Quality**: SC-006 enforces <200 LOC constraint

### Compliance

| Principle | Status | Notes |
|-----------|--------|-------|
| Single Responsibility | ✅ PASS | Each function handles one operation (add/view/delete) |
| Error Handling | ✅ PASS | FR-013 mandates graceful handling of invalid inputs |
| Code Size | ✅ PASS | <200 LOC requirement enforces simplicity |
| No Over-Engineering | ✅ PASS | FR-014 prevents feature creep |

**Gate Status**: ✅ **PASSED** - All quality gates satisfied. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console-app/
├── spec.md              # Feature specification
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (minimal for console app)
├── checklists/          # Quality validation
│   └── requirements.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
todo.py                  # Single file containing entire application
```

**Structure Decision**: Single file structure selected per FR-001. All code (menu loop, add task, view tasks, delete task, error handling) will be contained in `todo.py` at the repository root. No subdirectories needed for this minimal application.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations detected. All design decisions align with simplicity principles.

---

## Phase 0: Research

**Status**: ✅ COMPLETED

All technical decisions are straightforward for this simple application. No research needed.

### Technology Decisions

**Decision**: Python 3.x standard library only
**Rationale**: Requirements explicitly forbid external dependencies. Console I/O and list operations are built into Python.
**Alternatives Considered**: None applicable - requirements are prescriptive.

**Decision**: While loop for menu
**Rationale**: FR-005 requires continuous menu repetition until exit. Standard pattern: `while True:` with `break` on exit choice.
**Alternatives Considered**: Recursion (less clear, potential stack issues), state machine (over-engineered).

**Decision**: List methods for task management
**Rationale**: FR-002 mandates `todos` list. FR-008 requires `enumerate(todos, start=1)`. FR-011 requires `pop(index - 1)`.
**Alternatives Considered**: None - requirements are prescriptive.

**Decision**: Try-except for error handling
**Rationale**: FR-013 requires graceful error handling for invalid inputs (non-numeric menu choices, invalid task numbers).
**Alternatives Considered**: Pre-validation with `.isdigit()` (less Pythonic, doesn't handle negative numbers), regex validation (over-engineered).

### Edge Case Handling Strategy

| Edge Case | Solution |
|-----------|----------|
| Invalid menu choice (not 1-4) | Try-except ValueError for int conversion, range check, re-prompt |
| Empty task input | Accept as valid (spec doesn't forbid empty strings) |
| Delete from single-item list | Standard pop() handles this correctly |
| Very long task descriptions (100+ chars) | Accept as valid (spec allows up to 500 chars per assumption) |
| Non-numeric input for menu/delete | Try-except ValueError, display error, re-prompt |
| Special characters/emojis | Python 3 handles UTF-8 by default, accept as valid |
| Invalid task number (0, negative, >length) | Check range, display "Invalid number!" per FR-012 |

---

## Phase 1: Design & Contracts

**Status**: ✅ COMPLETED

### Data Model

See [data-model.md](data-model.md) for detailed entity design.

**Summary**: Single entity (Task as string) stored in `todos` list. No complex relationships or state machines.

### API Contracts

See [contracts/](contracts/) for detailed interface specifications.

**Summary**: Console I/O contract - menu selections (1-4) as input, text prompts and confirmations as output.

### Quickstart Guide

See [quickstart.md](quickstart.md) for user and developer onboarding.

**Summary**: Run `python todo.py`, select menu options, follow prompts.

---

## Implementation Approach

### Function Breakdown

Based on the specification, the implementation will consist of:

1. **`add_task()`**
   - Display: "Enter new task: "
   - Read input
   - Append to `todos` list
   - Display: "Task added!"

2. **`view_tasks()`**
   - If `len(todos) == 0`: display "No tasks yet!"
   - Else: display "Your Tasks:" + enumerate(todos, start=1)

3. **`delete_task()`**
   - Call `view_tasks()` first (FR-009)
   - Display: "Enter task number to delete: "
   - Read input
   - Validate: try converting to int, check range 1 to len(todos)
   - If valid: `todos.pop(index - 1)` (FR-011)
   - If invalid: display "Invalid number!" (FR-012)

4. **`show_menu()`**
   - Display menu options 1-4 in exact order (FR-015)
   - Return user choice

5. **`main()`**
   - Initialize `todos = []` (FR-002)
   - While loop for continuous menu (FR-005)
   - Match choice to function call
   - Break loop on choice 4 (Exit)

### Error Handling Strategy

- **Menu input**: Try-except ValueError for non-numeric input
- **Delete input**: Try-except ValueError + range validation
- **Invalid range**: Check `1 <= choice <= 4` for menu, `1 <= num <= len(todos)` for delete
- **Re-prompting**: Invalid input doesn't crash, returns to menu

### Testing Strategy

**Manual Testing Checklist** (from spec acceptance scenarios):

1. ✅ Add task to empty list → confirm storage
2. ✅ View tasks with 3 items → verify numbering
3. ✅ View empty list → verify "No tasks yet!" message
4. ✅ Add multiple tasks in succession → verify order
5. ✅ Delete task #3 from 5-item list → verify removal
6. ✅ Delete with invalid number → verify error message
7. ✅ Delete with non-numeric input → verify graceful handling
8. ✅ Exit application → verify clean termination
9. ✅ Invalid menu choice → verify error handling
10. ✅ Full workflow (add 3, view, delete 1, exit) → verify <30 seconds (SC-007)

**Optional Unit Tests** (if pytest added later):
- Test `add_task()` appends to list
- Test `view_tasks()` with empty list returns expected message
- Test `delete_task()` with valid index removes correct item
- Test error handling for invalid delete index

---

## Success Validation

Verify against Success Criteria from spec:

- **SC-001**: Add task <5 seconds ✅ (instant in-memory operation)
- **SC-002**: View tasks <2 seconds ✅ (instant list enumeration)
- **SC-003**: Delete task <10 seconds ✅ (instant pop operation)
- **SC-004**: No crashes on invalid input ✅ (try-except error handling)
- **SC-005**: All 4 menu options functional ✅ (function per operation)
- **SC-006**: <200 LOC ✅ (estimated 80-120 lines)
- **SC-007**: Full workflow <30 seconds ✅ (no performance bottlenecks)

---

## Next Steps

1. Run `/sp.tasks` to generate dependency-ordered task list
2. Review and approve tasks
3. Run `/sp.implement` to execute implementation
4. Perform manual testing against acceptance scenarios
5. Verify all success criteria met
