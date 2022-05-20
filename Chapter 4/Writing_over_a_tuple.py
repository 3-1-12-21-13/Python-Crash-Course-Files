# WRITING OVER A TUPLE
# Althought you can't modify a tuple, you can assign a new value to a variable
# that represents a tuple. So if we wanted to change our dimensions, we could
# redefine the entire tuple:
dimensions = (200,50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 50)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)
# When compared with lists, tuples are simple data structures. Use them when
# you want to store a set of values that should not be changed throughout the
# life of a program.