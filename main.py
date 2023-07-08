# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# inheritance
class Animal:
    def __init__(self, name: str, age: int, favorite_food: str):
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def eat(self):
        print(f'{self.name}, aged {self.age} is eating {self.favorite_food}')

    def sleep(self):
        print(f'{self.name}, aged {self.age} is sleeping')

    def move(self):
        print(f'{self.name}, aged {self.age} is moving at 10 km/h')


class Dog(Animal):
    def bark(self):
        print(f'{self.name}, aged {self.age} is barking')


class Cat(Animal):
    def meow(self):
        print(f'{self.name}, aged {self.age} is meowing')


class panther(Animal):
    def roar(self):
        print(f'{self.name}, aged {self.age} is roaring')

    def move(self):
        print(f'{self.name}, aged {self.age} is moving at 80 km/h')


class Owl(Animal):
    def __init__(self, name, age, favorite_food, turn_head_360):
        super().__init__(name, age, favorite_food)
        self.turn_head_360 = turn_head_360

    def sleep(self):
        super().sleep()
        print("am also doing some important things while am sleeping ...")

    def move(self):
        print(f'{self.name}, aged {self.age} is flying at 100 km/h')


dog = Dog('Rex', 3, 'meat')
dog.eat()
dog.sleep()
dog.bark()
dog.move()
print('------------------')

cat = Cat('Tom', 5, 'fish')
cat.eat()
cat.sleep()
cat.meow()
cat.move()
print('------------------')

panther = panther('Blacky', 7, 'meat')
panther.eat()
panther.sleep()
panther.roar()
panther.move()
print('------------------')

owl = Owl("Huntsman", 2, "worms", True)
owl.eat()
owl.sleep()
owl.move()
print(f'Turn head 360: {owl.turn_head_360}')
print('------------------')