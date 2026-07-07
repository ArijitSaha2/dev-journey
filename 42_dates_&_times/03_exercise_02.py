# Exercise 2
# Import the datetime module.
# Get the current date and time.
# Format it to display as: DD/MM/YYYY HH:MM:SS.
# Print the formatted date and time.

import datetime 

current_date = datetime.datetime.now()

current_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

print(current_date)