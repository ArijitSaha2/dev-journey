# Revision - Logical Operators
# Ask the user for their age and whether they have an ID (yes/no)
# If age is 18 or over AND they have an ID print "Entry allowed"
# If age is 18 or over but no ID print "Need ID"
# Otherwise print "Entry denied"

age = int(input("Enter your age: "))
ask_id = input("Do you have ID?[Enter YES OR NO.]\nAnswer:").lower()

if age >= 18 and ask_id == "yes":
    print("Entry Allowed")
elif age >= 18 and ask_id == "no":
    print("Need ID")
else:
    print("Entry Denied")