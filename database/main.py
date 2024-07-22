import sqlite3
conn = sqlite3.connect('college.sqlite3')
cursor = conn.cursor()
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL          
                   )""")
    conn.commit()
create_table()
def insert(name, email, address):
    cursor.execute(
        """
        INSERT INTO students (name,email,address) VALUES (?, ?, ?)
        """, (name, email, address))
    conn.commit()
    print('Data inserted successfully')
# name = input('Enter your name: ')
# email = input('Enter your email: ')
# address = input('Enter your address: ')
# insert(name, email, address)
