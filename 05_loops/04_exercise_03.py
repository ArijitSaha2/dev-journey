# Use a for loop to print the multiplication table of a number entered by the user
# Example: if user enters 5, print 5x1=5, 5x2=10 ... 5x10=50

i = int(input('Enter your number: '))
for numbers in range(1, 11):
    print(f"{i} x {numbers} = {i * numbers}")

"""
Incase question asks while loops
i  = int(input('enter your number: '))

num = 1

while num <= 10:
    print(f'{i} x {num} = {i * num}')
    num += 1

"""