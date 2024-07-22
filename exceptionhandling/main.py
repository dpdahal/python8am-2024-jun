# try:
#     print(10/2)
# except Exception as e:
#     print("Error: ", e)

# print("hello python")


def add(x,y):
    if y == 0:
        raise Exception("y should not be zero")
    return x+y


try:
    print(add(10,9))
except Exception as e:
    print("Error: ", e)

finally:
    print("finally block")