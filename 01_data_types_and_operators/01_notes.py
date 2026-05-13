# this is a comment

########################################################################

# numerical Data types

# integers 
1
100
5
# float
1. # 1.0 
50.0
3.142
# Complex
1 + 3j
########################################################################
# boolean
True
False
1 > 5  # False
########################################################################
# strings - character values, declared in single or double qoutes
'Hello World'
"1" # not the number 1, instead this represents the character "1"
########################################################################
# Collections - a collection of values
# list - a collection of values in a specific order 
[1, 2, 3, 'a']

# tuple - a collection of values in a specific order, but immutable
(1, 2, 3, 'a')

# set - a collection of values unordered and does not allow duplicates
{1, 2, 3}
{1, 2, 2, 2, 'a'} # this is same as {1, 2, 'a'}

# dictionary - a collection of unordered key, value pairs
{1: 'a', 2: 'b', 3: 'c'}

# operators
# python operators are special symbols used to perform specific operations on one or more operands. The variables, values, or expressions can be used as operands. For example, Python's addition operator (+) is used to perform addition operations on two variables, values, or expressions.

# Types of operators - Arithmetic, Comparison (Relational), Assignment, Logical, Bitwise, Membership, Identity

# arithmetic operator - It is used to perform basic mathematical operations such as addition, subtraction, multiplication, etc
# e.g. print(2 + 1) output = 3, print(2 - 1) output = 1

# comparison operator - Comparison operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.
# e.g. a = 1, b = 2 print(a > b) output = False a = 1, b = 2 print(a <= b) output = True

# Assignment operator - Python Assignment operators are used to assign values to variables.
# e.g. a = 1, a += 10, a *= 2

# bitwise operators - Python Bitwise operator works on bits and performs bit by bit operation. These operators are used to compare binary numbers.
# bitwise operators - work on binary (0s and 1s) representation of numbers
# e.g. a & b (AND), a | b (OR), a ^ b (XOR)
# skipping deep dive - revisit in DSA phase

# logical operators - Python logical operators are used to combile two or more conditions and check the final result.
# includes: and(both true else false), or(Atleast 1 True for True), not(does the opposite meaning if true makes false)
# e.g. 1 == 2 and 1 == 3 Output = false, 1 == 1 and 1 == 2-1 Output = True
# e.g. 1 == 2 or 1 == 1 Output = true, 1 == 2 or 1 == 2 output = false
# e.g a = True 
# not a  # False

# membership operators - Python's membership operators test for membership in a sequence, such as strings, lists, or tuples.
# e.g. 1 in (1,2,3) output = true, 
# L = ["a","b","c"] and don't ["a, b, c"] cuz it becomes a single string
# "a" in L output = True

# identity operators - compare the memory locations of two objects.
# e.g. a = [1, 2, 3, 4, 5], b = [1, 2], c = a
# print(a is c) and print(b is not a) output = True
# print(b is a) output = false

# Operators Precedence - the order in which Python evaluates operators in an expression.
# 2 + 3 * 4 = 14 (multiply first, then add)
# (2 + 3) * 4 = 20 (brackets first, then multiply)

########################################################################

# x = 3.14
# y = -4
# z = 5

# result = round(x)     # round(x) - rounds to nearest whole number
# result = abs(y)       # abs(y) - absolute value, distance from 0
# result = pow(4, 3)    # pow(4,3)  - 4 to the power of 3 = 64
# result = max(x, y, z) # max(x,y,z)- returns largest value
# result = min(x, y, z) # min(x,y,z)- returns smallest value

# print (result)

########################################################################

"""
import math

x = 9.9
# print(math.pi) # math.pi - value of pi
# print(math.e)  # math.e - Euler's number is approximately 2.718 — it's a mathematical constant used in exponential growth calculations, logarithms, and compound interest. Similar to how math.pi is used in geometry, math.e is used in calculus and finance.
# result = math.sqrt(x) # math.sqrt - square root
# result = math.ceil(x) # math.ceil - rounds up
# result = math.floor(x) # math.floor- rounds down

# print(result)"""