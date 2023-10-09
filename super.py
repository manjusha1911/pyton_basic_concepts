# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class child(person):
#     def __init__(aelf,fname,lname):
#         super().__init__(fname,lname)
# obj=child("manjusha","am")
# obj.printname()



# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class child(person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#         self.gdyear=2025
# obj=child("manjusha","am")
# obj.printname()
# print(obj.gdyear)

# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class child(person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.gdyear=year
# obj=child("manjusha","am",2025)
# obj.printname()
# print(obj.gdyear)



class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class child(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.gdyear=year
    def wlc(self):
        print("welcome "+ self.firstname,self.lastname," to the class of ",self.gdyear)
obj=child("manjusha","am",2025)
obj.wlc()