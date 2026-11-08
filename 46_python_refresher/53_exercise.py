# Exercise 53 — Dictionary Methods & Iteration
# Write a function that accepts a dictionary of 5 students and their marks.
# 1. Display all student names using .keys().
# 2. Display all marks using .values().
# 3. Display each student's name and marks using .items() and a loop.
# 4. Ask for a student name and use .get() to retrieve their marks. Handle missing names.
# 5. Add one new student using .update().
# Requirements:
# - Take all input from the user.
# - Use a function and loops.
# - Reuse your dictionary-building approach from Exercise 52.

def func(dictionary):
    print("Student Names: ",dictionary.keys())
    print("Student Marks: ",dictionary.values())
    print()

    print("Each student names and marks below: ")
    for keys, values in dictionary.items():
        print(f"{keys}: {values}")

    student_name = input("Enter name: ").strip().capitalize()
    if student_name in dictionary:
        print(f"Student {student_name}'s Marks = {dictionary.get(student_name)}")
    else:
        print("Name not found!")

    print()
    print("Enter your name and marks to be added in dictionary")
    print()
    student_name_2 = input("Enter name: ").strip().capitalize()
    marks = int(input("Enter your marks: "))
    dictionary.update({student_name_2: marks}) # It adds new values or updates existing ones

    print("Final dictionary: ",dictionary)

dictionary = {}

print("Enter your name and marks!")
print()

for x in range(5):
    names = input("Enter your name: ").strip().capitalize()
    marks = int(input("Enter your marks: "))
    print()
    dictionary[names] = marks

func(dictionary)