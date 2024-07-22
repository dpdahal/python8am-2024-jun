# print("Hello python")
# print("Hello python")
# print("Hello python")
# print("Hello python")
# print("Hello python")
# print("Hello python")
# print("Hello python")


# what is loop
# loop is a control structure that repeats a group
#  of statements a specified number of times



# types of loop
# for loop -> list, tuple, set, dictionary, string, range
# while loop -> condition based loop

# x=1
# while x<=10:
#     print(x)
#     x+=1
# nested loop

# WAP to print 10 to 1 using while loop
# WAP to print total even number between 1 to 100
# WAP to print your name 10 times

# students=[]

# num = int(input("Enter the number of students: "))
# x=1
# while x<=num:
#     name=input("Enter the name of student: ")
#     students.append(name)
#     x+=1


# a =0
# while a<len(students):
#     print(students[a])
#     a+=1

# x=1
# while x<=50:
#     if x==22 or x==25 or x==33 or x==44 or x==49:
#         print(x,end=',')
#     x+=1
    




# find_number=[22,25,33,44,49]
# x=0
# while x<=50:
#     if x in find_number:
#         print(x)
#     x+=1


# numbers=[10,20,30,40,50]
# new_list=[]
# total =len(numbers)
# x=0
# while x<total:
#     new_list.append(numbers[x]*2)
#     x+=1

# print(new_list)

# data=[12,13,34,65,78,19,18,17,16,15]
# 12,34,78,18,16

# WAP to print 1 to 100 using while loop and divisible by 3 and 5

# only print name lenght is greater than 4
# nn =[12,13,12,14,15,17,17]
# remove duplicate number 

# students=['ram','shyam','sitaram','sophia','gita','madan']

# for name in students:
#     print(name)


# data=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# # print(data[2][1])

# for row in data:
#     for col in row:
#         print(col)


# products=[
#     {'name':'apple','price':200,'qty':10},
#      {'name':'banana','price':100,'qty':20},
#     {'name':'mango','price':300,'qty':5},
#     {'name':'orange','price':150,'qty':15}
   
# ]

# # product_name  price  qty  total
# print("Product Name \t Price \t Qty \t Total")
# for product in products:
#     total = product['price']*product['qty']
#     print(f"{product['name']} \t\t {product['price']} \t {product['qty']} \t {total}")


# category=[
#     {'id':1,'name':'Electronics'},
#     {'id':2,'name':'Clothing'},
#     {'id':3,'name':'Furniture'},
#     {'id':4,'name':'Grocery'}
# ]

# products=[
#     {'name':'laptop','price':200,'qty':10,'category':1},
#     {'name':'shirt','price':100,'qty':20,'category':2},
#     {'name':'table','price':300,'qty':5,'category':3},
#     {'name':'apple','price':150,'qty':15,'category':4},
#     {'name':'mobile','price':200,'qty':10,'category':1},
#     {'name':'jeans','price':100,'qty':20,'category':2},
#     {'name':'chair','price':300,'qty':5,'category':3},
#     {'name':'banana','price':150,'qty':15,'category':4},
#     {'name':'computer','price':200,'qty':10,'category':1},
# ]


# for cat in category:
#     print(cat['name'])
#     for product in products:
#         if cat['id']==product['category']:
#             total = product['price']*product['qty']
#             print(f"\t{product['name']} \t {product['price']} \t {product['qty']} \t {total}")