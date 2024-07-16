# Recursion
#Python also accepts function recursion, which means a defined function can call itself
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

def my_recursion(k):
  if (k > 0):
     result= k + my_recursion(k - 1)
     print(result)
  else:
      result = 0
  return result

print("\n\nRecursion Example Result")
my_recursion(5)






