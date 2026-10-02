class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,value):
        if value<0 or value>100:
            print("marks out of range")
        else:
            self.__marks = value
    def getgrades(self):
        if self.__marks>90:
            return "A"
        elif self.__marks>80:
            return "B"
        elif self.__marks>70:
            return "C"
        elif self.__marks>60:
            return "D"
        else:
            return "F"
s1 = Student("Nikhil",92)
print(s1.marks)
print(s1.getgrades())



