# Create a list of names ["Alice", "Bob", "Charlie", "Diana", "Eve"]
# Use a loop to print only names that have more than 4 characters
# Print the names in uppercase
# Count and print how many names qualify

l = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

count = 0

for f_char in l:
    if len(f_char) > 4:
        count += 1
        print(f"{f_char.upper()}")

print(f"Total qualified names are {count}")