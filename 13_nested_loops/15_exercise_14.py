# Create a list of 3 teams, each team has 3 players
# Use a nested loop to print each team and its players
# Print team number and player number

team_1 = ['Player 1', 'Player 2', 'Player 3']
team_2 = ['Player X', 'Player Y', 'Player Z']
team_3 = ['Player +', 'Player -', 'Player $']

list_of_teams = [team_1, team_2, team_3]

counting = 0

for i in list_of_teams:
    counting += 1
    print(f"Team {counting} Has the following Players: ")
    for j in i:
        print(f"{j}\n",end = "")
    print()