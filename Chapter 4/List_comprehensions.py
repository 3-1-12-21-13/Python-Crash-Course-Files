# LIST COMPREHENSIONS
# A list comprehension takes the 4 lines of code used earlier to create the
# square program and turns it into 1 line of code. It combines the for loop and
# the creation of new elements into one line and automatically appends each new
# element. 
# NOT FOR BEGINNERS - but you might see it in other code.
squares = [value**2 for value in range(1,11)]
print(squares)
# To use this syntax, begin with a the list. 
# Next, define the expression for the values you want to store in the new list. 
# In this example the expression is value**2, which raises the value to the second power. 
# Then, write a for loop to generate the numbers you want to feed into the expression.
# The for loop in this example is for value in range(1, 11), which feeds the values 1 
# through 10 into the expression value**2. 
# Notice that no colon is used at the end of the for statement.