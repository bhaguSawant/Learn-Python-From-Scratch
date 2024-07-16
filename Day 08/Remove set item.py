#To remove an item in a set, use the remove(), or the discard() method.

# Remove "banana" by using the remove() method:
thisset={'Banana','Kiwi','Orange'}
thisset.remove('Banana')
print(thisset)

# Remove "banana" by using the discard() method:
thisset_1={'Banana','Kiwi','Orange'}
thisset_1.discard('Banana')
print(thisset_1)

# Remove a random item by using the pop() method:
thisset_1={'Banana','Kiwi','Orange'}
thisset_1.pop()
print(thisset_1)

# The clear() method empties the set:
thisset_2={'Banana','Kiwi','Orange'}
thisset_2.clear()
print(thisset_2)

# The del keyword will delete the set completely:
# thisset_3={'Banana','Kiwi','Orange'}
# del thisset_3
# print(thisset_3)           # It gives error when delete the set

# Loop Items
# Loop through the set, and print the values:
thisset_1={'a','b','c','d'}
for x in thisset_1:
    print(x)
