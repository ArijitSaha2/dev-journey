# Take a sentence as input
# Print the sentence with every character capitalized using .upper()
# Print only the first word (hint: use indexing to find the space)
# Print the sentence backwards
# Count how many times the letter 'e' appears

sentence  = input("Enter a sentence: ")
# Whos gonna address the elephant in the room
print(sentence.upper())

W = sentence.find(" ")
print(sentence[0:W])

print(sentence[::-1])

letter = sentence.lower().count("e")
print(f"The letter 'e' appears {letter} times")