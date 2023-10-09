l= ["a", "b", "a", "c", "c"]
b=[]
for i in l:
    if i not in b:
        b.append(i)
print(b)   #['a', 'b', 'c']



my=list(dict.fromkeys(l))
print(my)  ##['a', 'b', 'c']

print(dict.fromkeys(l))  #{'a': None, 'b': None, 'c': None}