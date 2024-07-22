def getStudent():
    cursor.execute("""SELECT * FROM  students """)
    # print(cursor.fetchall())
    # print(cursor.fetchone())
    print(cursor.fetchmany(10))


getStudent()

# ecommerce
# products(id,name,quantity,price)