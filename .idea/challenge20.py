#🔥 Project 5 – Multi-Account OOP Architecture
#You are building:
#User class → represents ONE account
#Bank class → manages MANY users + session
#No globals.
#No procedural helpers outside classes.
#Clean responsibility separation.
#🧠 Architecture Overview
#1️⃣ User Class
#Represents one account only.
#Must contain:
#self.email
#self._password_hash
#self.balance
#self.history
#Must implement:
#check_password(password)
#deposit(amount)
#withdraw(amount)
#get_history()
#2️⃣ Bank Class
#Represents the whole system.
#Must contain:
#self.users → dictionary {email: User}
#self.current_user → active session
#Must implement:
#register_user(email, password)
#login(email, password)
#logout()
#get_current_user()
#transfer(to_email, amount)
#🚨 Critical Rules
#✅ Password must be stored hashed
#Inside User.__init__:
#self._password_hash = hash(password)
#And password checking:
#return hash(input_password) == self._password_hash
#No raw passwords stored.
'''''
✅ All methods must return:
{
    "valid": True/False,
    "error": ...,
    "data": ...
}
Same contract everywhere.
History record format:
{
    "type": "transfer_out",
    "amount": 100,
    "to": "recipient@email.com",
    "balance_after": 400
}
and

{
    "type": "transfer_in",
    "amount": 100,
    "from": "sender@email.com",
    "balance_after": 600
}
'''
#This forces you to think about cross-object mutation safely.
#MY ATTEMPTS
class User:
    def __init__(self, email, password, balance=0, ):
        email_result = self.format_validator(email)
        if not email_result["valid"]:
            raise ValueError(email_result["error"])

        password_result = self.password_validation(password)
        if not password_result["valid"]:
            raise ValueError(password_result["error"])

        self.email = email
        self.__password_hash = hash(password)
        self.balance = balance
        self.history = []

    @staticmethod
    def format_validator(email):
        if " " in email:
            return {"valid": False,
                    "error": ["Email must not contain any space"],
                    "data": None}
        if "@" not in email:
            return {"valid": False,
                    "error": ["Email must contain @"],
                    "data": None}
        at = email.index("@")
        dot = email.find(".", at)
        if dot == -1:
            return {"valid": False,
                    "error": ["Email must have dot after @"],
                    "data": None}
        return {"valid": True,
                'error': None,
                "data": email}

    @staticmethod
    def password_validation(lock):
        if " " in lock:
            return {"valid": False,
                    "error": ["Password must not contain any space"],
                    "data": None}

        numbers = any(letter.isdigit() for letter in lock)

        if not numbers:
            return {"valid": False,
                    "error": ["Password must contain at least one number"],
                    "data": None}

        special_character = any(not letter.isalnum() for letter in lock)

        if not special_character:
            return {"valid": False,
                    "error": ["Password must contain one special characters "],
                    "data": None}

        if len(lock) < 5:
            return {"valid": False,
                    "error": ["Password must contain more than five character"],
                    "data": None}

        capital_letter = any(letter.isupper() for letter in lock)

        if not capital_letter:
            return {"valid": False,
                    "error": ["Password must contain at least one capital letter"],
                    "data": None}

        return {"valid": True,
                "error": None,
                "data": True}

    def change_password(self, password):
        result = self.password_validation(password)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}
        self.__password_hash = password
        return {"valid": True,
                "error": None,
                "data": True}

    def check_password(self, key):
        if hash(key) == self.__password_hash:
            return {"valid": True,
                    "error": None,
                    "data": True}
        return {"valid": False,
                "error": ["Incorrect password"],
                "data": None}

    @staticmethod
    def amount_validation(number):
        if not number:
            return {"valid": False,
                    "error": ["No amount value was entered"],
                    "data": None}
        try:
            number = int(number)
        except ValueError:
            return {"valid": False,
                    "error": ["Amount must be a whole number"],
                    "data": None}
        if number <= 0:
            return {"valid": False,
                    "error": ["Amount must be greater than zero"],
                    "data": None}
        return {"valid": True,
                "error": None,
                "data": number}

    def deposit(self, amount):
        result = self.amount_validation(amount)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}

        self.balance += result["data"]
        self.history.append(f'Deposit:{result["data"]}')
        return {'valid': True,
                "error": None,
                "data": result["data"]}

    def withdraw(self, amount):
        result = self.amount_validation(amount)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}

        if self.balance < result["data"]:
            return {"valid": False,
                    "error": ["insufficient balance"],
                    "data": None}

        self.balance -= result["data"]
        self.history.append(f'Withdraw:{result["data"]}')
        return {'valid': True,
                "error": None,
                "data": amount}

    def get_history(self):
        return {"valid": True,
                "error": None,
                "data": self.history}


