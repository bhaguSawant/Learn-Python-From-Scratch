#Global Variable tht are created OUTSIDE the function
# EX:

x="Awesome"
def my_function():
    x="Good"
    print("Python is "+ x)
my_function()           # Here we call the inside function variable x="Good"
print("Bhagyashree is " + x)  #Here we call outside function variable x="Awesome