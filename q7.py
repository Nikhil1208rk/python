class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Developer(Employee):
    def __init__(self,name , salary,language):
        super().__init__(name,salary)
        self.language = language
    def work(self):
        print(self.name,"is working in ",self.language)

d1 = Developer("Nikhil", 50000, "Python")

d1.display()
d1.work()

