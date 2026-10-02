class BankAccount:
    def __init__(self,name,__balance):
        self.name = name
        self.__balance = __balance

    def deposit(self,amount):
        self.__balance += amount
        print("deposit ",amount)
        print("updated-balance",self.__balance)
    def withdraw(self,amount):
        if amount > self.__balance:
            print("INsufficient balance")
        else:
            self.__balance -= amount
            print("withdraw ",amount)
            print("updated-balance",self.__balance)
    def display(self):
        print("name",self.name)
        print("current balance",self.__balance)

b1 = BankAccount("Nikhil",1000)
b1.deposit(1500)
b1.withdraw(1200)
b1.display()

