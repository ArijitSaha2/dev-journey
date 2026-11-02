# Exercise 16 — Expense Tracker
# Given:
# expenses = [120, 450, 80, 300, 150, 500, 60]

# Write a function that returns a dictionary containing:
# - "total" — total expenses.
# - "count" — number of expenses.
# - "above_200" — a list of expenses greater than 200.
# Expected output:
# {    "total": 1660,    "count": 7,    "above_200": [450, 300, 500]}

# Rules
# - Use a function and a loop.
# - No sum() or len().
# - Build the result yourself.

def expense_tracker(expenses):
    dictionary = {}
    total = 0
    count = 0
    above_200 = []

    for expense in expenses:
        count += 1
        total += expense
        if expense > 200:
            above_200.append(expense)
    dictionary['total'] = total
    dictionary['count'] = count
    dictionary['above_200'] = above_200

    return dictionary
print(expense_tracker([120, 450, 80, 300, 150, 500, 60]))