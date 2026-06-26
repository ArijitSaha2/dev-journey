# Revision Exercise 7
# Take a number as input
# Use a while loop
# Keep asking until the user enters 0
# Print "Program Ended" when the loop stops

num = int(input("Enter a number: "))

i = num

while i > 0:
    num = int(input("Enter a number: "))
    i = num
    if i == 0:
        print("Program Ended")
        break