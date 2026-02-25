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
#AI CORRECTION
#1️⃣ Your balance validation says:
#if balance <= 0:
#The requirement said:
#Prevent negative starting balances
#That means:
#balance < 0
#Right now you are also preventing someone from opening an account with 0 balance.

#2️⃣ Your error message inside deposit
#You wrote:
'''
raise ValueError("Balance must be greater than 0")
'''
#That message is wrong contextually.
#It should say something like:
"Deposit amount must be greater than 0"
#Clear error messages matter in real systems.
#3️⃣ Minor Design Improvement (Advanced Thinking)
#Inside __init__, you converted:
#balance = int(balance)
#That works.
#But since from_string is responsible for parsing external data,
#some engineers would prefer conversion there instead.
#Both designs are acceptable — but understanding the separation of responsibility is advanced thinking.

#Scenario (Backend Banking System)
#You are improving your BankAccount system.
#Right now, someone can do this:
'''
acc = BankAccount("Olamide", 500)
acc.balance = 1000000000   # 😑 cheating
'''
#That should NOT be allowed.
#🎯 Goal
#Create a class called SecureBankAccount.
#The class must:
#1️⃣ Have instance attributes:
#id
#owner
#a private balance attribute
#The balance must NOT be directly accessible like:
#acc.balance
#It should not exist as a public attribute.
#2️⃣ Have a class variable:
#next_id = 1
#Auto-increment ID like before.
#3️⃣ __init__ must:
#Accept owner and balance
#Prevent negative balance
#Store balance privately
#Assign ID automatically
#4️⃣ Add a method:
#def get_balance(self):
#5️⃣ Add methods:
'''
def deposit(self, amount)
def withdraw(self, amount)
'''
#Rules:
#Amount must be positive
#Cannot withdraw more than available balance
#Must raise ValueError if invalid
#6️⃣ Add:
'''
@classmethod
def total_accounts(cls)
'''
#Return total created accounts.
#MY ATTEMPT
class SecureBankAccount:
    next_id=1

    def __init__(self,owner,balance):
        balance=int(balance)
        self.id=SecureBankAccount.next_id
        self.owner=owner
        self.__balance=balance
        SecureBankAccount.next_id+=1

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        amount=int(amount)
        if amount<0:
            raise ValueError("Deposit amount must be greater than zero")
        self.__balance+=amount

    def withdraw(self,amount):
        amount=int(amount)
        if amount<0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if self.__balance<amount:
            raise ValueError("Withdrawal amount is greater than balance available")
        self.__balance-=amount

    @classmethod
    def total_id(cls):
        return cls.next_id-1

#🏦 Digital Wallet System (Professional Style)
#You are building the backend logic for a fintech startup in Nigeria.
#You must design a Digital Wallet system.
#🎯 Requirements
#1️⃣ Create a Class: DigitalWallet
#The wallet must have:
#owner (string)
#balance (default = 0)
#transactions (list that stores transaction history)
#2️⃣ Methods Required
#✅ deposit(amount)
#Adds money to balance
#Adds transaction string:
"Deposited ₦5000"
#Reject negative deposits
#✅ withdraw(amount)
#Subtracts money if balance is enough
#Adds transaction string:
"Withdrew ₦2000"
#if insufficient funds:
#Print "Insufficient funds"
#Do NOT change balance
#✅ transfer(amount, other_wallet)
#Sends money to another DigitalWallet object
#Should:
#Withdraw from sender
#Deposit to receiver
#Add transaction:
"Transferred ₦1000 to Tunde"
#✅ show_balance()
#Returns current balance
#✅ show_transactions()
#Prints all transactions
#MY ATTEMPT
class DigitalWallet:
    def __init__(self,owner,history="",balance=0):
     #history and bal is set to zero and empty in a case where a new wallet
        balance=int(balance)
        self.owner=owner
        self.transactions=[history]
        self.balance=balance

    def deposit(self,amount):
        amount=int(amount)
        if amount<=0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance+=amount
        self.transactions.append(f'Deposited:N{amount}')
    def withdraw(self,amount):
        amount=int(amount)
        if amount<0:
            raise ValueError("Withdraw amount must be greater than zero")
        if self.balance<amount:
            raise ValueError("Insufficient funds")
        self.balance-=amount
        self.transactions.append(f'Withdraw: N{amount}')

    def transfer(self,amount,other_wallet):
        amount = int(amount)
        if amount < 0:
            raise ValueError("Withdraw amount must be greater than zero")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.other_wallet=other_wallet
        self.other_wallet.balance+=amount
        self.transactions.append(f'Transferred {amount} to {self.other_wallet.owner}')

    def show_balance(self):
        return self.balance

    def show_transaction(self):
        return self.transactions



