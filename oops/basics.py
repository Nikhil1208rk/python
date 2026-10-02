class Car:
    brand = "toyota"  # variable
    wheels = 4
    def accelerate(self):   #function
        print("accelerate")
    def brake(self):
        print("brake")
car1 = Car()
car2 = Car()
print(car1.brand)
print(car1.wheels)
print(car1.accelerate())
print(car2.brand)
print(car2.wheels)
