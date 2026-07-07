# Exercise 3
# Import the datetime module.
# Ask the user to enter an event name.
# Ask for the event year, month, day, hour, and minute.
# Create a datetime object using the entered values.
# Format the event datetime as: DD/MM/YYYY at HH:MM
# Print the event name and its scheduled date and time.

import datetime

nam = input("Enter event name: ")

ev1 = int(input("Enter event day: "))
ev2 = int(input("Enter event month: "))
ev3 = int(input("Enter event year: "))
ev4 = int(input("Enter event hour: "))
ev5 = int(input("Enter event minute: "))

date = datetime.datetime(ev3, ev2, ev1, ev4, ev5)

date = date.strftime("%d/%m/%Y on %H:%M")

print(f"Event Name: {nam}\nScheduled at {date}")