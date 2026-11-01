# Exercise 12 — Passed Students
# Given this dictionary:
# scores = {    "Alex": 85,    "John": 42,    "Sarah": 91,    "Mike": 58,    "Emma": 73}



# Write a function that returns a list containing the names of students who scored 60 or above.

# Expected output:
# ["Alex", "Sarah", "Emma"]

def passed_students(scores):
    Passed = []
    for keys, values in scores.items():
        if values >= 60:
            Passed.append(keys)

    return Passed 


print(passed_students({"Alex": 85, "John": 42, "Sarah": 91, "Mike": 58, "Emma": 73}))