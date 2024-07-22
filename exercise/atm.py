print("==============Welcome to ATM==============")
pin = int(input("Enter your pin: "))

if pin==1234:
    amount=10000
    print("1. Withdraw")
    print("2. Balance Enquiry")
    option = int(input("Enter your option: "))
    if option==1:
        new_amount = int(input("Enter the amount to withdraw: "))
        if new_amount>amount:
            print("Insufficient balance")
        else:
            rem = amount-new_amount
            print("Remaining balance is: ",rem)
            print("Withdrawn amount is: ",new_amount)
    elif option==2:
        print("Your balance is: ",amount)
    else:
        print("Invalid option")
        exit()

else:
    print("Invalid pin")
    exit()



# students_list = ['ram','sita']
# print("1. Add student")
# print("2. Remove student")
# print("3. Display students")
# print("4. Exit")

# loop: while, for