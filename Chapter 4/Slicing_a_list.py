# SLICING A LIST
# In Python, when you work with a specific group of items within a list rather
# than the whole list or a single element, this is known as a slice.
player_list = [f"Player {i}" for i in range(1,6)]
print(f"My first three players are - {player_list[0:3]}.")
print(f"Players 2 through to 5 are - {player_list[1:5]}.")