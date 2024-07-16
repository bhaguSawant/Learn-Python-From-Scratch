# Join Two List
# One of the easiest ways are by using the + operator.

list_1=['Bhagyashree','Anjana','Rohit']
list_2=[30,40,50]
new_list = list_1 + list_2
print(new_list)

# Or
# Another way to join two lists is by appending all the items from list2 into list1, one by one:
# Ex:1
list_x=['A','B','C']
list_y=['a','b','c']
list_x.append(list_y)
print(list_x)

# Ex:2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)