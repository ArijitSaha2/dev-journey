# Revision - *args & **kwargs
# Create a function that accepts any number of positional arguments
# Print each argument on a new line

# Create a function that accepts any number of keyword arguments
# Print each key and value in format "key: value"

def func1(*args, **kwargs):
    for x in args:
        print(x, end= " ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

func1("Mr", "Spongebob", "in" , "Ocean",
      Type = "TV Show",
      For_whom = "Kids",
      Duration = "Several Seasons")