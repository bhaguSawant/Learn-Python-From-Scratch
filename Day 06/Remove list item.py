# Remove list item
this_list=['x','y','z','A']
this_list.remove('x')
print(this_list)

# Remove specified index item
this_list.pop(2)
print(this_list)

# The del keyword also removes the specified index:
del this_list[1]
print(this_list)

# The del keyword can also delete the list completely.
# del this_list
# print(this_list)

# Clear the list by using clear()method
this_list.clear()
print(this_list)