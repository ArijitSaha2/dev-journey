# Ask the user to enter a number
# Use a while loop to print the reverse countdown from that number to 0
# Skip any number divisible by 4
# Stop if the number hits 5

num = int(input('enter a number: '))

while num >= 0:
    if num % 4 == 0:
        num -= 1 # is necessary here cuz the reason is just below this line
        continue # Here continue jumps straight back to to start of loop so value remains same without any change meaning it can loop continueous on the same value or even break the code
    print(num)
    num -= 1
    if num == 5:
        break