# Lambda Function is a small anonymous function
# Lambda function can take any number of arguments
# and take mutiple number of argument
# Syntax:   lambda argumemt: expression
# eg: lambda a: a+b


# Ex:1
# Add 10 argument a, & return the result
x=lambda a: a+10
print(x(5))

# Ex:2
# Use that function definition to make a function that always doubles the number you send in:

def my_function(n):
    return lambda a:a*n
my_doubler =my_function(3)       # n=3 considered
print(my_doubler(11))            # Here a= 11 Considered


# Ex:3
# Summarize argument a, b, and c and return the result:
x = lambda a,b,c: a+b+c
print(x(3,4,7))