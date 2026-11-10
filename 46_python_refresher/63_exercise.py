# Exercise 63 — Understanding if __name__ == "__main__"
# Task: Create a program that demonstrates how Python executes code directly versus when a file is imported.

# Requirements:
# 1. Create a function called greet() that prints a welcome message.
# 2. Create another function called main() that calls greet().
# 3. Use if __name__ == "__main__": to call main().
# 4. Add a print statement outside the condition to demonstrate that top-level code executes when the file is imported.
# Rules:
# - Use only one Python file.
# - Research what __name__ and "__main__" represent.
# - Don't copy a complete solution from the documentation.

def greet():
    print("Hello World!")

def main():
    greet()


if __name__ == "__main__":
    main()

print("This is outside the condition.")