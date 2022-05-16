# EXERCISE 4.10
# 4-10. Slices: Using one of the programs you wrote in this chapter, add
# several lines to the end of the program that do the following:
#
# Print the message "The first three items in the list are" then use a slice to
# print the first three items from that program’s list.
item_list = [f"Item {i}" for i in range(1,11)]
print(f"The first three items are - {item_list[:3]}")
# Print the message "The first three items from the middle of the list are"
# then use a slice to print the first three items from that program’s list.
print(f"Three items from the middle of the list are - {item_list[3:6]}")
# Print the message "The last three items in the list are" then use a slice to
# print the first three items from that program’s list.
print(f"The last three items on the list are - {item_list[7:10]}")