debug=DigitalWallet(input("Enter in your name:"),"deposit:500",500)
print(debug.balance)
debug_test=DigitalWallet("yemi")
debug.deposit(300)
debug.withdraw(100)
debug.withdraw(200)
debug.transfer(400,debug_test)
print(debug.balance)

#❌ Issues You Must Fix
#1️⃣ Bad transactions Initialization (Very Important)
def __init__(self,owner,history="",balance=0):
    self.transactions=[history]
#Problem:
#Every new wallet starts with:
#[""]
#That means there is always a fake transaction inside.
#Professionally:
#self.transactions = []
#Transactions should start empty.
#2️⃣ Transfer Logic Is Not Professional
#You wrote:
#self.balance -= amount
#self.other_wallet = other_wallet
#self.other_wallet.balance += amount
#❌ Problem:
#You are directly modifying another object's balance.
#That breaks encapsulation thinking.
#3️⃣ You Didn’t Add Receiver Transaction History
#Requirement says:
#Transfer should log:
"Transferred ₦1000 to Tunde"
#But what about the receiver?
#Receiver should also have something like:
"Received ₦1000 from Olamide"
#4️⃣ Wrong Behavior for Insufficient Funds
#The requirement said:
#If insufficient funds:
#Print "Insufficient funds"
#Do NOT change balance
#You are doing:
raise ValueError("Insufficient funds")
#That crashes the program.
#We are building backend logic, not stopping the entire app.
#5️⃣ Method Name Typo
#You wrote:
#def show_transaction(self):
#Requirement says:
#show_transactions()
#AI CORRECTION
''''''
class DigitalWallet:
    def __init__(self,owner,balance=0):
     #history and bal is set to zero and empty in a case where a new wallet
        balance=int(balance)
        self.owner=owner
        self.transactions=[]
        self.balance=balance

    def deposit(self,amount):
        amount=int(amount)
        if amount<=0:
            print("Deposit amount must be greater than zero")
            return False
        self.balance+=amount
        self.transactions.append(f'Deposited:N{amount}')
        return True

    def withdraw(self,amount):
        amount=int(amount)
        if amount<0:
            print("Withdraw amount must be greater than zero")
            return False
        if self.balance<amount:
            print("Insufficient funds")
            return False
        self.balance-=amount
        self.transactions.append(f'Withdraw: N{amount}')
        return True

    def transfer(self,amount,other_wallet):
        if self.withdraw(amount):
          other_wallet.deposit(amount)
          self.transactions.append(f'Transferred N{amount} to {other_wallet.owner}')
          other_wallet.transactions.append(f'Received N{amount} from {self.owner}')
    def show_balance(self):
        return self.balance

    def show_transactions(self):
        return self.transactions

#🔥 Challenge #2 — Mini Banking System
#You are building the core logic for a small digital bank.
#This time, we are not just modeling a wallet.
#We are modeling the Bank itself.
#🎯 Objective
#You must design two classes:
#BankAccount
#Bank
#This tests:
#Class-to-class interaction
#Lists of objects
#Searching objects
#Encapsulation
#Method coordination
#🏦 Class 1: BankAccount
#Attributes
#owner (string)
#balance (default = 0)
#account_number (auto-generated number)
#transactions (list)
#Requirements
#🔢 Account Number
#Each new account must automatically get a unique account number.
#Example:
#First account → 1001
#Second → 1002
#Third → 1003
#You must implement this using a class variable.
#Methods Required
#✅ deposit(amount)
#Add to balance
#Add transaction
#Reject invalid deposits
#✅ withdraw(amount)
#Subtract if sufficient
#Add transaction
#Print message if insufficient
#✅ show_details()
#Return formatted string:
#Account: 1001
#Owner: Olamide
#Balance: ₦5000

