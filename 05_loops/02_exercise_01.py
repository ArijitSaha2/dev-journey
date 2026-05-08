# Create a list of 10 numbers
# Use a for loop to print each number
# Skip any number divisible by 3 using continue
# Stop the loop if the number exceeds 7 using break


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in l:
    if n % 3 == 0:
        continue
    print(n)
    if n == 7:
        break