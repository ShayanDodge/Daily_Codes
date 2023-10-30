class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

a = MyClass(1)
b = MyClass(2)
c = a + b
print(c.value)  # Output: 3