#🏛 Class 2: Bank
#The Bank manages multiple accounts.
#Attributes
#name
#accounts (a list storing BankAccount objects)
#Methods Required
#✅ create_account(owner, initial_deposit=0)
#Creates a new BankAccount
#Adds it to bank’s account list
#Returns the account object
#✅ find_account(account_number)
#Searches accounts list
#Returns the account object
#If not found → print "Account not found"
#✅ transfer(sender_account_number, receiver_account_number, amount)
#Find both accounts
#Withdraw from sender
#Deposit to receiver
#Only complete transfer if withdraw succeeds
#✅ total_bank_balance()
#Returns total money across all accounts
#MY ATTEMPT
class BankAccount:
    account_created = 1001
    def __init__(self,owner,balance=500,):
        self.owner=owner
        self.account_number=BankAccount.account_created
        self.balance=balance
        self.transactions=[]
        BankAccount.account_created+=1

    def deposit(self,amount):
        amount=int(amount)
        if amount<=0:
            print("Deposit must be greater than zero")
            return False
        self.balance+=amount
        self.transactions.append(f'Account:{self.account_number} Owner:{self.owner} Balance:{self.balance} ')

        return True
    def withdraw(self,amount):
        amount=int(amount)
        if amount<=0:
           print("Withdrawal amount must be greater than zero")
           return False
        if self.balance<amount:
            print("Withdraw amount is greater than balance available ")
            return False
        self.balance-=amount
        self.transactions.append(f'Account:{amount}'
                                 f'Owner:{self.owner}'
                                 f'Balance{self.balance}')
        return True
    def show_details(self):
        return self.transactions

class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts=[]

    def create_account(self):
        storage=BankAccount(self.name)
        self.accounts.append(storage)
        return storage

    def find_account(self,account_number):
        for account_details in self.accounts:
            if account_details.account_number==account_number:
                return account_details
        print("Account not found")
        return None

    def transfer(self,sender_account,receiver_account_number,amount ):
        sender=False
        receiver=False
        sender_details=None
        receiver_details=None
        for account in self.accounts:
            if account.account_number==sender_account:
                sender_details=account
                sender=True
        if not sender:
           print("Sender Account number those not exist ")
           return sender
        for account in self.accounts:
            if account.account_number == receiver_account_number:
                receiver = True
                receiver_details=account
        if not receiver:
           print("Receiver Account number those not exist")
           return receiver
        result=sender_details.withdraw(amount)
        if result:
          deposit_result=receiver_details.deposit(amount)
          if deposit_result:
            print("Transaction successful")
            return True
          else:
              return False
        else:
            return False

    def total_bank_balance(self):
        total=0
        for account in self.accounts:
            total+=account.balance
        return total

#AI CORRECTION
#❌ Problem 1 — create_account() is Wrong
#Your version:
def create_account(self):
    storage=BankAccount(self.name)
#🚨 Issue
#You are using self.name (bank name) as account owner
#You are not accepting owner
#You are not accepting initial_deposit
#But the requirement was:
#create_account(owner, initial_deposit=0)
#So it should allow:
#acc1 = my_bank.create_account("Olamide", 10000)
#Your version cannot do that
#❌ Problem 2 — Default Balance in BankAccount
#You wrote:
def __init__(self,owner,balance=500)
#Why is default 500?
#The requirement said default should be 0.
#This is a design mistake.
#❌ Problem
#3 — show_details()
#Is Wrong
#Requirement:
#Account: 1001
#Owner: Ola_mide
#Balance: ₦5000
#Your
#version:
#return self.transactions
#🚨 That
#returns
#transaction
#history — not account
#details.
#❌ Problem 4 — Transaction Log Format Error
#In withdraw:
self.transactions.append(f'Account:{amount}'
                         f'Owner:{self.owner}'
                         f'Balance{self.balance}')
#You accidentally wrote:
Account: {amount}
#Instead of:
Account: {self.account_number}

#That’s a real - world logging bug.

#❌ Problem 5 — transfer() Signature Wrong
#Requirement:
#transfer(sender_account_number, receiver_account_number, amount)
#Your version:
def transfer(self, sender_account, receiver_account_number, amount)
#That part is fine.
#BUT:
#You manually looped twice to find accounts instead of using your own find_account() method.
#Professionally, we reuse logic.
#You already wrote:
find_account()
#❌ Problem 6 — Missing Initial Deposit in Account Creation
#When creating account with initial money, that money should:
#Be added to balance
#Be recorded in transactions
#Right now your create_account does neither

