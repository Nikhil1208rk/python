class Student:
    def __init__(self, name, rollno , marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def alldetails(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)

s1=Student('Alex',11,89)
s2=Student('Bob',12,98)
print(s1.name)
print(s1.rollno)
print(s2.name)
print(s2.rollno)
print(s2.marks)
print(s1.marks,s2.marks)
print(s1.marks,s2.marks)
s1.name = 'nikki'
print(s1.name)
print(s1.rollno)
print(s1.alldetails())