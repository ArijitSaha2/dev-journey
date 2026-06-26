# Revision Exercise 5
# Take a user's full name as input
# Print it in lowercase
# Print whether the name starts with the letter "a"
# Print whether the name ends with the letter "n"

name = input("Enter your Full Name: ")

print(name.lower())

low = name.lower()

if low.startswith("a"):
    print(f"Name starts with 'a'?? = {True}")

else:
    print(f"Name starts with 'a'?? = {False}")

if low.endswith("n"):
    print(f"Name ends with 'n'?? = {True}")

else:
    print(f"Name ends with 'n'?? = {False}")