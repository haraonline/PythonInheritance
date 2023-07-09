class Person:
    instance_count = 0  # count of Person instances created

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.instance_count += 1  # increment count of instances

    def __str__(self):
        return f'{self.name}, {self.age}, years old'


p1 = Person('John', 32)
p2 = Person('Jane', 28)
p3 = Person('Bob', 45)
p4 = Person('Mary', 38)
print(p1)
print(p2)
print(p3)
print(p4)
print(f'Total instance created = {Person.instance_count}')
