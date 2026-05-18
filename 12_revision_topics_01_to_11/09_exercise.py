# Create a list of numbers [5, 12, 3, 18, 7, 24, 9, 15]
# Use a loop to print only numbers that are divisible by 3
# Count how many divisible numbers there are
# Print the count at the end

l = [5, 12, 3, 18, 7, 24, 9, 15]

count = 0

for num in l:
    
    if num % 3 == 0:
        count += 1
        print(num)

print(f"Total numbers divible by 3 in list is {count}")