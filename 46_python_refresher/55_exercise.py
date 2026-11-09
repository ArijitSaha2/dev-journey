# Exercise 55 — Collections & Iterators + Revision

# Write a function that accepts a list of student names and marks.
# 1. Create a dictionary using the names as keys and marks as values.
# 2. Use dictionary comprehension to create a new dictionary containing only students who scored 40 or above.
# 3. Use list comprehension to create a list of student names.
# 4. Convert that list into an iterator using iter().
# 5. Use next() to retrieve and display each name until the iterator is exhausted.
# 6. Display the final dictionary.
# Requirements:
# - Take 5 student names and marks through user input.
# - Use functions and loops where appropriate.
# - Use comprehensions, iter() and next().

def func(names, mark_s):
    dictionary = {}
    for keys, values in zip(names, mark_s):
        dictionary[keys] = values
    print(dictionary)

    di = {name: marks for name, marks in dictionary.items() if marks >= 40}
    print(f"Dictionary containing 40 or above: {di}")

    Li = [x for x in names]
    print(f"List comprehension: {Li}")

    iterator_name = iter(Li)
    print(next(iterator_name))
    print(next(iterator_name))
    print(next(iterator_name))
    print(next(iterator_name))
    print(next(iterator_name))

name = []
marks = []
for x in range(5):
    student_name = input("Enter name: ")
    mark = int(input("Enter marks: "))
    name.append(student_name)
    marks.append(mark)

func(name, marks)