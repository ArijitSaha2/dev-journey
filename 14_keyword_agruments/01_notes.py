# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello("Hello", title="Mr.", last="Spongebob", first="Squarepants") # keyword arguments, order doesn't matter
hello("Hello", "Mr", "Spongebob", "Squarepants") # positional arguments, order matters

# end = keyword argument in print() that defines what is printed at the END of output
#       default is "\n" (newline), change it to keep output on same line
# sep  = keyword argument in print() that defines the SEPARATOR between multiple arguments
#       default is " " (space), change it to separate with anything

for x in range(1, 11):
    print(x, end=" ") # end=" " keeps numbers on same line with space
print() # moves to next line
print("A", "B", "C", "D", sep="-") # sep="-" separates each argument with a dash instead of space