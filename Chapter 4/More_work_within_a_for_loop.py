# DOING MORE WORK WITHING A FOR LOOP
# This is essentially the same as the previous example except with a method
# included to demonstrate that you can add more to a for loop without breaking
# it.
# You can also include more than 1 line of code underneath the for loop and the
# loop will still consider it part of it. 
# Example below:
invites = ['ghenghis','angela','oscar','kublai']
for invite in invites:
    print(f"\nDear {invite.title()}, Would you like to attend my soiree?")
    print(f"Oh and {invite.title()}? Please bring a culturally appropriate gift.")
