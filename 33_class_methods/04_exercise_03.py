# Class Methods Exercise 3
# Create a class Game
# Add a class variable called game_name = "Minecraft"
# Create a class method called change_game_name()
# Change the game name to "GTA 6"
# Print the game name before changing it
# Print the game name after changing it

class Game:

    game_name = "Minecraft"

    @classmethod
    def change_game_name(cls):
        Game.game_name = "GTA 6"
        return f"{Game.game_name}"

print(Game.game_name)
print(Game.change_game_name())