# process of binding data and methods together and
# restrict direct acess to data
# to make anything private use __ before variable
# class BankAccount:
#     def __init__(self,name,__balance):
#         self.name = name
#         self.__balance = __balance
#     def getbalance(self):
#         return self.__balance
#     def deposit(self,amount):
#         self.__balance += amount
#         print(self.__balance)
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("Not enough money")
#         else:
#             self.__balance -= amount
#             print(self.__balance)
# s1 = BankAccount('nikki',100)
# s2 = BankAccount('vivek',200)
# print(s1.name,s1.getbalance())
# print(s2.name,s2.getbalance())
# a = s1.deposit(1000)
# print(a)
# print(s1.name,s1.getbalance())


# to access the private variable data without calling the function use:-
# @property

class Marks:
    def __init__(self,name,__marks):
        self.name = name
        self.__marks = __marks
    @property
    def marks(self):
        return self.__marks

s1=Marks('nikki',100)
print(s1.marks)



