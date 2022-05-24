# JANKY CODE
# This code takes a number (num), and gives you its first 10 multiples.
# It will print all the other numbers between between num and the sum of itself*10.
# It then stores these multiples in two lists for future use. One list with the 10 multiples. The other is all the numbers which weren't multiples.

num = 200
mult_num = []
not_mult_num = []
for i in range(1,num*10+1):
    if i in range(num,(num*10+1),num):
        print(f"{i} is a multiple of {num}.")
        mult_num.append(i)
    else:
        print(f"{i} is not a multiple of {num}.")
        not_mult_num.append(i)
