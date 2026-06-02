# if __name__==__main__:(this script can be imported or run standalone)
# Functions and classes in this module can be resused without the main block of code executing
# Good practice(code is modular,
#               helps readability,
#               leaves no global variables,
#               avoid unintended execution)

# ex. library = Import library for functionality
#               When running library directly, display a help page

def favourite_food(food):
    print(f"Your Favourite food is {food}")

def main():
    print("This is script1")
    favourite_food("pizza")
    print("Goodbye!")

if __name__ == "__main__":
    main()