class Bank:

    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self, address, password):
        if address in self.users:
            return {"valid": False,
                    "error": ["Email address already exist"],
                    "data": None}

        account = User(address, password)
        self.users[address] = account
        return {"valid": True,
                "error": None,
                "data": address}

    def login(self, email, password):
        if email not in self.users:
            return {"valid": False,
                    "error": ["Email address dose not exist"],
                    "data": None}

        user_obj = self.users[email]
        result = user_obj.check_password(password)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}

        self.current_user = user_obj
        return {"valid": True,
                "error": None,
                "data": self.current_user}

    def logout(self):
        self.current_user = None
        return {"valid": True,
                "error": None,
                "data": self.current_user}

    def get_current_user(self):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}

        return {"valid": True,
                "error": None,
                "data": self.users}

    def transfer(self, receiver_email, amount):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}
        if receiver_email in self.users:
            receiver_account = self.users[receiver_email]
        else:
            return {"valid": False,
                    "error": ["Email address doesn't exist "],
                    "data": None}

        withdraw_result = self.current_user.withdraw(amount)
        if not withdraw_result["valid"]:
            return {"valid": False,
                    "error": withdraw_result["error"],
                    "data": None}
        deposit_result = receiver_account.deposit(amount)
        if not deposit_result["valid"]:
            return {"valid": False,
                    "error": deposit_result["error"],
                    "data": None}
        self.current_user.history.append({"type": "transfer_out",
                                          "amount": amount,
                                          "to": receiver_email,
                                          "balance": self.current_user.balance
                                          })
        receiver_account.history.append({"type": "transfer_in",
                                         "amount": amount,
                                         "from": self.current_user.email,
                                         "balance": receiver_account.balance
                                         })

        return {"valid": True,
                "error": None,
                "data": True}
#MY ATTEMPT
#🔎 Critical Fixes (Important)
#1️⃣ 🔥 MAJOR BUG — Password Hash Broken
#In change_password:
#self.__password_hash = password
#❌ This stores RAW password.
#It must be:
#self.__password_hash = hash(password)
#Otherwise check_password() breaks
#2️⃣ 🔥 Inconsistent History Format
#Right now:
#deposit() → "Deposit:100" (string)
#withdraw() → "Withdraw:100" (string)
#transfer() → dictionary
#That’s inconsistent.
#Pick ONE structure.
#3️⃣ withdraw() Return Value Wrong
#return {'valid': True, "data": amount}
#You return the original amount, not validated int.
#Should return:
#"data": result["data"]
#Consistency matters
#4️⃣ get_current_user() Is Wrong
#return {"data": self.users}
#That returns ALL USERS.
#It should return:
'''
return {
    "valid": True,
    "error": None,
    "data": self.current_user
}
'''
#Otherwise that method name makes no sense
#5️⃣ 🚨 Transfer Has Hidden Logical Issue
#You call:
#withdraw()
#deposit()
#Then manually append transfer history.
#But withdraw() and deposit() already appended history entries.
#So transfer now creates:
#Withdraw entry
#Deposit entry
#transfer_out entry
#transfer_in entry
#That’s 4 records for 1 transfer.
#You need either:Option A (Cleanest)
#Add internal parameter to deposit() and withdraw():
'''
def deposit(self, amount, record_history=True)
'''
#Then in transfer:
self.current_user.withdraw(amount, record_history=False)
receiver.deposit(amount, record_history=False)
#And only record transfer history once.
T#hat’s real backend thinking.
#🏆 Skill Level Assessment
#You are no longer beginner.
#You are early-intermediate backend logic level.

