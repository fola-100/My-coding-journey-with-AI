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
#SECOND ATTEMPT
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    @classmethod

    def from_string(cls, data):
        name,price,quantity=data.split("|")
        return cls(name,int(price),int(quantity))

    def total_value(self):
        return self.quantity * self.price

#NEXT CHALLENGE
#You are building a User Registration System
#🎯 Goal
#Create a class called Account.
#The class must:
#1️⃣ Have these instance attributes:
#id
#username
#2️⃣ Have a class variable:
#next_id = 1
#This will track what ID should be assigned next
#3️⃣ The __init__ method must:
#Take only username
#Automatically assign:
#self.id = Account.next_id
#Then increment next_id by 1
#So every new account gets a new ID automatically.
#4️⃣ Add a class method:
'''
@classmethod
'''
#def total_accounts(cls):
#This method should return how many accounts have been created so far.
#MY ATTMEPT

class Account:
    def __int__(self,user_name,):
        self.id=user_name
        self.id=Account.next_id

    @classmethod
    def next_id(cls):

   def total_accounts(cls):
#am stuck on what to do

#❌ First Big Issue
'''You wrote:
def __int__(self, user_name):
'''
#That is wrong.
#It must be:
'''
def __init__(self, username):
#__int__ is something completely
'''
# different in Python(used for number conversion).
#❌ Second Issue
#You wrote:
'''
self.id = user_name
self.id = Account.next_id
'''
#Two problems:

#You overwrote
#self.id twice.
#You never stored username.
#You need:
#self.username = username
#self.id = ...
#❌ Third Issue
#You wrote:
'''
@classmethod
def next_id(cls):
'''
#But next_id is supposed to be a class variable, not a method.
#It should exist at the top of the class like this:
#❌ Fourth Issue
#You started:
'''
def total_accounts(cls):
'''
#But you forgot:
'''
@classmethod
'''
#Also you didn’t implement logic.
#SECOND ATTEMPT
class Account:
    next_id=1
    def __init__(self,user_name):

        self.user_name=user_name
        self.id=+Account.next_id

    @classmethod
    def total_accounts(cls):
        return cls.next_id
#CORRECTION
#❌ Problem 1: You Are Not Incrementing
#You wrote:
#self.id = +Account.next_id
#That + does NOTHING useful.
#It just means:
#self.id = Account.next_id
#You never increased next_id.
#So every account will get:
#1
#over and over.
#❌ Problem 2: total_accounts Logic Is Still Wrong
#You wrote:
#return cls.next_id
#But remember the logic:
#If 3 accounts are created:
#IDs assigned: 1, 2, 3
#next_id becomes: 4
#So returning next_id gives 4 — which is incorrect.
#You must calculate based on what next_id represents
class Account:
    next_id = 1

    def __init__(self, username):
        self.username = username
        self.id = Account.next_id
        Account.next_id += 1

    @classmethod
    def total_accounts(cls):
        return cls.next_id - 1

#Bank Account System
#🎯 Goal
#Create a class called BankAccount.
#The class must:
#1️⃣ Have instance attributes:
#id
#owner
#balance
#2️⃣ Have a class variable:
#next_id = 1
#3️⃣ __init__ must:
#Accept owner and balance
#If balance is negative → raise a ValueError
#Automatically assign:
#self.id = BankAccount.next_id
#Increment next_id
#4️⃣ Add a class method:
'''
@classmethod
def from_string(cls, data_str):
'''
#String format: "owner|balance"
#Must convert balance to int
#Must return a new object
#5️⃣ Add an instance method:
'''
def deposit(self, amount):
'''
#Increase balance
#Amount must be positive
#If not → raise ValueError
#6️⃣ Add a class method:
'''
@classmethod
def total_accounts(cls):
'''
#Return how many accounts were created
#My Attempt
class BankAccount:
    next_id=1
    def __init__(self,owner,balance):
        balance=int(balance)
        if balance<=0:
            raise ValueError("Balance must be greater than 0")

        self.id=BankAccount.next_id
        self.owner=owner
        self.balance=balance
        BankAccount.next_id+=1

    @classmethod
    def from_string(cls,data_str):
        name,bal=data_str.split("|")
        return cls(name,bal)
    def deposit(self,amount):
        amount=int(amount)
        if amount<=0:
            raise ValueError("Balance must be greater than 0")
        else:
            self.balance+=amount
    @classmethod
    def total_accounts(cls):
       return cls.next_id-1
