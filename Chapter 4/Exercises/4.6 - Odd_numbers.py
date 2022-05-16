# EXERCISE 4.6
# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = list(range(1,20,2))
for odd in odd_numbers:
    print(f"These are the odd numbers in my list - {odd}.")