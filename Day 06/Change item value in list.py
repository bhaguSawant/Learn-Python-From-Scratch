# Change Item Value
thislist=['A','B','D','E','F']
thislist[1]='Z'
print(thislist)

# Change a Range of Item Values
thislist[1:4]=["Hello","Wallo"]
print(thislist)

# Insert Items
thislist.insert(2,'Apple')
print(thislist)

# Extend list
thislist_1=['A','B','C']
thislist.extend(thislist_1)
print(thislist)