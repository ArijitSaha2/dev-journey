# Revision - While Loop
# Print numbers from 1 to 10
# Skip any number divisible by 3 using continue
# Stop the loop if the number is 8 using break

i = 1
while i in range(1, 11):
    if i % 3 == 0:
        i += 1
        continue
    elif i == 8:
        break
    print(i)
    i += 1