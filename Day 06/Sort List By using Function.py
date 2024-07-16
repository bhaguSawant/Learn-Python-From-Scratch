# Sort list by using function
# 'key = function'.
# You can also customize your own function by using the keyword argument key = function.
def myfun(n):
    return abs(n-50)
thisList=[100,40,20,50,82]
thisList.sort(key=myfun)
print(thisList)

