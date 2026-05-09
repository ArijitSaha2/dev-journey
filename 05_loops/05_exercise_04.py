# Create a list of 5 names
# Use a for loop to print each name
# Skip any name that starts with the letter 'A'
# Stop the loop if you encounter the name 'Stop'

l = ["Rose", "Rosy", "Nina", "Aria","Titania", "Marie", "Stop"]

for names in l:
    if names.startswith("A"):
        continue
    if names == "Stop":
        print(f"Stop has been encountered.")
        break
    print(names)