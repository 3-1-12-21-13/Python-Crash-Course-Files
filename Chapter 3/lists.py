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

# INSERTING ELEMENT INTO LIST
# You can add a new element to any position in a list using the insert() method
# Example below:
new_list.insert(3,'new list item 4')
print(f"The new item on the list is -",new_list[3].title())

# REMOVING ITEMS FROM LIST
# You can delete an item from a list using the del statement.
# Example below:
print(new_list_statement)
print("Now I remove item 1 from the list")
del new_list[0]
print("\nnow the list is:")
print(new_list)

# REMOVING AN ITEM USING THE POP() METHOD
# The pop() method removes the last value on a list and allows you to store it
# for later use. By default it will always take the last item on the list.
# You can define the position of the value you want to pop by placing its position
# in the brackets. 
# Example below:
pop_list_example = [1,2,3,4,5,6]
print(f"My list contains the numbers -",pop_list_example)
print("Now I will remove 6.")
the_number_6 = pop_list_example.pop()
print(f"My list contains the numbers -",pop_list_example)
print(f"The number 6 is now stored here -",the_number_6)
print("Now I will remove the number 3.")
the_number_3 = pop_list_example.pop(2)
print(f"My list now contains the numbers -",pop_list_example)
print(f"The number 3 is now stored here -",the_number_3)

# REMOVING AN ITEM BY VALUE
# You can remove an item from a list if you know the value by using remove().
# This is handy if you can recall the item name but not it's position on the
# list.
# Example below:
list_items = ['bottle','cup','glass','mug']
print(f"My items are listed as -",list_items)
print("Now I will remove mug.")
list_items.remove('mug')
print(f"My items are listed as -",list_items)

# ASSIGNING A VALUE FROM A REMOVED ITEM BY VALUE
# That is a stupid title. Anyway. You can use the remove() method to assign
# the removed value to a variable.
# Example Below:
list_items.append('chalice')
print(f"My list of items is now - ",list_items)
print("I will now remove chalice.")
things_I_wouldnt_drink_out_of = 'chalice'
list_items.remove(things_I_wouldnt_drink_out_of)
print(f"My list of items is now - ",list_items)
print(f"Chalice is now stored here -",things_I_wouldnt_drink_out_of)

# SORTING A LIST PERMANENTLY WITH THE SORT() METHOD
# You can use the sort() method on a list to change the values order
# into an alphabetical one.
# Example Below:
sort_list = ['d','b','a','c','e']
print("\nUnsorted list - ",sort_list)
sort_list.sort()
print("\nSorted list - ",sort_list)
# You can also use the reverse=true with sort() to reverse order the list.
# Example Below:
sort_list.sort(reverse=True)
print("\nReverse Sorted List - ",sort_list)

# SORTING A LIST TEMPORARILY WITH THE SORTED() METHOD
# You can use the sorted() method on a list to change the values order
# temporarily without affected the order of the list permanently. 
# Example Below:
print("\nHere is the original list - ", sort_list)
print("\nHere is the sorted list - ", sorted(sort_list))
print("\nHere is the original list again - ", sort_list)

# PRINTING A LIST IN REVERSE ORDER
# You can print the order of a list in reverse using the reverse()
# method. This will NOT alphabetically reverse the values. Just
# reverse their order in the list.
# Example Below:
sort_list = ['up','down','left','right']
print("\nHere is the original list - ", sort_list)
sort_list.reverse()
print("\nHere is the original list reversed - ", sort_list)

# FINDING THE LENGTH OF A LIST
# You can find the length of a list by using the len() function.
# Example Below:
len_list = [12341,134673,134212143,55556312489]
print("\nHere is a list of numbers - ", len_list)
print("Here are how many numbers are in the list - ", len(len_list))