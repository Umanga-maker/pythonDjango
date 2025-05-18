class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def honk(self):
        print("Beep Beep!")

    def brake(self):
        print("brake")

my_car = Car("Red", "Toyota")
my_car.honk()

my_car.brake()
