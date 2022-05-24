# CHECKING WHETHER A VALUE IS IN A LIST
# You can check whether a list contains a certain value before taking an action. To find out whether a particular value is already in a list, use the keyword IN.
mult_fives = [i for i in range(5,51,5)]
for i in range(1,51):
   if i in mult_fives:
        print(f"{i} is a multiple of 5.")
   else:
        print(f"{i} is not a multiple of 5.")
# The code block above starts by creating a list of all the multiples of 5 between 5 and 50. Then, it uses an IF keyword in a FOR loop to to go through all numbers between 1 and 50. The FOR loop then prints a different statement if the number is in the created list or not.