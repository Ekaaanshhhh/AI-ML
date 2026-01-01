#instance method has only one parameter self whereas class method has cls as a parameter and is decorated using @classmethod, decorators are higher order function that modify and return the behaviour of a function, for example

class Laptop:
    storage_type="SSD"
    def __init__(self,storage,ram):
        self.storage = storage
        self.ram =ram
    
    @classmethod #decorator that defines the behaviour of get_info as a class method
    def get_info(cls):
        print(f"this laptop has {cls.storage_type} storage")

    def get_ram(self):
        print(f"this laptop has {self.ram} ram")


lap1 = Laptop("512gb","8gb")

Laptop.get_info()#class method called using class name
lap1.get_ram()#instance method called using object name
