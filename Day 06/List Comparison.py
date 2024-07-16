#List Comaparion using
# Check B charachter in which fruits then print the newlist of B fruit name
fruits=['Apple','Mango','Banana','Strawbwrry','Cherry']
newlist=[]
for x in fruits:
    if 'B' in x:
        newlist.append(x)

print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
fruits=['Apple','Mango','Banana','Strawbwrry','Cherry']
newlist=[x for x in fruits if x!='Apple']
print(newlist)

# Set the value in list Upper case
list1=['Bhagyashree','Anjana']
newlist=[x.upper()for x in list1]
print(newlist)

# Set all values in the new list to 'hello':
Fruit=['Orange','Papaya','Lichi']
newlist=['Hello' for x in Fruit]
print(newlist)

# Return "orange" instead of "banana":
Fruit=['Orange','Papaya','Lichi']
newlist=[x if x!='Orange' else 'Banana' for x in Fruit]
print(newlist)



