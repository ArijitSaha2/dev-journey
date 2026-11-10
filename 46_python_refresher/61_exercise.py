# Exercise 61 — Working with datetime
# Task: Create a program that displays date and time information.

# Requirements:
# 1. Import the datetime module.
# 2. Display the current date and time.
# 3. Display only the current year, month and day.
# 4. Display only the current hour, minute and second.
# 5. Ask the user to enter a year, month and day, then create and display a date object using those values.
# Rules:
# - Research the datetime module and its classes using the official Python documentation.
# - Use functions and methods from the module rather than manually formatting the date yourself.
# - Keep everything in one exercise file.

import datetime 

def display():

    date_time = datetime.datetime.now()
    print(f"Current date and time = {date_time}")

    today = datetime.date.today()
    print(f"Current year month day = {today}")

    time = date_time.time()
    print(f"Current Hour Minute Second = {time}")

    ask1 = int(input("Enter year: "))
    ask2 = int(input("Enter month: "))
    ask3 = int(input("Enter day: "))

    user_values = datetime.date(ask1, ask2, ask3)
    print(f"Year Month Date from USER = {user_values}")


display()