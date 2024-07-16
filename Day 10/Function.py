#Function
# Function can define by using def keyword

# EX:1
def my_function():
    print("Hello")

my_function()        #Call the function

# Ex:2
# Passing Arguments
def my_Function(fname):
    print(fname +"Reference")     # Calling  Argument

my_Function("my name")

# Ex:3
# This function expects 2 arguments, and gets 2 arguments:
def my_function1(fname, lname):
  print(fname + " " + lname)

my_function1("Emil", "Refsnes")



# Arbitrary Arguments, *args
def my_new_function(*kid):
    print("The smallest child is :"+kid[1])

my_new_function("Meera",'Jeevan','Bharti')

# Return value
def my_function2(x):
  return 4 * x
print(my_function2(4))
print(my_function2(2))
print(my_function2(7))