# EXERCISE 5.1
# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
player_list = [f"Player {i}" for i in range(1,6)]
print("\nIs there a player 3? I predict true.\n")
for player in player_list:
    if player == "Player 3":
        print("Player 3 is here.")
    else:
        print(f"This is {player}.")

