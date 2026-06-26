# Revision Exercise 6
# Take a number as input
# Print "Even" if the number is even
# Otherwise print "Odd"
# If the number is negative, print "Negative Number" before checking even/odd

num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is negative")

if num % 2 == 0:
    print(f"{num} is even")

else:
    print(f"{num} is odd")