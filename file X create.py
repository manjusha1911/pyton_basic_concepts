f1=open("myfile3.txt","x")
f1.write("sai ram\njai sree ram\nhar har mahadev\njai sri krishna")
f1.close()
f1=open("myfile3.txt","r")
print(f1.read())


# "x" - Create - will create a file, returns an error if the file exist