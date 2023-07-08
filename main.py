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

# inheratance
class Animal:
    def __init__(self, name, age, favorite_food):
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def eat(self):
        print(f'{self.name}, aged {self.age} is eating {self.favorite_food}')

    def sleep(self):
        print(f'{self.name}, aged {self.age} is sleeping')


class Dog(Animal):
    def bark(self):
        print(f'{self.name}, aged {self.age} is barking')


class Cat(Animal):
    def meow(self):
        print(f'{self.name}, aged {self.age} is meowing')


dog = Dog('Rex', 3, 'meat')
dog.eat()
dog.sleep()
dog.bark()

cat = Cat('Tom', 5, 'fish')
cat.eat()
cat.sleep()
cat.meow()
