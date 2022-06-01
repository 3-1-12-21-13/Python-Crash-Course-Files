# EXERCISE 5.9
# Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!

usernames = [f"user {i}" for i in range (1,5)]

usernames.append('admin')
for user in usernames:
    if usernames == []:
        print("We need to find some users!")
    elif user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

# Remove all of the usernames from your list, and make sure the correct message is printed.

del usernames
usernames = []

if usernames == []:
    print("We need to find some users!")