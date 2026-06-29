# Exercise 2
# Create a class called Game.
# Add __init__(title, genre).
# Add __contains__(keyword) to check if the keyword exists in the title.
# Create one Game object.
# Check if "War" is in the game using the in operator.

class Game:

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __contains__(self, keyword):
        return keyword in self.title
    
game1 = Game("Forza Horizon 6", "Racing")
print('war' in game1)
print('Horizon' in game1)