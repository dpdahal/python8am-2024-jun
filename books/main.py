import os

if not os.path.exists('users.txt'):
    handle=open('users.txt','w')
    handle.close()

books=[
    {'id':1,'name':'python','price':100},
    {'id':2,'name':'java','price':200},
    {'id':3,'name':'c++','price':300},
    {'id':4,'name':'c#','price':400},
    {'id':5,'name':'php','price':500},
]

def register():
    print("=====Register=====")
    username = input('Enter username: ').strip()
    
    if username in open('users.txt').read():
        print('User already exists')
        exit()
    password=input('Enter password: ').strip()
    confirm_password = input('Confirm password: ').strip()
    if password!=confirm_password:
        print('Passwords do not match')
        exit()

    handle=open('users.txt','a')
    handle.write(f'{username},{password}\n')
    handle.close()
    print('User registered successfully')



def login():
    print("=====Login=====")
    username = input('Enter username: ').strip()
    password=input('Enter password: ').strip()
    users = open('users.txt').readlines()
    is_login=False
    for user in users:
        user=user.strip().split(',')
        if user[0]==username and user[1]==password:
            is_login=True
    if is_login:
        print(f"=====Welcome: {username}=====")
        print("Id\t Name\t Price")
        for book in books:
            print(f"{book['id']}\t {book['name']}\t {book['price']}")
    else:
        print('Invalid username or password')
        exit() 
            
            


question = input('Do you have an account? (y/n): ').strip()
if question=='y':
    login()

else:
    register()
    