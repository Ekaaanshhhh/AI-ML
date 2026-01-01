class Product_store:
    no_of_units = 0;    
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        no_of_units+=1
    


    def get_details(self):
        return f"Product: {self.product_name}, Price: {self.price}, Units Available: {Product_store.no_of_units}"   
    