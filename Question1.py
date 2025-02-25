class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"car deteils:{self.brand} {self.model} {self.year}")

#creating an object of the car class
class display(car):
    def __init__(self, brand, model, year):
        car.__init__(self, brand, model, year)
        my_car = car("Mercedez", "c63", 2019)
        my_car.display()