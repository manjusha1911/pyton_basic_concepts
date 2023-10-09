def myf(l):
    return len(l)
l=['Ford', 'Mitsubishi', 'BMW', 'VW']
l.sort(reverse=True,key=myf)
print(l)