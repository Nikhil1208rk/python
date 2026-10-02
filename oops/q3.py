class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            print("Invalid salary")
        else:
            self.__salary = new_salary
            print("New salary:", new_salary)


e1 = Employee("Gustavo", 10000)

# Get salary
print("Current salary:", e1.salary)

# Update salary
e1.salary = 15000
print("Current salary:", e1.salary)

# Try invalid salary
e1.salary = -5000
print("Current salary:", e1.salary)