# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.__age = age
#         self._salary = salary
#     def displayEmployee(self):
#         print("Name :", self.name,",age:", self.__age, ",salary:", self._salary )

# e1=Employee("Bhavana", 24, 10000)


# print(e1.name)
# print(e1._salary)
# print(e1.__age)

# DUCK TYPING
class Duck:
    def sound(self):
        return "Quack, quack!"
    
class AnotherBird:
    def sound(self):
        return "I'm similar to a duck!"
    
def makeSound(duck):
    print(duck.sound())

# creating instances
duck=Duck()
AnotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(AnotherBird)