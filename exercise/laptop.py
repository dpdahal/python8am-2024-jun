print("===============Computer bazar===============")
print("1. Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:50000)")

product_name=""
dell_price=0
toshiba_price=0
mac_price=0
quantity=0

question=int(input("Enter the product number: "))

if question==1:
    product_name="Dell"
    quantity=int(input("Enter the quantity: "))
    dell_price=20000*quantity
elif question==2:
    product_name="Toshiba"
    quantity=int(input("Enter the quantity: "))
    toshiba_price=30000*quantity
elif question==3:
    product_name="Mac"
    quantity=int(input("Enter the quantity: "))
    mac_price=50000*quantity
else:
    print("Invalid product number")
    exit()


print("Delivery Option: 1. Home(Rs:1000)  2.Pickup(Rs:0)")
delivery_price=0
delivery_option=int(input("Enter the delivery option: "))
if delivery_option==1:
    delivery_price=1000


print("Packing Option: 1. Plastic Bag(Rs:1000)  2.Bag (Rs:2000) 3. Gift Box(Rs:5000)")
packing_price=0
packing_option=int(input("Enter the packing option: "))
if packing_option==1:
    packing_price=1000
elif packing_option==2:
    packing_price=2000
elif packing_option==3:
    packing_price=5000

total_price=dell_price+toshiba_price+mac_price
tax_amount=0
print("Location 1. KTM(rs:13%) 2. Lalitpur(rs:0%) 3. Bhaktapur(rs:0%)")

location =int(input("Enter the location: "))
if location==1:
    tax_amount=total_price*0.13


grand_total=total_price+delivery_price+packing_price+tax_amount

print("===============Invoice===============")
print("Product Name: ",product_name)
print("Quantity: ",quantity)
print("Total Price: ",total_price)
print("Delivery Price: ",delivery_price)
print("Packing Price: ",packing_price)
print("Tax Amount: ",tax_amount)
print("Grand Total: ",grand_total)
print("===============Thank you===============")