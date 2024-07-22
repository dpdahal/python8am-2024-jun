# class User:
#     x=10

#     @property
#     def test(self):
#         return ("Hello test")
    

# obj = User()
# print(obj.test)

# what is decorator?
# Decorators are very powerful and useful tool in Python since it
#  allows programmers to modify the behavior of function or class.
#  Decorators allow us to wrap another function in order to extend
#  the behavior of the wrapped function, 
# without permanently modifying it.

# list of decorators
# @classmethod
# @staticmethod
# @property

# what is classmethod decorator?
# A class method is a method which is bound to the class and 
# not the object of the class.

# class Student:
#     name = "Rahul"
#     age = 20

#     @classmethod
#     def printDetails(cls):
#         return f"Name is {cls.name} and age is {cls.age}"

# what is staticmethod decorator?
# A static method does not receive an implicit first argument.
#  A static method is also a method which is bound to the class
#  and not the object of the class.


# class User:
#     x = 10

#     @staticmethod
#     def test():
#         print("Hello test")
    
# User.test()
# obj = User()
# print(obj.test())


# what is property decorator?
# Python @property is one of the built-in decorators.
#  @property decorator is used to create a property of a class.
#   The property created can be accessed as an attribute instead of a method.