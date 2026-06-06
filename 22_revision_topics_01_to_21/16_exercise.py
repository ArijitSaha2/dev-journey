# Revision - Default Arguments & Keyword Arguments
# Create a function with name, age, and city parameters
# Set default values for age (18) and city ("Mumbai")
# Call it 3 times: with all args, with only name, with name and city as keyword argument

def func(name, age = 18, city = "Mumbai"):
    print(f"Hi {name}, your {age} years old in {city}")

func("Alice", 21, city ="New York")
func("Kayle", 22, city = "California")
func("Angie", 21, city = "Texas")
func("Tom")


# Revision - Iterables
# Create a list of 5 names
# Use a for loop to print each name with its index number
# Format: "1. Alice", "2. Bob" etc.

names = ["Alice", "Jessie", "Tanya", "Kaileigh", "Ariana"]

count = 1
for x in names:
    print(f"{count}. {x}")
    count += 1