class Person:
    def __init__(self,name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
    def greet (self):
        return f"Hello, my name is {self.name}."
    
class Employee:
    def __init__(self, employee_id, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id
    def get_id(self):
        return f"My employee ID is {self.employee_id}."
    
class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name=name, employee_id=employee_id)
        self.department= department
    def show_details(self):
        return f"{self.greet()} {self.get_id()} I'm a Manager in the {self.department} department."
    
manager = Manager("David", "E2345", "Marketing")

print(manager.greet())
print(manager.get_id())
print(manager.show_details())

