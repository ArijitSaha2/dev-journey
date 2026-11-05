# Exercise 35 — User Input
# Write a program that:
# 1. Asks the user for their name, age and city.
# 2. Converts their age into an integer.
# 3. Displays all three values with appropriate labels.
# 4. Displays the data type of each value.
# Use input() and type casting.

def user_input(name, age, city):
    age = int(age)
    return f"Name: {name} {type(name)}\nAge: {age} {type(age)}\nCity: {city} {type(city)}"

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print(user_input(name, age, city))