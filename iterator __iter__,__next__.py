class myn:
    def __iter_(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
mycls=myn()
myi=iter(mycls)
print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))
print(next(myi))