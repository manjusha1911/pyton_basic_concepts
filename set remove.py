a={"apple", "banana", "cherry"}
a.remove("banana")
print(a)

# a.remove("kiwi")   
# print(a)  #KeyError: 'kiwi'

a={"apple", "banana", "cherry"}
a.discard("banana")
print(a)
a.discard("kiwi")  # will NOT raise an error.
print(a)

a={"apple", "banana", "cherry"}
a.pop()
print(a)


a={"apple", "banana", "cherry"}
print(a.pop())

a={"apple", "banana", "cherry"}
# a.clear()
print(a)

a={"apple", "banana", "cherry"}
del a
print(a)