#Your bank system must now:
#Save users to file
#Load users from file
#Restore balances
#Restore password hashes
#Restore transaction history
#Work after program restart
#🧠 Architecture Upgrade
#We keep:
#User
#Bank
#We ADD:
#File persistence inside Bank
#📦 JSON File Structure
#File name:
#bank_data.json
#Expected structure:
'''
{
  "users": {
    "alice@email.com": {
      "password_hash": 123456789,
      "balance": 500,
      "history": [
        {
          "type": "deposit",
          "amount": 500,
          "balance_after": 500
        }
      ]
    }
  }
}
'''
#🧠 Required New Methods in Bank
#1️⃣ save_to_file()
#Convert all User objects to serializable dictionaries
#Write to JSON file
#2️⃣ load_from_file()
#Read JSON file
#Reconstruct User objects
#Restore:
#hashed password
#balance
#history
#You cannot call normal constructor that hashes password.
#You must allow:
#User(email, password_hash=stored_hash, balance=stored_balance, history=stored_history)
#That means your User.__init__ must support:
#def __init__(self, email, password=None, password_hash=None, balance=0, history=None)
#Only one of password or password_hash will be provided.
#MY ATTEMPT
import hashlib
import json
from json import JSONDecodeError


class User:
    def __init__(self, email, password=None, password_hash=None, history=None, balance=0):
        email_result = self.format_validator(email)
        if not email_result["valid"]:
            raise ValueError(email_result["error"])

        if password_hash is None:
            password_result = self.password_validation(password)
            if not password_result["valid"]:
                raise ValueError(password_result["error"])

            self.__password_hash = hashlib.sha256(password.encode()).hexdigest()

        else:
            self.__password_hash = password_hash

        if history is None:
            self.history = []

        else:
            self.history = history

        self.email = email
        self.balance = balance

    def to_dic(self):
        return {"email": self.email,
                "password": self.__password_hash,
                "balance": self.balance,
                "history": self.history
                }

    @staticmethod
    def format_validator(email):
        if " " in email:
            return {"valid": False,
                    "error": ["Email must not contain any space"],
                    "data": None}
        if "@" not in email:
            return {"valid": False,
                    "error": ["Email must contain @"],
                    "data": None}
        at = email.index("@")
        dot = email.find(".", at)
        if dot == -1:
            return {"valid": False,
                    "error": ["Email must have dot after @"],
                    "data": None}
        return {"valid": True,
                'error': None,
                "data": email}

    @staticmethod
    def password_validation(lock):
        if " " in lock:
            return {"valid": False,
                    "error": ["Password must not contain any space"],
                    "data": None}

        numbers = any(letter.isdigit() for letter in lock)

        if not numbers:
            return {"valid": False,
                    "error": ["Password must contain at least one number"],
                    "data": None}

        special_character = any(not letter.isalnum() for letter in lock)

        if not special_character:
            return {"valid": False,
                    "error": ["Password must contain one special characters "],
                    "data": None}

        if len(lock) < 5:
            return {"valid": False,
                    "error": ["Password must contain more than five character"],
                    "data": None}

        capital_letter = any(letter.isupper() for letter in lock)

        if not capital_letter:
            return {"valid": False,
                    "error": ["Password must contain at least one capital letter"],
                    "data": None}

        return {"valid": True,
                "error": None,
                "data": True}

    def change_password(self, password):
        result = self.password_validation(password)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}
        self.__password_hash = hashlib.sha256(password.encode()).hexdigest()
        return {"valid": True,
                "error": None,
                "data": True}

    def check_password(self, key):
        if hashlib.sha256(key.encode()).hexdigest() == self.__password_hash:
            return {"valid": True,
                    "error": None,
                    "data": True}
        return {"valid": False,
                "error": ["Incorrect password"],
                "data": None}

    @staticmethod
    def amount_validation(number):
        if not number:
            return {"valid": False,
                    "error": ["No amount value was entered"],
                    "data": None}
        try:
            number = int(number)
        except ValueError:
            return {"valid": False,
                    "error": ["Amount must be a whole number"],
                    "data": None}
        if number <= 0:
            return {"valid": False,
                    "error": ["Amount must be greater than zero"],
                    "data": None}
        return {"valid": True,
                "error": None,
                "data": number}

    def deposit(self, amount, record_history=True):
        result = self.amount_validation(amount)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}

        self.balance += result["data"]

        if record_history:
            self.history.append({"type": "deposit",
                                 "amount": result["data"],
                                 "balance_after": self.balance})
        return {'valid': True,
                "error": None,
                "data": result["data"]}

    def withdraw(self, amount, record_history=True):
        result = self.amount_validation(amount)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}

        if self.balance < result["data"]:
            return {"valid": False,
                    "error": ["insufficient balance"],
                    "data": None}

        self.balance -= result["data"]
        if record_history:
            self.history.append({"type": "withdraw",
                                 "amount": result["data"],
                                 "balance_after": self.balance})
        return {'valid': True,
                "error": None,
                "data": result["data"]}

    def get_history(self):
        return {"valid": True,
                "error": None,
                "data": self.history}


