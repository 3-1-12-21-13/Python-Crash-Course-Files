# CHECKING FOR INEQUALITY
# to determine whether two values are not equal, you can combine an exclamation
# point and an equal sign (!=). The exclamation point represents not.
values = (i for i in range(1,6))
for value in values:
    if value != 5:
        print(f"{value} - This number is not 5.")
    else:
        print(f"{value} - This number is 5.")