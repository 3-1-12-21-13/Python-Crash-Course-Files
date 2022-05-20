# EXERCISE 4-12
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think
# of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
buffet = ("vegan","vegetarian","chicken","pork","cow")
for item in buffet:
    print(f"The buffet options are - {item.title()}")
# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.
buffet = ("vegan","vegetarian","fish","octopus","cow")
print("\nThe buffet options have now changed.")
for item in buffet:
    print(f"The buffet options are now - {item.title()}")