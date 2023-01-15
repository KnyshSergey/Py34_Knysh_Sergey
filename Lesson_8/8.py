import time

class Auto:
    def __init__(self, brand, age, mark, color="red", weight=1500):

        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(self.age)

# truck = Auto("BMW", 2, "X7", color="Black", weight=2500)
#
# truck.move()
# truck.stop()
# truck.birthday()

# print(truck)

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="silver", weight=2300):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load
    def move(self):
        super().move()
        print("Attention")
    def load(self):
        time.sleep(1)
        print("Loaded")
        time.sleep(1)




class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="silver", weight=2300):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")

truck1 = Truck("Mercedes-Benz", 12, "B259", 8000)
car1 = Car("Ferrary", 4, "Enzo", 416, color="red", weight=1650)
print(truck1.brand)
print(car1.mark)
# truck1.load()
car1.move()

