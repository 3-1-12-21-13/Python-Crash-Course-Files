# DOING SOMETHING AFTER A FOR LOOP
# You can continue to run code after a for loop. You just have to remember not
# to indent the code. It's important to understand that it won't apply to
# all the items on a list like the for loop. 
# Example below:
invites = ['ghenghis','angela','oscar','kublai']
for invite in invites:
    print(f"\nDear {invite.title()}, Would you like to attend my soiree?")
    print(f"Oh and {invite.title()}? Please bring a culturally appropriate gift.")
print(f"\nAlso please remember everyone that {invites[-1].title()} is not \
drinking at this time and would respect everyones discretion.\nThat means you, \
{invites[-2].title()}.")