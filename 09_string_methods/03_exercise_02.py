# Take a phone number as input (format: 123-456-7890)
# Count how many dashes it has
# Replace all dashes with spaces
# Print the result

phone = input("Enter phone: ")

num = phone.count("-")
print(f"Your phone has {num} dashes")

phone = phone.replace("-"," ")
print(f"Your phone number is {phone}")