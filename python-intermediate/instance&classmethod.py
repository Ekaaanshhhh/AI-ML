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

    @staticmethod
    #created when we neither want to use instance attributes nor class attributes
    #static method does not take cls or self as a parameter
    def welcome_msg():
        print("Welcome to the laptop store")
    
    @staticmethod
    #this is a static method because it does not use storage type(class attribute) or ram type and storage type(instance attributes)
    def discount(price,percent):
        return price-((percent/100)*price);


lap1 = Laptop("512gb","8gb")

Laptop.get_info()#class method called using class name
lap1.get_ram()#instance method called using object name
lap1.welcome_msg()#static method called using object name

print(f"discounted price of laptop 1 is {lap1.discount(1000,15)}")
