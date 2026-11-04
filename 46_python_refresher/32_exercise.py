# Exercise 32 — Conditional Statements
# Write a function that accepts a student's score and determines their grade.

# Grading criteria:
# - 90–100: A
# - 80–89: B
# - 70–79: C
# - 60–69: D
# - Below 60: F
# Rules:
# - Use if, elif and else.
# - Accept the score as a function parameter.
# - Return the grade.
# - No loops.
# Topic focus: Conditional statements.

def grading(score):

    if score >= 90:
        return "Grade - A"
    elif score >= 80:
        return "Grade - B"
    elif score >= 70:
        return "Grade - C"
    elif score >= 60:
        return "Grade - D"
    elif score < 60:
        return "Grade - F"       

print(grading(91))