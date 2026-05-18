# Create a list of numbers [3, 7, 1, 9, 4, 6, 2, 8, 5]
# Use a loop to find the largest and smallest number
# Print both (no min() or max() allowed)

l = [3, 7, 1, 9, 4, 6, 2, 8, 5]

largest = l[0]

smallest = l[0]

for num in l:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest Number in list =",largest) 
print("Smallest Number in list =",smallest)