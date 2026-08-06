# AI Coding Agent Demonstration

## Purpose

This demonstration shows why users must test and review AI-generated code.

The initial function correctly calculates the average of a normal list. However, it fails when the list is empty because Python cannot divide by zero.

The human-reviewed version checks whether the list is empty before performing the calculation.

## File

- [`average_demo.py`](average_demo.py)

## Initial AI-Suggested Code

```python
def ai_suggested_average(numbers):
    return sum(numbers) / len(numbers)
```

This function works with a normal list but produces a `ZeroDivisionError` when the list is empty.

## Human-Reviewed Code

```python
def reviewed_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)
```

The added condition prevents the error.

## Expected Output

```text
Normal input:
AI-suggested version: 90.0
Human-reviewed version: 90.0

Empty-list input:
AI-suggested version failed: cannot divide by zero.
Human-reviewed version: 0
```

## Main Lesson

AI-generated code can provide a useful starting point, but the user must test edge cases, identify errors, and understand the final solution.
