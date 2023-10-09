a=["man","honey","nany"]
new=["manjusha" for k in a ]
print(new)
# nl=[i for i in a if "y" in i]
# print(nl)

# n=[j for j in a if j!="honey"]
# print(n)


##nl=[i for i in a]
nl=[x for x in range(1,11)]
print(nl)

nl2=[i for i in range(1,11)if i<=5]
print(nl2)
nl=[y.upper() for y in a]
print(nl)


#if else..........................
a=["manjusha","honey","nany"]
newl=[x if x!="manjusha" else "vasu" for x in a]
print(newl)