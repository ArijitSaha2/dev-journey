# Revision - If/Elif/Else
# Ask the user to enter their age
# If age is 18 or over print "Adult"
# If age is between 13 and 17 print "Teenager"
# Otherwise print "Child"

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
elif age >= 13 and age <= 17:
    print("Teenager")
else:
    print("Child")