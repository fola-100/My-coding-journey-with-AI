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
#AI CORRECTION
#❌ What’s Wrong
#1️⃣ You used the wrong separator
#The challenge clearly said:
"name|price|quantity"
#But you wrote:
#name,price,quantity = data.split(",")
#That splits using a comma , not |.
#That means your code will break for:
"Phone|300|5"
#This violates the constraint.
#2️⃣ You did NOT convert price and quantity to integers inside the classmethod
#The constraint said:
#price and quantity must be stored as integers (not strings)
#Right now you are storing them as strings:
#return cls(name, price, quantity)
#Then inside total_value() you are converting them to float:
#return float(self.quantity) * float(self.price)
#That’s not correct design.
#3️⃣ Using float instead of int
#The challenge required integers.
#You used float().
#Even though it works mathematically, it violates the requirement.
