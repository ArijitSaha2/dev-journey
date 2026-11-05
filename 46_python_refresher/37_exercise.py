# Exercise 37 — Match-case

# Write a program that accepts a menu choice from the user:
# - 1 → Display "Start Game"
# - 2 → Display "Load Game"
# - 3 → Display "Settings"
# - 4 → Display "Exit"
# - Anything else → Display "Invalid choice"
# Use Python's match-case statement.

def menu(choice):

    value = choice 

    match value:
        case 1:
            print("Gaming starting")
        case 2:
            print("Loading from last checkpoint")
        case 3:
            print("Opened Settings Menu")
        case 4:
            print("Exiting")
        case _:
            print("Invalid Choice")

print("""
1. Start Game
2. Load Game
3. Settings
4. Exit
""")

userinput = int(input("Enter your choice: "))
menu(userinput)