# Take a username as input
# Check if it's longer than 15 characters - print warning if so
# Print the username with first letter capitalized only
# Print how many vowels (a, e, i, o, u) are in the username
# Print the username reversed

name = input("Enter Username: ")

if len(name) > 15:
    print("Username Should not exceed 15 characters")

elif len(name) <= 15:
    print(name.capitalize())

Original = name
name = name.lower()

vowels = "a", "e", "i", "o", "u"
c = 0
for n in name[0:]:
    if n in vowels:
        c += 1 

print(f"There are {c} vowels")
print(Original[::-1])