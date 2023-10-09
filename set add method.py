s={"apple", "banana", "cherry", True, 1, 2}
# s.add("Sairam")
print(s)



a={"apple", "banana", "cherry"}
b = {"pineapple", "mango", "papaya"}
a.update(b)
print(a)

a={"apple", "banana", "cherry"}
b=["pineapple", "mango", "papaya"]
a.update(b)
print(a)

a={"apple", "banana", "cherry"}
b=("pineapple", "mango", "papaya")
a.update(b)
print(a)