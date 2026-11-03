# Exercise 21 — Username Cleaner
# You are given a list of usernames:
# usernames = ["Alex99", "JOHN", "Sarah_22","", "mike123", "ab"]

# Write a function that:
# 1. Removes unnecessary whitespace.
# 2. Converts usernames to lowercase.
# 3. Excludes usernames shorter than 5 characters.
# 4. Returns a new list without modifying the original.
# Rules:
# - Use a function, loop and conditionals.
# - Use appropriate string methods.
# - No list comprehension.
# Topic focus: Strings, lists, loops and conditionals.

def username_cleaner(usernames):
    user = []
    update = 0
    for username in usernames:
        update = username.strip().lower()
        if len(update) >= 5:
            user.append(update)
            
    return user 

print(username_cleaner(["Alex99", "JOHN", "Sarah_22", "", "mike123", "ab"]))