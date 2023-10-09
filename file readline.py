f1=open("myfile1.txt","r")
print(f1.readline())
print(f1.readline())
print(f1.readline())
f1.close()

#print line by line space will be given line by line


# O/P
'''
my name is manjusha

i am from andhra pradesh

i am 22 yrs old
'''


f=open("myfile1.txt","r")
for i in f:
    print(i)

# O/P
'''
my name is manjusha

i am from andhra pradesh

i am 22 yrs old
'''
