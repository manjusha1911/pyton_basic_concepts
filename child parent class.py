class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class child(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
p1=person("manjusha","am")
p1.printname()