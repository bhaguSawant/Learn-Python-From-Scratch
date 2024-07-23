#You can return one line by using the "readline()" method

f=open("demofile.txt","r")
print(f.readline())


# By calling readline() two lines you can read the two first lines

# eg: Read two lines of the file
f=open("demofile.txt","r")
print(f.readline())
print(f.readline())