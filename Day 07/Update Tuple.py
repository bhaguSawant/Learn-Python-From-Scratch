# In Tuple you can not update /add/remove
# But u can convert it into list & after converting into list then u can add / remove/ delete tuple items

# Change Tuple Values
thistuple=('A','B','C','D','E')
y=list(thistuple)    #Convert it into list
print(type(y))

y[2]='Z'             #Add index 2 'Z' char in list
thistuple=tuple(y)    #Again convert it into tuple
print(y)

# Add Items
thistuple1=('A','B','c','D','E')
x=list(thistuple)             #Convert it into list
print(type(x))

x.append('zz')                     #Add zz char into list
thistuple1=tuple(x)               #Again convert it into tuple
print(x)