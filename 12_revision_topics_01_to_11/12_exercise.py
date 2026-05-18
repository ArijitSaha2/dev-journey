# Create a list of numbers [4, 7, 2, 9, 1, 5, 8, 3, 6]
# Use a loop to reverse the list without using [::-1]
# Store the reversed list in a new variable
# Print both original and reversed

l = [4, 7, 2, 9, 1, 5, 8, 3, 6]
em = []

for num in l:
    em.insert(0, num)

print(f"Original = {l}")
print(f"Reversed = {em}")