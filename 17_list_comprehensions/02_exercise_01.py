# Use list comprehension to create a list of squares for numbers 1 to 10
# Use list comprehension to filter only even squares from that list
# Print both lists

square_even = []

square = [square_even * square_even for square_even in range(1, 11)]
even = [square_even * square_even for square_even in range(1, 11) if square_even % 2 == 0]

print(square)
print(even)