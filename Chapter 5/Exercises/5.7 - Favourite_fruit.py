# EXERCISE 5-8
# Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.

# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ['banana','strawberry','apple']
for fruit in favorite_fruits:
    if fruit == 'banana':
        print(f"You really like {fruit}s!")
    elif fruit == 'strawberry':
        print(f"You really like {fruit}s!")
    elif fruit == 'apple':
        print(f"You really like {fruit}s!")
if 'kiwi' not in favorite_fruits:
    print("You don't like kiwis.")
