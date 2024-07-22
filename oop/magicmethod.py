# what is constructor and destructor in python
# Constructor: Constructor is a special method in python which is used to initialize
#  the object of a class.
# constructor is called when the object is created.


class Student:
    def __init__(self):
        print("This is constructor")

    def info(self):
        print("This is info method")

    def __del__(self):
        print("This is destructor")

    def __new__(cls):
        print("This is new method")
        return object.__new__(cls)
    # __str__ method is called when we use print() function
    # __repr__ method is called when we use object in interpreter
    # __add__ method is called when we use + operator

   


obj = Student()
print(dir(obj))
obj.info()