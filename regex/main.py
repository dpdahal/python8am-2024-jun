# course ="we are learning python8am class"

import re
name ='ram'
# name must be in alphabets not in numbers
# patterns = '^[a-zA-Z]*$'
# if re.match(patterns,name):
#     print("valid")
# else:
#     print("invalid")

passwored = 'ram123'
# password must be included with numbers and a
# lphabets and length should be 6-16

pattern = '^[a-zA-Z0-9]{6,16}$'

if re.match(pattern,passwored):
    print("valid")
else:
    print("invalid")

