# # what is file handling?
# # File handling is an important part of any web application.
# # Python has several functions for creating, reading, updating, and deleting files.

# # file modes
# # 'r' - Read - Default value. Opens a file for reading, error if the file does not exist
# # 'a' - Append - Opens a file for appending, creates the file if it does not exist
# # 'w' - Write - Opens a file for writing, creates the file if it does not exist
# # 'x' - Create - Creates the specified file, returns an error if the file exists


# # types types
# # text files
# # binary files


# handle = open('students.txt', 'a')
# handle.write('ram \n')
# handle.close()

# # wap to read the content of the file
# handle = open('students.txt', 'r')
# # content = handle.read()
# # content = handle.readlines()
# content = handle.readline()
# print(content)

# # name, age, address,phone


books=[
    {'id':1,'name':'python','price':100},
    {'id':2,'name':'java','price':200},
    {'id':3,'name':'c++','price':300},
    {'id':4,'name':'c#','price':400},
    {'id':5,'name':'php','price':500},
]