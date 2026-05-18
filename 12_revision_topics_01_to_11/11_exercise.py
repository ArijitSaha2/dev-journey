# Create a list of numbers [10, 25, 3, 47, 8, 16, 33, 52, 7, 41]
# Use a loop to separate even and odd numbers into two separate lists
# Print both lists at the end

l = [10, 25, 3, 47, 8, 16, 33, 52, 7, 41]
ev = []
od = []

for num in l:
    if num % 2 == 0:
        ev.append(num)
    else:
        od.append(num)

print("Even =",ev)
print("Odd  =",od)