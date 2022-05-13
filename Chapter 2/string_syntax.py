#ADDING WHITESPACE
# whitespace refers to any nonprinting character such as spaces, tabs,
# and end of line symbols. You can use whitespace to organize your 
# output so it's easier for users to read.
# To add a tab to your text, use the character combination \t.
# Example below:
print("This is a message without a tab at the beginning.")
print("\tThis is a message WITH a tab at the beginning.")

#ADDING A NEWLINE
# To add a newline to a string, use the character combination \n.
# Example below:
print("This text has a newline \nhere.")

#COMBO
# You can combine the two together without any problems but it uses two
# backslashes. Example below:
print("Here is my title".title() + "\n\tnumber 1" + "\n\tnumber 2" + "\n\tnumber 3")
# You have to put the n before the t otherwise it wouldn't work. You'd add
# a tab to the end of the old line before starting a new one.

#STRIPPING WHITESPACE
# If you have whitespace at the end of a name, Python will treat it as 
# A seperate name. You can strip whitespace from the right with the rstrip() method.
# Example below:
spaced_r_message = "You can't see all the space but the computer can                 "
proof = "see?"
print(f"{spaced_r_message}{proof}")
print(f"\nHere I will get rid of it.\n{spaced_r_message.rstrip()} {proof}\nIsn't that better?")
# You can strip whitespace from the left with the lstrip() method.
# Example below:
spaced_l_message = "                  You can see all the space there?"
print(f"{proof.title()}{spaced_l_message}")
print(f"What about now? {spaced_l_message.lstrip()} No you can't. \nI got rid of it.")
# You can strip whitespace from both sides with the strip() method.
spaced_b_message = "          See the space both sides?            "
print(f"{proof.title()}{spaced_b_message}{proof.title()}")
print(f"Let's get rid of that.\n{proof.title()} {spaced_b_message.strip()} {proof.title()}\nNot anymore. I got rid of it.")