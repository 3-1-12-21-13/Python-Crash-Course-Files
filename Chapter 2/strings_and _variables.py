# EXAMPLE OF METHODS WITHIN VARIABLES
# Below is the method title() being called on the variable 'message_for_title'. 
message_for_title = "This is the message for the title."
print(message_for_title.title())
# Every method is followed by a set of parenthesis (). This is because methods
# often require extra information to work correctly.

# Other string methods to alter text include upper() and lower(). 
# Examples below.
print(message_for_title.upper())
print(message_for_title.lower())

# USING VARIABLES IN STRINGS
# To insert a variables value into a string, place the letter f immediately
# before the opening quotation mark. Put braces around the name or names of 
# any variable you want to use inside the string. Python will replace each 
# variable with its value when the string is displayed. 
first_name = "Erlich"
middle_name = "Timothy"
last_name = "Bachman"
full_name= f"{first_name} {middle_name} {last_name}"
print(full_name)
# With f-strings, you can use them to compose complete messages using the 
# information assoaciated with a variable. Shown here:
print(f"Hello, {full_name.upper()}!")
# Another example
weird_emphasis = f"Hello, {first_name.title()} {middle_name.upper()} {last_name.title()}!"
print(weird_emphasis)