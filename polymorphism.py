class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        print(self.brand,self.model)
    def move(self):
        print("Fly")

car1=Car("bmw","lambogini")
boat1=Boat("Ibiza","touring 20")
plane1=Plane("Indigo","747")
for i in (car1,boat1,plane1):
    print(i.brand)
    i.move()
