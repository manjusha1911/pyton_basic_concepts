class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")
class car(vehicle):
    pass
class boat(vehicle):
    def move(self):
        print("sail")
class plane(vehicle):
    def move(self):
        print("fly")
car1=car("bmw","lambogini")
boat1=boat("ibiza","tourning 20")
plane1=plane("indigo","747")
for i in(car1,boat1,plane1):
    print(i.brand)
    print(i.model)
    i.move()
