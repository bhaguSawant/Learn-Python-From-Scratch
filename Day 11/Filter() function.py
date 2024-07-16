# Filter() function are used to filter the any values in list

# Ex:1
# Filyer the array & return a new aeeay with only the values equal to or above 18:

age=[20,12,18,24,32]
def My_fun(x):
    if x<18:
        return False
    else:
        return True
adult = filter(My_fun,age)
for x in adult:
    print(x)