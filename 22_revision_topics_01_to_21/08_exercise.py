# Revision - String Methods
# name = "  hello world  "
# Remove the whitespace, capitalize only the first letter
# Replace "world" with "Python"
# Print the final result and its length

name = "  hello world  " 

result = name.strip(" ").replace("world", "Python")

print(result.capitalize(), len(result))