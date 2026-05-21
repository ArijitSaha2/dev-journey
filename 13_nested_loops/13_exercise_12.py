# Create a list of 5 test scores
# Calculate and print the average using a loop
# No sum() allowed

test_scores = [79, 91, 80, 67, 95]

total = 0

for i in test_scores:
    total += i
sum_5 = total / len(test_scores)
print(f"Average = {sum_5:.2f}")