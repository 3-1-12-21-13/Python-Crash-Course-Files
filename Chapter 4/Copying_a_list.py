# COPYING A LIST
# To copy a list, you can make a slice that includes the entire original list
# by omitting the first and second index. This tells Python to make a slice
# that starts at the first item and ends with the last item, producing an
# entire copy of the list.

# EXAMPLE
# This line creates a list where the values are 'item' followed by a numberic
# order. E.g. 'item 1','item 2' etc.
original_list = [f"item {i}" for i in range(1,6)]
# This line copies the original_list and capitalizes each entry. The copy is
# technically a slice as demonstrated by the syntax on the end of original_list
copied_list = [i.title() for i in original_list[:]]
print(f"The original list is - {original_list}")
print(f"The copied list is - {copied_list}")
# This block of code demonstrates how inserting another value into the original
# list after the initial copy means it does not show up on the copied list and
# vise-versa.
original_list.insert(0,'item 0')
copied_list.append('item 6')
print(f"\nThe original list is now - {original_list}")
print(f"The copied list is now - {copied_list}")