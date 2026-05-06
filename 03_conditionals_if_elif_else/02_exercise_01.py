# Ask the user to enter their age
# If age is 18 or above print "You are an adult"
# If age is between 13 and 17 print "You are a teenager"
# If age is below 13 print "You are a child"
# Handle the case where age is 0 or negative

a = int(input("Enter your age: "))

if a >= 18:
    print("You are an adult")

elif a >= 13 and a <= 17:
    print("You are a teenager")

elif a < 13 and a >= 1:
    print("You are a child")

else:
    print("Age cannot be negative or 0")