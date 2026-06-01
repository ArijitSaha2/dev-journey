# list comprehension = A concise way to create lists in python 
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# Think of it as a compressed for loop that builds a list automatically
# Instead of: create empty list → loop → append → done
# You just write: [what you want for each item in the collection]

# Lists
# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
# print(squares)

# String
# fruits = ["apple", "banana", "coconut", "mango"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)

# With Conditions
# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers if num % 2 == 1]
# print(positive_num)
# print(negative_num)
# print(even_num)
# print(odd_num)

# with conditions 
# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)