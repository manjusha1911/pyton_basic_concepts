def man(n):
    return lambda n :n*10
# print(man(10)(11))
myf=man(10)
print(myf(11))