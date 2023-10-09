def myl(l):
    print(len(l))
l=['Ford', 'Mitsubishi', 'BMW', 'VW']
myl(l)


def myl(l):
    return len(l)
l=['Ford', 'Mitsubishi', 'BMW', 'VW']
# l.sort(reverse=True) #descending order
l.sort()  #ascending order
print(l)
