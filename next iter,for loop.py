class person:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            self.a+=1
            return self.a
        else:
            raise StopIteration
mycls=person()
myiter=iter(mycls)
for i in myiter:
    print(i)