# Exercise 19 — Employee Salary Analyzer
# Given:
# employees = {"Alex": 35000, "John": 22000, "Sarah": 48000, "Mike": 28000, "Emma": 52000}

# Write a function that returns a dictionary containing:
# - Employees earning ₹30,000 or more.
# - The number of employees earning below ₹30,000.
# Rules:
# - Use a function and regular loop.
# - Use conditionals.
# - No dictionary comprehension.

def salary_analyzer(employees):
    Overall = {
    "earning_over_30k": [],
    "earning_below_30k": 0
    }
    for employee in employees:
        if employees[employee] >= 30000:
            Overall["earning_over_30k"].append(employee)
        else:
            Overall["earning_below_30k"] += 1

    return Overall
print(salary_analyzer({"Alex": 35000, "John": 22000, "Sarah": 48000, "Mike": 28000, "Emma": 52000}))