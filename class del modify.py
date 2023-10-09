class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myf(self):
        print("my name is "+self.name +" and my age is",self.age)
p1=person("manjusha",28)
p1.age=48   #update
p1.myf()



class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myf(self):
        print("my name is "+self.name +" and my age is",self.age)
p1=person("manjusha",28)
del p1.age
p1.myf()
