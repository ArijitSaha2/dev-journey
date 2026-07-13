# Exercise 7
# Create a function called greet_people() that accepts any number of names using *args.
# Inside the function:
# - Count how many names were passed.
# - Print "Total people: X".
# - Print each person's name on a new line.
#
# Only run the function if __name__ == "__main__".
#
# Call the function with at least five names.


if __name__ == "__main__":
    
    count = 0
    def greet_people(*args):
        global count
        for people in args:
            print(people)
            count += 1
        return count

    greet_people("Alice", "Ariana", "Ari", "Kaylee", "Kathy")
    print(f"Total People: {count}")