# module = a file containing code you want to include in your program 
#          use 'import' to include a module(built-in or your own)
#          use to break up a large program reusable separate files

# print(help("math"))

# import math
# # import math as m
# # from math import e

# a, b, c, d, e = 1, 2, 3, 4, 5

# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

# OUR OWN MODULE
import example_module

result = example_module.pi
result2 = example_module.square(3)
result3 = example_module.cube(3)
result4 = example_module.circumference(3)
result5 = example_module.area(3)

print(result5)