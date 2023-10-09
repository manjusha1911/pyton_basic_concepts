def manjusha(l):
    b=[]
    for i in l:
        if i not in b:
            b.append(i)
    print(b)
manjusha(['a', 'b', 'c'])



def manjusha(l):
    u=list(dict.fromkeys(l))
    print(u)
manjusha(['a', 'b', 'c'])



def manjusha(l):
    return list(dict.fromkeys(l))
l=manjusha(['a', 'b', 'c'])
print(l)


#O/P  ['a', 'b', 'c']