def count_vowels(text):
    count = 0
    for alphabets in text:
        if alphabets.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("HEllo world"))