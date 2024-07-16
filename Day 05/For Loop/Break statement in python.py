#Exit the loop when x is "banana":
fruits=["Apple","Banana","Orange"]
for x in fruits:
    print(x)
    if x=='Banana':
       break

# Using continue statement print frults
fruit=['Mango','Cherry','Papaya']
for x in fruit:
    if x == 'cherry':
        continue
    print(x)
