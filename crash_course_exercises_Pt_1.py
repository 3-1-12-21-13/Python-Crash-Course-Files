#2-1. Simple Message: Assign a message to a variable, and then print that message.
message_2_1 = "This is a simple message"
print(message_2_1)

#2-2. Simple Messages: Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new message.
message_2_2 = "This is another simple message."
print(message_2_2)
message_2_2 = "This is an alteration to the previous simple message."
print(message_2_2)

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name_var = "Erlich"
print(f"Hello {name_var.title()}, \nWould you like to learn some Python today?")

#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name 
# in lowercase, uppercase, and title case.
name_var2 = "Erlich Bachman"
print(f"This is the name in lowercase - '{name_var2.lower()}'\nThis is the name in uppercase - '{name_var2.upper()}'\
    \nThis is the name in titlecase - '{name_var2.title()}'")

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, 
# including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
quote = "  Everyone has a plan until they get punched in the face.  "
author = "mike tyson"
print(f'{author.title()} once said, "{quote.strip()}"')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
# Then compose your message and represent it with a new variable called message. Print your message.
famous_person = "Mike Tyson"
quote_message = f'{famous_person} once said, "{quote.strip()}"'
print(quote_message)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three
# stripping functions, lstrip(), rstrip(), and strip().
name_var = "   Erlich Bachman     "
print(f'\nHere is the name unstripped - "{name_var}".\nHere is the name with lstrip - "{name_var.lstrip()}".\
    \nHere is the name with rstrip - "{name_var.rstrip()}".\nFinally, here is the name with strip - \
"{name_var.strip()}". \n\nThere. You happy now? Good.\n\n\t\tNow fuck off.\n\n\n')