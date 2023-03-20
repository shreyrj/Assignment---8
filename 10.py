class MyClass:
pass
obj = MyClass()
# Get the class of the object using type()
class_name = type(obj).__name__
print("Class name:", class_name)