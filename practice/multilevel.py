class Animal:
    def __init__(self, species):
        self.species = species
    def eat(self):
        return f"{self.species} is eating."
    
class Mammal(Animal):
        def __init__(self, species, fur_colour):
             super().__init__(species)
             self.fur_colour = fur_colour
        def breathe(self):
             return f"{self.species} breathes air."
        
class Dog (Mammal):
    def __init__(self, species, fur_colour,name):
             super().__init__(species, fur_colour)
             self.name = name
    def bark(self):
             return f"{self.name} says woof!."
    
my_dog = Dog("Dog", "Brown", "Buddy")

print(my_dog.eat())
print(my_dog.breathe())
print(my_dog.bark())