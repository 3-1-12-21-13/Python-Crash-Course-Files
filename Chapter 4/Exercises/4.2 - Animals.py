# EXERCISE 4.2
# 4-2. Animals: Think of at least three different animals that have a common
# characteristic. Store the names of these animals in a list, and then use a 
# for loop to print out the name of each animal.

paws = []
paws.append('lion')
paws.append('dog')
paws.append('cat')
for paw in paws:
    print(f"These are the animals in my list - {paw.title()}.")

# Modify your program to print a statement about each animal, such as A dog
# would make a great pet.

paws.append('cheetah')
paws.append('wolf')
for paw in paws:
    print(f"A {paw.title()} would make a great pet!")

# Add a line at the end of your program stating what these animals have in 
# common. You could print a sentence such as Any of these animals would make a
# great pet!
for paw in paws:
    print(f"A {paw.title()} would make a great pet!")
print("\nAll these animals would make a great pet!")
