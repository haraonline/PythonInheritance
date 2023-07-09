class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # def __str__(self):
    #     return f'{self.color} {self.make} {self.model} ({self.year})'
    #
    # def __repr__(self):
    #     return f'{self.color} {self.make} {self.model} ({self.year})'


my_car = Car('BMW', 'X5', 2020, 'red')
print(my_car)
print(my_car.__dict__)
print(my_car.__repr__())
print(my_car.__str__())

