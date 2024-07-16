#1. Use the len function to print the length of the string.
a="Hello Python"
print(len(a))

# 2.Get the first character of the string txt.
b="Hello Python"
print(b[0])

#3. Get the characters from index 2 to index 4 (llo).
c="Hello Bhagyashree"
print(c[2:5])

#4. Return the string without any whitespace at the beginning or the end.
d=" Hello Bhagyashree "
print(d.strip())

#5. Convert the value of txt to upper case.
e="hello"
print(e.upper())

#6.Convert the value of txt to lower case.
f="HELLO"
print(f.lower())

#7. Replace the character H with a J.
g="Hello"
print(g.replace('H','J'))

#8. Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = f"My name is John, and I am {age}"
print(txt.format(age))
