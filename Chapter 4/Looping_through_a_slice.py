# LOOPING THROUGH A SLICE
# You can slice in a for loop if you want to loop through a s subset of the
# elements in a list.

# EXAMPLE
# These are the names of the players uncapitalized.
player_names = ['ghenghis','angela','oscar','teddy','alexander']
# This line takes the names from player_names, capitalizes them, and stores
# them in player_names_capital.
player_names_capital = [i.title() for i in player_names ]
# This line creates a list where the values are "Player" followed by a numeric
# sequence. End Result is = "Player 1","Player 2" etc.
player_number = [f"Player {i}" for i in range(1,6)]
# This for loop takes the previous lists and combines them into a statement for
# the first three players. It should read: "Player 1 is Ghenghis" etc.
for player in player_names_capital[:3]:
    print(f"{player} is {player_number.pop(0)}.") 