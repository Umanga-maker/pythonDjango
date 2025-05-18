# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())


class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age
    
    # setter method
    def set__age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set__age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())