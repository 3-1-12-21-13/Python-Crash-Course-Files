# EXERCISE 5.2
# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

# Tests for equality and inequality with strings
string_1 = "This is the first string."
string_2 = "This is the second string."
if string_1 == string_2:
    print("string 1 and string 2 are equal.")
elif string_1 != string_2:
    print("string 1 and string 2 are not equal.")

# Tests using the lower() method
names = ["Barry","Gary","Larry"]
for name in names:
    if name.lower() == "barry":
        print(f"Hello, {name.lower()}. I have dropped your capital letter because you are an object as far as I am concerned.")
    else:
        print(f"Hello, {name}. It is good to see you again.")

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
one_to_ten = [i for i in range(1,11)]
for number in one_to_ten:
    if number == 5:
        print(f"{number} - This number is 5.")
    elif number > 5:
        print(f"{number} - This number is greater than 5.")
    elif number < 5:
        print(f"{number} - This number is less than 5.")

# Tests using the AND keyword and the OR keyword
print("\n")
for number in one_to_ten:
    if number > 3 and number < 5:
        print(f"{number} - This number is 4.")
    elif number == 1 or number < 2:
        print(f"{number} - This number is 1.")

# Test whether an item is in a list
print("\n")
fives = [i for i in range (0,51,5)]
print(f"Here is the list called fives - {fives}")
if 5 in fives:
    print("shockingly, 5 is in the list of fives.")

# Test whether an item is not in a list
if 6 not in fives:
    print("even more shockingly, 6 is not in the list of fives.")