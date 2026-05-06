# Ask the user to enter a number
# If the number is even print "Even number"
# If the number is odd print "Odd number"
# If the number is 0 print "Zero"

user = int(input("Enter your number: "))

if user == 0:
    print("You Entered 0 which is also even")

elif user % 2 == 0:
    print("Even number")

else:
    print("Odd Number")