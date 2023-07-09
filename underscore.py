import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2


c = Circle(10)
print(c.area())


class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2


c = Circle2(10)
print(c.area())
print(c.__dict__)
# print(c._Circle2__radius)
