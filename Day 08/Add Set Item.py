#Add an item to a set, using the add() method
Myset={'A','B','C','D','E'}
Myset.add('Z')
print(Myset)

# Add elements from tropical into thisset:
thisset={"Latur","Udgir","Mumbai"}
tropical={'A','B','Z'}

thisset.update(tropical)
print(thisset)

# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)