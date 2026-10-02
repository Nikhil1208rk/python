class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno

    def study(self):
        print("Student is studying")


s1 = Student("Nikhil", 19, 101)

s1.display()
print("Roll No:", s1.rollno)
s1.study()
