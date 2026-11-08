# Exercise 52 — Dictionary Basics
# Write a function that accepts a dictionary containing student names and their marks.
# 1. Create a dictionary using 5 student names as keys and their marks as values.
# 2. Display the complete dictionary.
# 3. Ask for a student name and display their marks.
# 4. Ask for another student and update their marks.
# 5. Display the updated dictionary.
# Requirements:
# - Take all names and marks through user input.
# - Use a function.
# - Handle a student name that doesn't exist when searching.

def func(dictionary):
    print(f"Display Dictionary: {dictionary}")
    print()

    print("For checking Marks")
    name = input("Enter your name: ").strip().capitalize()
    if name in dictionary:
        print(f"Marks of student {name} = {dictionary[name]}")
    else:
        print("Name not found")

    print("Enter your name only if your marks increased!")

    another_name = input("Enter your name: ").strip().capitalize()
    update_marks = int(input("Enter updated marks: "))
    if another_name in dictionary:
        dictionary[another_name] = update_marks
        print(f"Updated Dictionary: {dictionary}")
    else:
        print("Name not found.")

    


dictionary = {}

print("Write your name and marks!")
for x in range (5):
    students = input("Enter your name: ").strip().capitalize()
    marks = int(input("Enter your marks: "))
    print()
    dictionary[students] = marks

func(dictionary)