class Bank:

    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self, address, password):
        self.load_from_file()
        if address in self.users:
            return {"valid": False,
                    "error": ["Email address already exist"],
                    "data": None}

        account = User(address, password)
        self.users[address] = account
        self.save_to_file()
        return {"valid": True,
                "error": None,
                "data": address}

    def login(self, email, password):
        self.load_from_file()
        if email not in self.users:
            return {"valid": False,
                    "error": ["Email address dose not exist"],
                    "data": None}

        user_obj = self.users[email]
        result = user_obj.check_password(password)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}

        self.current_user = user_obj
        return {"valid": True,
                "error": None,
                "data": self.current_user}

    def logout(self):
        self.current_user = None
        return {"valid": True,
                "error": None,
                "data": self.current_user}

    def get_current_user(self):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}

        return {"valid": True,
                "error": None,
                "data": self.current_user}

    def transfer(self, receiver_email, amount):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}

        if receiver_email == self.current_user.email:
            return {"valid": False,
                    "error": ["invalid receiver email"],
                    "data": None}

        if receiver_email in self.users:

            receiver_account = self.users[receiver_email]

        else:

            return {"valid": False,
                    "error": ["Email address doesn't exist "],
                    "data": None}
        withdraw_result = self.current_user.withdraw(amount, False, )
        if not withdraw_result["valid"]:
            return {"valid": False,
                    "error": withdraw_result["error"],
                    "data": None}

        deposit_result = receiver_account.deposit(amount, False)

        if not deposit_result["valid"]:
            return {"valid": False,
                    "error": deposit_result["error"],
                    "data": None}
        self.current_user.history.append({"type": "transfer_out",
                                          "amount": amount,
                                          "to": receiver_email,
                                          "balance": self.current_user.balance
                                          })
        receiver_account.history.append({"type": "transfer_in",
                                         "amount": amount,
                                         "from": self.current_user.email,
                                         "balance": receiver_account.balance
                                         })
        # Saving both new change for both sender and receiver account
        self.save_to_file()

        return {"valid": True,
                "error": None,
                "data": True}

    def save_to_file(self):
        data = {"users": {}}
        for user_address, user_account in self.users.items():
            result = user_account.to_dic()

            data["users"][user_address] = {"password_hash": result["password"],
                                           "balance": result["balance"],
                                           "history": result["history"]
                                           }

        with open("bank_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        self.users = {}
        try:
            with open("bank_data.json", "r") as file:
                users = json.load(file)
            for users_address, users_account in users["users"].items():
                stored_hash = users_account["password_hash"]
                stored_balance = users_account["balance"]
                stored_history = users_account["history"]
                account = User(users_address, password_hash=stored_hash, history=stored_history,
                               balance=stored_balance)
                self.users[users_address] = account
        except (json.JSONDecodeError, FileNotFoundError):
            self.users = {}

    def user_deposit(self, amount):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}
        result = self.current_user.deposit(amount)
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}
        self.save_to_file()
        return {"valid": True,
                "error": None,
                "data": result["data"]}

    def user_withdraw(self, amount):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}
        result = self.current_user.withdraw(amount)
        self.save_to_file()
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}
        return {"valid": True,
                "error": None,
                "data": result["data"]}

    def user_password_change(self, key):
        if self.current_user is None:
            return {"valid": False,
                    "error": ["No current_user logged in"],
                    "data": None}

        result = self.current_user.change_password(key)
        self.save_to_file()
        if not result["valid"]:
            return {"valid": False,
                    "error": result["error"],
                    "data": None}
        return {"valid": True,
                "error": None,
                "data": result["data"]}

