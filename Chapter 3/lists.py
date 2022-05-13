# LISTS
# A list is a collection of items in a particular order. You can make a list
# to include anything. lists contain more than one item so it's a good idea to
# name them as a plural.
# In Python, square brackets [] indicate a list, and individual elements are 
# separated by commas. Example below:
lists_example = ['list item 1','list item 2','list item 3','list item 4']

# If you print a list, it will print the whole thing with square brackets included.
# Example below:
print(lists_example)

# ACCESSING ELEMENTS IN A LIST
# An element is the term for whatever items are in your list.
# You can access them by writing the name of the list followed
# by the position of the element.
# Example below:
print(f"This is the first item on the list -", lists_example[0])

# ADDING METHODS TO AN ELEMENT
# You can add methods to an element the same way you would to a string
# Example Below:
print(f"This is the second item on the list with title() added - ", lists_example[1].title())

# USING NEGATIVE NUMBERS
# A handy way to find out the last item on any list is to call the
# element by using negative 1. Regardless of the list size this will always
# call the last item on the list.
# Example Below:
print(f"This is the last item on the list - ", lists_example[-1])

# USING INDIVIDUAL VALUES FROM A LIST
# You can use individual values from a list and use them to create a variable.
# Example Below:
lists_statement = f"The third item on the list is - {lists_example[2].title()}."
print(lists_statement)

# ADDING ELEMENTS TO A LIST
# The simplest way to add items to the end of a list is to use the append method.
# This will add an item to the end of a list.
# Example below:
lists_example.append('list item 5')
print(f"The new last item on the list is - ", lists_example[-1].title())

# You can use the append method to make it easy to build an empty list from the 
# ground up. 
# Example below:
new_list = []
new_list.append('new list item 1')
new_list.append('new list item 2')
new_list.append('new list item 3')
new_list_statement = f"The items on my new list are: \n{new_list[0].title()}\
\n{new_list[1].title()}\n{new_list[-1].title()}"
print(new_list_statement)