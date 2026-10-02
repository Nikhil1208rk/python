# where child class acquire parent class property

# class Animal:             #parent class
#     def eat(self):
#         print('eat')
#
# class Dog(Animal):
#     def bark(self):
#         print('bark')
# class Fish(Animal):
#     def swim(self):
#         print('swim')
# class Bird(Animal):
#     def fly(self):
#         print('fly')
#
#
# bird1 = Bird()
# bird1.eat()
# bird1.fly()


class Company:
    def __init__(self,companyName):
        self.companyName = companyName
    def address(self):
        print("noida")
class Employee(Company):
    def __init__(self,name,id,companyName):
        self.name=name
        self.id=id
        super().__init__(companyName)  # it used to access constructor and methods from parent class
    def work(self):
        print("software engg.")







