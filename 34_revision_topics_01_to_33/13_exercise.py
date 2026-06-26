# Revision Exercise 13
# Create a string: "python programming"
# Print the string in uppercase
# Print how many times the letter "p" appears
# Replace "programming" with "coding"

s = "python programming"

print(s.upper())

count = 0 

small = s.lower()

for x in small:
    if x == "p":
        count += 1
    
print(f"Total 'p' = {count}")

change = s.replace("programming", "coding")
print(change)