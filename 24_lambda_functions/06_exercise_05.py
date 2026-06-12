# Lambda Exercise 5
# Create a list of words = ["python", "java", "javascript", "go", "rust"]
# Use map and lambda to convert all words to uppercase
# Use filter and lambda to keep only words with more than 3 characters
# Print both results

words = ["python", "java", "javascript", "go", "rust"]

Bigger = list(map(lambda word: word.upper(), words))

reduce = list(filter(lambda small:len(small) > 3, words))

print(Bigger)
print(reduce)