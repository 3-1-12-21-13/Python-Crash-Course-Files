# Testing for equality is case-sensitive in Python. This means that two values
# of the same name but different case will be seen as FALSE when compared.
# This will return as FALSE.
value = "Value"
print(value == "value")
# You can use methods on functions to correct this however.
# Example below:
value = "Value"
value.lower() == 'value'
print(value.lower() == 'value')
print(value)
# As you can see - we changed the value of the variable to lowercase for the if
# Statement but it doesnt change the whole value of the variable, as shown in
# following print statement.

# a site might use a conditional test like this to ensure that every user has a
# truly unique username, not just a variation on the capitalization of another 
# person’s username. When someone submits a new username, that new username is 
# converted to lowercase and compared to the lowercase versions of all existing
# usernames. During this check, a username like 'John' will be rejected if any 
# variation of 'john' is already in use.