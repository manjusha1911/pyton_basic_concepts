def  myf():
    x=100
    def myf2():
        print(x)
    myf2()
myf()



def myf():
    x=20
    print(x)
myf()
# print(x)  #error

def myf():
    global x
    x=10
    print(x)
myf()
print(x)


x=100
def  myf():
    print(x)
myf()
print(x)


# x=100
def  myf():
    x=200
    print(x)
myf()
print(x)
