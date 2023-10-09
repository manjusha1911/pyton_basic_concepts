f1=open("myfile1.txt","a")
f1.write("\nI am  learning python")
f1.close()
f1=open("myfile1.txt","r")
print(f1.read())
f1.close()

# "a" - Append - will create a file if the specified file does not exist