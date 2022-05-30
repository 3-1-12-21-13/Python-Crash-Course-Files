# The IF-ELIF-ELSE CHAIN
# If you want to use more than two options to test a condition, then using the IF-ELIF-ELSE syntax is the way forward. Python executes only one block in an IF-ELIF-ELSE chain. It runs each conditional text in order until one passes. 
# When a test passes, the code following that test is executed and Python skips the rest of the tests.
# Example below:
number = 23
if number < 20:
    print("The number is lower than 20.")
elif number == 20:
    print("The number is 20.")
elif number > 20:
    print("The number is greater than 20.")
else:
    print("I'm not sure this a number.")