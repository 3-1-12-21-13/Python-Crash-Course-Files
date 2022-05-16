# USING RANGE TO MAKE A LIST OF NUMBERS
# If you want to make a list of numbers, you can convert the results of range()
# directly into a list using the list() function. When you wrap list() around a
# call to the range() function, the output will be a list of numbers.
numbers = list(range(1,6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given
# range. If you pass a third argument to range(), Python uses that value as a 
# step size when generating numbers.
# For example, here is a list of even numbers between 1 & 10.
# In this example, the range() function starts with the value 2 and then adds 2
# to that value. It adds 2 repeatedly until it reaches or passes the end value.
numbers = list(range(2,11,2))
print(numbers)

# You can create almost any set of numbers you want to using the range() function.
# For example, consider how you might make a list of the first 10 square numbers 
# (that is, the square of each integer from 1 through 10).
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# We start with an empty list called squares. 
# We tell Python to loop through each value from 1 to 10 using the range() function.
# Inside the loop, the current value is squared and assigned to the variable square. 
# Each new value of square is appended to the list squares. 
# Finally, when the loop has finished running, the list of squares is printed.

# Another way to do this is:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
