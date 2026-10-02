class Student:
    def __init__(self,name,__roll_no,__marks):
        self.name = name
        self.__roll_no = __roll_no
        self.__marks = __marks
    @property
    def roll_no(self):
        return self.__roll_no
    @property
    def marks(self):
        return self.__marks
    def display(self):
        print(self.name,self.roll_no,self.marks)

s1=Student('nikhil',101,85)
s2=Student('vekii',2,5)
s1.display()


