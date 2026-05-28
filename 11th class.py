class Car:
    color = "black"
    def __init__(self,type):
        self.type = type
    
    def start():
        print("car start")
    
    def stop():
        print("car stop")

class ToyotaCar(Car):

    def __init__(self, name, type):
        super.__init__(type)#super method is used to access methods of the parent class
        self.name = name


car1 = ToyotaCar("URBAN_CRUISER","electric")
print(car1.name)
print(car1.color)
print(car1.type)