# Take a string input from user
# Print the first 3 characters
# Print the last 3 characters
# Print the string reversed
# Print every 2nd character

user = input("Enter a string: ")

print(f"First 3 characters = {user[0:3]}")
print(f"Last 3 characters = {user[-3:]}")
print(f"Reversed = {user[::-1]}")
print(f"Printed Every 2nd character = {user[::2]}")