#Second attempt
class BankAccount:
    account_created = 1001
    def __init__(self,owner,balance=0,):
        self.owner=owner
        self.account_number=BankAccount.account_created
        self.balance=balance
        self.transactions=[]
        BankAccount.account_created+=1

    def deposit(self,amount):
        amount=int(amount)
        if amount<=0:
            print("Deposit must be greater than zero")
            return False
        self.balance+=amount
        self.transactions.append(f'Account:{self.account_number} |'
                                 f'Owner:{self.owner} |'
                                 f'Balance{self.balance}')

        return True
    def withdraw(self,amount):
        amount=int(amount)
        if amount<=0:
           print("Withdrawal amount must be greater than zero")
           return False
        if self.balance<amount:
            print("Withdraw amount is greater than balance available ")
            return False
        self.balance-=amount
        self.transactions.append((f'Account:{self.account_number}|'
                                  f' Owner:{self.owner}|'
                                  f' Balance{self.balance}'))
        return True
    def show_details(self):
        return (f'Account:{self.account_number}|'
                f'Owner:{self.owner}|'
                f'Balance{self.balance}|')

class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts=[]

    def create_account(self,owner,initial_deposit=0):
        storage=BankAccount(owner,initial_deposit)
        self.accounts.append(storage)
        return storage

    def find_account(self,account_number):
        for account_details in self.accounts:
            if account_details.account_number==account_number:
                return account_details
        print("Account not found")
        return None

    def transfer(self, sender_account,receiver_account_number,amount ):
        sender= self.find_account(sender_account)
        if not sender:
           print("Sender Account number does not exist ")
           return sender
        receiver=self.find_account(receiver_account_number)
        if not receiver:
           print("Receiver Account number does not exist")
           return receiver
        result=sender.withdraw(amount)
        if result:
          deposit_result=receiver.deposit(amount)
          if deposit_result:
            print("Transaction successful")
            return True
          else:
              return False
        else:
            return False

    def total_bank_balance(self):
        total=0
        for account in self.accounts:
            total+=account.balance
        return total
#❌ 1️⃣ Initial Deposit Logic Is Not Professional
#Right now:
#storage = BankAccount(owner, initial_deposit)
#This directly sets balance.
#But professional systems do NOT directly set balance like this.
#Why?
#Because:
#It bypasses validation
#It bypasses transaction logging
#If initial_deposit is 10000,
#it should be recorded in transactions.
#Right now it is not.

#❌ 2️⃣ Transaction Log Format Is Weak
#Right now you log:
f'Account:{self.account_number} |Owner:{self.owner} |Balance{self.balance}'
#The is logs the entire account snapshot.
#Professionally, logs should record the action, not full state.
#Better format:
"Deposited ₦500"
"Withdrew ₦300"
#❌ 3️⃣ Minor Formatting Issue
#In show_details:
'''
return (f'Account:{self.account_number}|'
        f'Owner:{self.owner}|'
        f'Balance{self.balance}|')
'''
#You are missing spaces and currency formatting.
#🧠 Level Assessment
#You are no longer just “learning classes.”
#You now understand:
#Class variables
#Object interaction
#Encapsulation logic
#Validation flow
#Method reuse
#Conditional transaction execution
#🎓 Final Professional Version (For Learning)
class BankAccount:
    account_created = 1001

    def __init__(self, owner):
        self.owner = owner
        self.account_number = BankAccount.account_created
        self.balance = 0
        self.transactions = []
        BankAccount.account_created += 1

    def deposit(self, amount):
        amount = int(amount)
        if amount <= 0:
            print("Deposit must be greater than zero")
            return False

        self.balance += amount
        self.transactions.append(f"Deposited ₦{amount}")
        return True

    def withdraw(self, amount):
        amount = int(amount)
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
            return False

        if self.balance < amount:
            print("Insufficient funds")
            return False

        self.balance -= amount
        self.transactions.append(f"Withdrew ₦{amount}")
        return True

    def show_details(self):
        return (
            f"Account: {self.account_number}\n"
            f"Owner: {self.owner}\n"
            f"Balance: ₦{self.balance}"
        )


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, owner, initial_deposit=0):
        account = BankAccount(owner)
        self.accounts.append(account)

        if initial_deposit > 0:
            account.deposit(initial_deposit)

        return account

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        print("Account not found")
        return None

    def transfer(self, sender_acc_num, receiver_acc_num, amount):
        sender = self.find_account(sender_acc_num)
        receiver = self.find_account(receiver_acc_num)

        if not sender or not receiver:
            return False

        if sender.withdraw(amount):
            receiver.deposit(amount)
            return True

        return False

    def total_bank_balance(self):
        return sum(account.balance for account in self.accounts)