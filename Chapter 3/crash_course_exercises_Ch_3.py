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

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you 
# invite? Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.
dinner_party = ['Ghenghis Khan,','Alexander the Great,','Alan Turing,','Lao Tzu,']
dinner_party_text = "Would you care to attend my dinner party?"
print(f"Dear",dinner_party[0],dinner_party_text,"\nDear",dinner_party[1],dinner_party_text,\
"\nDear",dinner_party[2],dinner_party_text,"\nDear",dinner_party[-1],dinner_party_text)

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# 
# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating
# the name of the guest who can’t make it.
#
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person
# you are inviting.
#
# Print a second set of invitation messages, one for each person who is still in your list.
print(f"Sorry everyone,",dinner_party[-1],"can't make it. Shame.")
dinner_party.pop(-1)
dinner_party.append('Angela Carter,')
print(f"Dear",dinner_party[0],dinner_party_text,"\nDear",dinner_party[1],dinner_party_text,\
"\nDear",dinner_party[2],dinner_party_text,"\nDear",dinner_party[-1],dinner_party_text)

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
#
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end 
# of your program informing people that you found a bigger dinner table.
#
# Use insert() to add one new guest to the beginning of your list.
#
# Use insert() to add one new guest to the middle of your list.
print("\nGood news, guys! I forgot I had a massive fucking table somehow! \nI've\
 invited even MORE people as a result.")
dinner_party.insert(0,'Kublai Khan,')
dinner_party.insert(2,'Oscar Wilde,')
dinner_party.append('H.P Lovecraft,')
print(f"Dear",dinner_party[0],dinner_party_text,"\nDear",dinner_party[1],dinner_party_text,\
"\nDear",dinner_party[2],dinner_party_text,"\nDear",dinner_party[3],dinner_party_text,\
"\nDear",dinner_party[4],dinner_party_text,"\nDear",dinner_party[5],dinner_party_text,\
"\nDear",dinner_party[-1],dinner_party_text)

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time 
# for the dinner, and you have space for only two guests.
#
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can 
# invite only two people for dinner.
#
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry
# you can’t invite them to dinner.
#
# Print a message to each of the two people still on your list, letting them know they’re still invited.
#
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make
# sure you actually have an empty list at the end of your program.
print("\nSorry guys, the table is actually really small.")
unvite_message1 = f'Sorry, {dinner_party.pop(6)} I am requesting you fuck off.'
unvite_message2 = f'Sorry, {dinner_party.pop(5)} I am requesting you fuck off.'
unvite_message3 = f'Sorry, {dinner_party.pop(4)} I am requesting you fuck off.'
unvite_message4 = f'Sorry, {dinner_party.pop(3)} I am requesting you fuck off.'
unvite_message5 = f'Sorry, {dinner_party.pop(2)} I am requesting you fuck off.'
print(unvite_message1)
print(unvite_message2)
print(unvite_message3)
print(unvite_message4)
print(unvite_message5)
print("My dinner party list is now - ",dinner_party)
print("That is still too many, I think.")
del dinner_party[:2]
print("My dinner party list is now - ",dinner_party)
print("Much better.")