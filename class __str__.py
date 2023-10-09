# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1)  
'''
# O/P
<__main__.Person object at 0x15039e602100>
'''

class person:
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}{self.age}"
p1=person("manjusha ",28)
print(p1)