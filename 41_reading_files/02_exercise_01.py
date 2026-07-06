# Exercise 1
# Read and print the contents of story.txt using file.read().
# Read and print the contents of player.json using json.load().
# Read scores.csv using csv.reader() and print each row using a loop.
# Handle FileNotFoundError for each file.

# for .txt
file_path = "story.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)

