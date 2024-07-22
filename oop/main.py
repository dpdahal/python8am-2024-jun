# What is oop?
# OOP stands for Object-Oriented Programming.
# what is object?
# An object is an instance of a class.
# what is class?
# A class is a blueprint for the object.

# name ='ram' # variable
# def test(): # function
#     print('hello')


# class Students:
#     name ='ram'

#     def info(self):
#         print("I am info method")


# obj = Students()
# print(obj.name)
# obj.info()

# class Calculator:
#     def add(self,x,y):
#         return x+y
    
#     def sub(self,x,y):
#         return x-y
    
#     def mul(self,x,y):
#         return x*y 
    

# obj = Calculator()
# print(obj.add(10,20))
# print(obj.sub(10,20))
# print(obj.mul(10,20))

# class User:
#     name ='ram'

#     def info(self):
#         # obj =User()
#         print(self.name)


# obj = User()
# obj.info()

# class SIP:

#     def take_value(self):
#         p =int(input("Enter the principal amount: "))
#         t=int(input("Enter the time: "))
#         r = int(input("Enter the rate: "))
#         return [p,t,r]

#     def caluclate(self):
#         p,t,r = self.take_value()
#         return p*t*r/100

#     def display(self):
#         print(self.caluclate())


# obj = SIP()
# obj.display()

class Product:
    productData=['laptop','mobile','tv']
    def add(self,new_product):
        pass
    def show(self):
        pass

    def update(self,old_product,new_product):
        pass

    def delete(self,product):
        pass