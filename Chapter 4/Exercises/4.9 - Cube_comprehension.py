# EXERCISE 4.9
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
cubes = [value**3 for value in range(1,11)]
numerals = list(range(1,11))
for cube in cubes:
    numeral = numerals.pop(0)
    print(f"The value of {numeral} cubed is - {cube}.")