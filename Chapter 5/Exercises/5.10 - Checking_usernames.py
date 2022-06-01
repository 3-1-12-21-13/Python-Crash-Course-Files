# EXERCISE 5.10
# Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users.
current_users = [f"User {i}" for i in range(1,6)]
current_users_lower = [user.lower() for user in current_users]
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
new_users = [f"User {i}" for i in range (1,3)]
new_users.append('New User 3')
new_users.append('New User 4')
# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}'s name is taken. You will need to choose a new username.")
    else:
        print(f"{new_user}'s name in available. Adding user.")
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)