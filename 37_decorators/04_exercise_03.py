# Exercise 3
# Create a decorator called login_required.
# Before the function runs, print "Checking login...".
# Create a function open_profile(username).
# Print "<username>'s profile opened".
# Decorate the function and call it with your name.

def login_required(func):
    def wrapper(*args, **kwargs):
        print("Checking Login...")
        func(*args, **kwargs)
    return wrapper

@login_required
def open_profile(username):
    print(f"{username}'s profile opened")

open_profile("Camilla Cabello")