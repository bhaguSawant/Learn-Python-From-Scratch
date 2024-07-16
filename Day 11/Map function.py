# Map function
# Map function execute a special function
def my_func(n):
    return  len(n)
x= map(my_func,('Apple','Banana'))
print(x)
print(list(x))         ## Covert the map into a list for readabality

# Ex:2
def my_func1(a,b):
    return  a+b
x= map(my_func1,('Apple','Banana','Grapes'),('Orange','Cherry','Mango'))
print(x)
print(list(x))  ## Convert into a list
