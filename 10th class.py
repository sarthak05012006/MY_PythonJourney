class Car:
    color = "black"
    
    def start(self):
        print("car start")
    
    def stop(self):
        print("car stop")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car1.start()
print(car1.name)
print(car1.color)# taked attribute from parent class 