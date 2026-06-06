# Revision - Scope
# Create a global variable x = 100
# Inside a function, modify x using the global keyword
# Print x before and after calling the function

x = 100

def func_x():
    global x
    x = 200

func_x()
print(x)


# Revision - Mixed Challenge
# Create a list of numbers 1 to 20
# Use list comprehension to get only numbers divisible by 3 or 5
# Print the result and the sum of all numbers in it

l = [i for i in range(1, 21) if i % 3 == 0 or i % 5 == 0]

print(f"Result = {l}\nSum of numbers {sum(l)}")