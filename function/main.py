# what is function?
# function is a block of code which only runs when it is called.

# type of function
# 1. Built-in function -> print(), input(), len(), sum(), max(), min(), etc.
# 2. User-defined function -> function created by user.


# def my_function():
#     print("Hello from a function")


# my_function()
# my_function()

# function with argument or parameter


# def user(name,email):
#     print("Hello "+name + " your email is "+email)

# user("Ram",'ram@gmail.com')
# user("Shyam","shyam@gmail.com")


# def even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(10)

# WAP to make a function get_result() which will take 5 
# def get_result(nep,eng,mat,sic,com):
#     total = nep+eng+mat+sic+com
#     percentage = total/5
#     if percentage >= 80:
#         grade = "A+"
#     elif percentage >= 70:
#         grade = "A"
#     elif percentage >= 60:
#         grade = "B"
#     elif percentage >= 50:
#         grade = "C"
#     else:
#         grade = "Fail"
#     print("Total:",total)
#     print("Percentage:",percentage)
#     print("Grade:",grade)


# nep =int(input("Enter nep mark: "))
# eng =int(input("Enter eng mark: "))
# mat =int(input("Enter mat mark: "))
# sic =int(input("Enter sic mark: "))
# com =int(input("Enter com mark: "))
# get_result(nep,eng,mat,sic,com)



# WAP to make function list_sum() which will take list of numbers

# def list_sum(numbers):
#     total =0
#     for num in numbers:
#         total += num

#     print("Total:",total)
# list_sum([1,2,3,4,5,6,7,8,9,10])

# WAP to make function product() which will take name, price, quantity and
#  return total price
# def product(name,price,quantity):
#     print("Product Name:",name)
#     print("Price:",price)
#     print("Quantity:",quantity)
#     total = price * quantity
#     print("Total Price:",total)

# product("Apple",100,10)

# WAP to make function my name repeat() which will take name and number

# def my_name_repeat(name,num):
#     x=1
#     while x<=num:
#         print(name)
#         x+=1

    
# my_name_repeat("Ram",5)


# function return value


# def add(x,y):
#     sm=x+y
#     sb =x-y
#     return [sm,sb]
    

# add(7,8)

# optional argument

# def user(name,age=0):
#     print(name)
#     print(age)

# user("Ram",60)

# * args -> tuple
# ** kwargs -> dictionary

# def users(*args, **kwargs):
#     print(args)
#     print(kwargs)


# users('ram','sita','gita',name='sophia',address='us')


# function scope
# global scope: variable declared outside function access anywhere
# local scope: variable declared inside function access only inside function
# x=10
# def test():
#     global x
#     x =x+50
#     print(x)

# test()
# print(x)
# nestesd function
# def outer_function():
#     def inner_function(name):
#         print("Hello",name)
    
#     return inner_function
# # outer_function()()
# a = outer_function()
# a('ram')

# x=10
# y=20
# print(x+y)
# z=x+y
# print(z)
# lambda function
# a = lambda x,y: x+y
# print(a(10,20))


# def a(x,y):
#     return x+y
# recursion function
# 5-1=4 *5 =20
# 4-1=3 *4 =60
# 3-1=2 *3 =120
# 2-1=1=120

# def fac(n):
#     if n==1:
#         return 1
#     return n*fac(n-1)

# print(fac(5))


# def test():
#     print("hello")
#     test()

# test()




# generator function
# def my_gen():
#     n=1
#     print("This is first print")
#     yield n

#     n+=1
#     print("This is second print")
#     yield n

#     n+=1
#     print("This is third print")
#     yield n

# for i in my_gen():
#     print(i)

# obj = my_gen()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(my_gen())
# print(type(my_gen))
# decorator function
# closure function
# def add(x,y):
#     return x+y

# def total(x,y,add):
#     return add(x,y)

# total(10,20,add)

# map, filter, reduce

# data =[10,20,30,40,50]
# def mul(x):
#     return x*2
# # map_data = map(lambda x:x*2,data)
# map_data = map(mul,data)
# print(list(map_data))
# new_data=[]
# for i in data:
#     new_data.append(i*2)

# print(new_data)

# data = [1,2,3,4]

# x=0
# while x<10:
#     print(data[x])
#     x+=1

# def zero_check(any_function):
#     def inner(x,y):
#         if y==0:
#             return "You can't divide by zero"
#         else:
#             return any_function(x,y)
#     return inner



# @zero_check
# def add(x,y):
#     return x+y

# print(add(10,0))


# def total(x,y):
#     """
#     This is total function
#     It will return sum of two number
    
#     """
#     return x+y


# print(total.__doc__)

# print(print.__doc__)


# data =[11,13,30,40,50]

# map_data = map(lambda x:x*2,data)

# def even(x):
#     return x*2



# import datetime

# jobs=[
#     {'title':'Software Engineer', 'company':'Google', 'exp_date':'2022-01-24'},
#     {'title':'Python developer', 'company':'ms', 'exp_date':'2025-01-24'},
#     {'title':'DevOps Engineer', 'company':'Amazon', 'exp_date':'2022-01-24'},
#     {'title':'Data Analyst', 'company':'Facebook', 'exp_date':'2022-01-24'},
#     {'title':'Data Scientist', 'company':'TCS', 'exp_date':'2024-10-24'},

# ]


# for job in jobs:
#     exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     today = datetime.datetime.now()
#     if exp_date < today:
#         exp_days = today - exp_date
#         print(f"{job['title']} job in {job['company']} is expired {exp_days.days} days ago")
#     else:
#         active_days = exp_date - today
#         print(f"{job['title']} job in {job['company']} {active_days.days} is active")


# import math

# print(dir(math))


# course ='we are learning python  11am'

# json