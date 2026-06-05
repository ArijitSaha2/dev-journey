# Revision - Format Specifiers
# price = 1234567.891
# Print the price with 2 decimal places
# Print the price with 2 decimal places and comma separator
# Print the price as a percentage with 2 decimal places (multiply by 0.01 first)

price = 1234567.891

print(f"{price:.2f}")
print(f"{price:,.2f}")
print(f"{price:.2%}")