class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.rollno = rollno

    def display(self):
        super().display()
        print("Roll No:", self.rollno)


class CollegeStudent(Student):
    def __init__(self, name, rollno, branch):
        super().__init__(name, rollno)
        self.branch = branch

    def display(self):
        super().display()
        print("Branch:", self.branch)


s1 = CollegeStudent("Nikhil", 101, "CSE")

s1.display()
