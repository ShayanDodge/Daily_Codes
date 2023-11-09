class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

my_object_1 = MyClass("I am an instance variable")
my_object_2 = MyClass("I am another instance variable")

print(MyClass.class_variable)      # Output: I am a class variable
print(my_object_1.class_variable)  # Output: I am a class variable
