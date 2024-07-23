# It is always good pratice to close the file
#eg: Close the file when u r finish the with it

f=open("demofile.txt","r")
print(f.readline())
f.close()