# Ask user to enter a number
# Print the multiplication table for that number (1 to 10)
# Use a while loop

user = int(input("Enter a number: "))

i = 1
while i < 11:
        print(f"{user} x {i} = {user * i}")
        i += 1