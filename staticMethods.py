"""
1. Static methods in Python are methods that belong to a class rather than an instance of a class. They can be
called on the class itself, not on an instance of the class.

2. They are defined using the @staticmethod decorator above the method, and they do not take a 'self' parameter like
instance methods do. Because they don't have access to 'self', they can't modify the object's state (though they can
modify class state).

3. Static methods do not have access to any other methods in the same class unless they're passed in as parameters.

4. They are used when a method doesn't need to access any instance or class-specific data, but still belongs to the
class because of some semantic relationship.

5. In general, static methods can be used to create utility functions that perform a specific task relevant to the
class, but don't need to interact with the class or instance itself.

6. A static method is bound to the class and not the instance of the class. This means that you can call a static
method without creating an instance of the class.

7. Since they don't take 'self' or 'cls' parameters, they can't be overridden by subclasses.

"""


class MyClass:
    class_attribute = 10

    def __init__(self, name):
        self.name = name

    @staticmethod
    def say_hello():
        print("Hello there!")


MyClass.say_hello()  # Hello there!
