# Create a function using *args
# Accept any number of names
# Print each name in uppercase with its position number
# Example: "1. ALICE"

def any_names(*args):
    counter = 1
    for num_of_names in args:
        print(f"Name: {num_of_names.upper():<5}, Position Numer: {counter}")
        counter += 1


any_names("Alice",
          "Jake",
          "Emily",
          "AJ",
          "Stacy")