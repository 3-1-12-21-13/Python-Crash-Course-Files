# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
# Example below:
# (I've chosen to not include friends actual names as that is a bit weird.)
friend_list = ['friend 1', 'friend 2', 'friend 3']
friend1 = f"The name of the first friend is - {friend_list[0].title()}."
friend2 = f"The name of the second friend is - {friend_list[1].title()}."
friend3 = f"The name of the last friend is - {friend_list[-1].title()}."
print(f"{friend1}\n{friend2}\n{friend3}")

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of
#  just printing each person’s name, print a message to them. The text of each
#  message should be the same, but each message should be personalized with the
#  person’s name.
print(f"Hello {friend_list[0].title()}, would you like to play a game?")
print(f"Hello {friend_list[1].title()}, would you like to play a game?")
print(f"Hello {friend_list[-1].title()}, would you like to play a game?")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your 
# list to print a series of statements about these items, 
# such as “I would like to own a Honda motorcycle.”
# Example below:
interesting_list = ['interesting item 1', 'interesting item 2', 233091]
statement1 = f"My favourite interesting item is - {interesting_list[0].title()}."
statement2 = f"My least favourite interesting item is - {interesting_list[1].title()}"
statement3 = f"My favourite number is - {interesting_list[-1]}."
print(f"{statement1}\n{statement2}\n{statement3}")

