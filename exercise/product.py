# print("=============Product Module=============")
# num = int(input("Enter number of products: "))
# product_list = []
# x=1
# while x<=num:
#     print(f"=============Product No: {x}=============")
#     name = input("Enter product name: ")
#     price = int(input("Enter product price: "))
#     quantity = int(input("Enter product quantity: "))
#     total = price*quantity
#     p_data={"name":name,"price":price,"quantity":quantity,"total":total}
#     product_list.append(p_data)

#     x+=1



# print("Product Name\t Price \t Quantity \t Total")
# for product in product_list:
#     print(f"{product['name']}\t\t{product['price']}\t{product['quantity']}\t\t{product['total']}")


# 1*1=1
# 1*2=2
# 1*3=3


students=[
    {'name':'ram','gender':'male','stauts':True},
    {'name':'sita','gender':'female','stauts':False},
    {'name':'rita','gender':'female','stauts':True},
    {'name':'laxmi','gender':'female','stauts':False},
    {'name':'gopal','gender':'male','stauts':False},
]
total_students=len(students)
total_male=0
total_female=0

for student in students:
    if student['gender']=='male':
        total_male+=1
    else:
        total_female+=1
print(f"Total Students: {total_students}")
print(f"Total Male: {total_male}")
print(f"Total Female: {total_female}")

# total active students
# total inactive students
# total active male and inactive
# total active female and inactive
# WAP to enter name and find students 