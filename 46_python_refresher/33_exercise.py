# Exercise 33 — Nested Conditionals
# Write a function that accepts a user's age and checks:
# 1. If the user is 18 or older:
#    - Check whether they have an ID.
#    - If they have an ID, print "Entry allowed".
#    - Otherwise, print "ID required".
# 2. If the user is under 18, print "Entry denied".
# Rules:
# - Use if, else and nested conditionals.
# - Use a function with two parameters: age and has_id.
# - No loops.
# Topic focus: Nested conditionals.

def age_verify(age, has_id):
    if age >= 18: 
        if has_id ==  True:
            print(f"USER is {age}")
            print("Entry allowed")
        else:
            print("Entry Denied ID REQUIRED")
    else:
        print("Entry Denied USER is under 18")

age_verify(27, True)