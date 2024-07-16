#1. Create a variable named carname and assign the value Volvo to it.
carname='Volvo'
print(carname)

# 2. Create a variable named x and assign the value 50 to it.
x=50
print(x)

# 3.Display the sum of 5 + 10, using two variables: A and B.
A=5
B=10
print(A+B)

# 4.Create a variable called z, assign x + y to it, and display the result.
C=9
D=90
Z=C+D
print(Z)

# 5. Insert the correct syntax to assign values to multiple variables in one line:
E,F,G = "Orange", "Banana", "Cherry"
print(E)
print(F)
print(G)

# 6. Insert the correct keyword to make the variable x belong to the global scope.

def my_variable():
    global x
    x="Fanstatic"

my_variable()
print("global variable is " + x)