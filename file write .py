f1=open("myfile2.txt","w")
f1.write("I have completed python, html, css")
f1.close()
f1=open("myfile2.txt","r")
print(f1.read())

# "w" - Write - will create a file if the specified file does not exist