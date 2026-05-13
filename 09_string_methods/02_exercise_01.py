# Take a user's full name as input
# Print it in uppercase
# Print how many characters it has including spaces
# Check if it contains only letters using isalpha()

name = input("Enter your full name: ")

l = len(name)
l_check = name.isalpha()
print(f"Your Name in Upper Case: {name.upper()}")
print(f"It contains {l} characters including spaces")
print(f"Does it only contain letter?:{l_check}")