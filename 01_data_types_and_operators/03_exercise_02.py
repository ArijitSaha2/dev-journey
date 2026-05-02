# Write a script that:

# Create a dictionary of 3 people with their names as keys and ages as values
# Print each person's age using their name
# Check if a specific name is in the dictionary
# Find who is older using a comparison operator

book = {"Jason": 27, "Allison": 21, "Andre": 25, "Jessie": 22}
print(book)

print(book["Jason"])
print(book["Allison"])
print(book["Andre"])
print(book["Jessie"])

print(f"Is Punisher person in the book: {"Punisher" in book}")

print("is Jason older then Allison:", book["Allison"] < book["Jason"])

print("is Jason older then Andre:", book["Andre"] < book["Jason"])

print("is Jason older then Jessie:", book["Jessie"] < book["Jason"])