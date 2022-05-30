# CHECKING WHETHER A VLUE IS NOT IN A LIST
# Sometimes you need to know if a valu does not appear in a list. You can use the keyword NOT in this situation. 
player_list = [f"Player {i}" for i in range (1,6)]
added_player = "Player 6"
if added_player not in player_list:
    print(f"{added_player.title()} has joined the game.")
# The IF line in this example reads quite clearly. If the added player variable is not in the player_list, then print the statement below.
