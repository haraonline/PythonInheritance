class MyClass:
    count = 0  # Class attribute

    def __init__(self):
        MyClass.count += 1  # Increment the 'count' class attribute by 1

    @classmethod
    def get_count(cls):
        return cls.count  # Return the 'count' class attribute


# Create instances of MyClass
a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()

# Call the class method
print(MyClass.get_count())  # Output: 3
