class Car:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.__speed = speed
    def accelerate(self,amount):
        self.__speed += amount
        print("accelerate",self.__speed)
    def brake(self,amount):
        self.__speed -= amount
        print("brake",self.__speed)
    @property
    def speed(self):
        print( self.__speed)

c1 = Car("toyota","fortuner",50)
c1.accelerate(60)
c1.brake(50)