f=open("myfile1.txt","r")
print(f.read())  # will read all lines
print(f.read(5))  #first 5 letters will be printed
f.close()