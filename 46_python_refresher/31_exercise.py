# Exercise 31 — Logical Operators
# Write a function that accepts three Boolean values: is_logged_in, is_verified, and is_admin.

# Check the following conditions:
# 1. The user is logged in and verified.
# 2. The user is logged in or is an admin.
# 3. The user is not verified.
# Print the result of each condition.

# Rules:
# - Use and, or, and not.
# - Use a function with three parameters.
# - No loops.
# Topic focus: Logical operators.

def logical_operator(is_logged_in, is_verified, is_admin):

    if is_logged_in == True and is_verified == True:
        print("USER IS LOGGED IN AND VERIFIED")
    if is_logged_in == True or is_admin == True:
        print("USER IS LOGGED IN AND IS AN ADMIN")
    if not is_verified: 
        print("USER IS NOT VERIFIED")

logical_operator(is_logged_in = True, is_verified = False, is_admin = False)