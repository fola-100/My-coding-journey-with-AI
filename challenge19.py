#Learning class and object
#🧠 Scenario (Automation Style)
#You are building a Simple Inventory System for a small store
#🎯 Goal
#Create a class called Product.
#The class must:
#Have attributes:
#name
#price
#quantity
#Have a normal __init__ constructor.
#Have a class method:
#from_string(cls, data_str)
#The string format will be:
#"name|price|quantity"
#Example:
#data = "Phone|300|5"
#product = Product.from_string(data)
#After creating the object:
#You must also include an instance method:
#def total_value(self):
#This should return:
#price * quantity
#My attempt
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_string(cls, data):
        name, price, quantity = data.split(",")
        return cls(name, price, quantity)

    def total_value(self):
        return float(self.quantity) * float(self.price)
