# Revision Exercise 23
# Create a recursive function called countdown()
# It should take one number as a parameter
# Print the number
# Stop when the number reaches 0
# Call the function with 5

def countdown(num):
    if num == 0:
        return
    else:
        print(num)
        return countdown(num - 1)
countdown(5)