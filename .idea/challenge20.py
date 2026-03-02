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


