# Exercise 13 — Failed Students
# Given this dictionary:
# scores = {"Alex": 85, "John": 42, "Sarah": 91, "Mike": 58, "Emma": 73, "David": 35}



# Write a function that returns a dictionary containing only students who failed (scored below 60).

# Expected output:
# {"John": 42, "Mike": 58, "David": 35}



# Focus: Dictionary iteration, conditionals and adding key-value pairs.

# No filter() or dictionary comprehension. Use a regular loop.

def failed_students(scores):
    Failed = {}
    for keys, values in scores.items():
        if values < 60:
            Failed[keys] = values
    return Failed

print(failed_students({"Alex": 85, "John": 42, "Sarah": 91, "Mike": 58, "Emma": 73, "David": 35}))