# Exercise 2
# Create a decorator called excited.
# Before the function runs, print "Get Ready!".
# Create a function play_game(game).
# Print "Playing <game>".
# Decorate the function and call it with "Minecraft".

def excited(func):
    def wrapper(*args, **kwargs):
        print("Get Ready")
        func(*args, **kwargs)
    return wrapper

@excited
def play_game(game):
    print(f"Playing {game}")

play_game("Minecraft")