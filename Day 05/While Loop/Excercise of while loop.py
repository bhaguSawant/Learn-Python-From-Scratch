#Ex 1. Print i as long as i is less than 6.

i = 1
while i < 6:
  print(i)
  i += 1

#Ex 2. Simple while-loop exercise code to build countdown clock
countdown=10
while countdown>0:
    print(countdown)
    countdown -=1

#3.Stop the loop if i is 3.
i = 0
while i < 6:
  if i == 3:
    break
  i += 1
  print(i)

#Ex:4.Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")