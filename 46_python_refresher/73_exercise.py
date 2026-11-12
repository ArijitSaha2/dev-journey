# Exercise 73 — Dates and Time (datetime)
# What this tests: Working with Python's datetime module.

# Task: Create a simple date and time display.

# Requirements:
# 1. Import the datetime module.
# 2. Display the current date and time.
# 3. Display only the current year, month and day.
# 4. Display only the current hour, minute and second.
# 5. Ask the user to enter a year, month and day.
# 6. Create a date object using the user's input and display it.
# Rules:
# - Use datetime.datetime.now().
# - Use datetime.date.today().
# - Use datetime.date() to create the user's date.
# - No classes or unnecessary functions.

import datetime

date_time = datetime.datetime.now()

date_today = datetime.date.today()

time = date_time.time()

print(f"Current date and time = {date_time}")
print(f"Current year, month, date = {date_today}")
print(f"Current Time = {time}")

u1 = int(input("Enter year: "))
u2 = int(input("Enter month: "))
u3 = int(input("Enter day: "))

user = datetime.date(u1, u2, u3)
print(user)