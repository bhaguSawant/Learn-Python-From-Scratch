# Write to an exisisting file

# f=open("demofile1.txt","x")   # Create new file
f=open("demofile1.txt","a")
f.write("My new content is my introduction")
f.close()


# Open and read the file content
f=open("demofile1.txt","r")
print(f.read())