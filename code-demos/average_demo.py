# AI Coding Agent Demonstration
# Topic: Why AI-generated code requires human review


# Initial AI-suggested version
def ai_suggested_average(numbers):
    return sum(numbers) / len(numbers)


# Human-reviewed version
def reviewed_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


# Test with a normal list
scores = [80, 90, 100]

print("Normal input:")
print("AI-suggested version:", ai_suggested_average(scores))
print("Human-reviewed version:", reviewed_average(scores))


# Test with an empty list
empty_scores = []

print("\nEmpty-list input:")

try:
    print("AI-suggested version:", ai_suggested_average(empty_scores))
except ZeroDivisionError:
    print("AI-suggested version failed: cannot divide by zero.")

print("Human-reviewed version:", reviewed_average(empty_scores))
