# what is inheritance?
# Inheritance is a parent and child relationship between classes.
# Inheritance is a mechanism by which one class 
# acquires the properties and behavior of another class.

class Laptop:
    def brand(self,brand_name):
        print(f"{brand_name} is a brand")

class Dell(Laptop):
    pass


class Toshiba(Laptop):
    pass

   
obj = Dell()
obj.brand('dell')

tobj = Toshiba()
tobj.brand('toshiba')