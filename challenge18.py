#Transaction History & Account State Engine
#You will build:
#A transaction engine that records every action performed on an account.
'''
📦 Core Data Structure (MANDATORY)
data_base = {
    "user@email.com": {
        "password": "pass123!",
        "balance": 0,
        "history": []
    }
}
Every transaction must append a record like:
{
    "type": "deposit",
    "amount": 500,
    "balance_after": 1500
}
'''
#Required Features
#You must implement only these for now:
#1️⃣ Deposit with history
#Validate user logged in
#Validate amount
#Update balance
#Append history record
#2️⃣ Withdrawal with history
#Validate balance
#Validate password
#Update balance
#Append history record
#3️⃣ View transaction history
#Only logged-in users
#Return full history list
#No mutation
#MY-ATTEMPT
data_base = {"olamide@gmail.com": {"password": "pass123!","balance": 100,"history": ["deposite=500","withdrawal=300"]},
             "ofolaranmi@gmail.com":{"password":"mide1"}
}
current_user={'olamide@gmail.com':{"active":True}}

def gmail_validator(address,data_storage):
    if not address:
        return{"valid":False,
               "error":["No email address entered"],
               "success":None}
    if not address in data_storage:
        return{"valid":False,
               "error":["Email address not found"],
               "success":None}
    return{"valid":True,
           "error":None,
           "success":address,}


def password_validator(lock,data_storage,address):
    if not lock:
        return{"valid":False,
               "error":["No password was entered"],
               "success":None}
    try:
        if lock != data_storage[address]["password"]:
            return {"valid": False,
                    "error": ["incorrect password"],
                    "success": None}
    except KeyError:
        return {"valid": False,
                "error": ["invalid address entered"],
                "success": None}


    return{"valid":True,
           "error":None,
           "success":True}

def login_validator(gmail,password,data_vault):
    email_result=gmail_validator(gmail,data_vault)
    if not email_result["valid"]:
        return{"valid":False,
               "error":email_result["error"],
               "success":None}
    password_result=password_validator(password,data_vault,gmail)
    if not password_result["valid"]:
        return{"valid":False,
               "error":password_result["error"],
               "success":None}
    return{"valid":True,
           "error":None,
           "success":gmail}

def amount_validator(amount):
    if not amount:
        return{"valid":False,
               "error":["No amount value entered"],
               "success":None}
    try:
      amount=int(amount)
    except ValueError:
        return{"valid":False,
               "error":["Number must be a whole number"],
               "success":None}
    if amount<=0:
        return{"valid":False,
               "error":["Number must be greater than zero"],
               "success":None}
    return{"valid":True,
           "error":None,
           "success":amount}
def apply_transaction(amount, user, data_vault,action):
    try:
       amount=int(amount)
    except ValueError:
        return{"valid":False,
               "error":["NO amount was entered"],
               "success":amount}
    data_vault[user]["balance"]+=amount
    data_vault[user]["history"].append(f'{action}:{amount}')
    return{"valid":True,
           "error":None,
           "success":data_vault[user]["balance"]}

def deposit_check(address,security,safe,value,choice):
    if not safe:
        return{"valid":False,
               "error":["Nothing found data_storage"],
               "success":None}
    login_result = login_validator(address, security, safe)
    if not login_result["valid"]:
        return{"valid":False,
               "error":login_result["error"],
               "success":None}
    amount_result=amount_validator(value)
    if not amount_result["valid"]:
        return{"valid":False,
               "error":amount_result["error"],
               "success":None}
    result=apply_transaction(value, address, safe,choice)
    return{"type":choice,
           "amount":value,
           "balance_after":result["success"]}



#WITHDRAWAL WITH HISTORY
def balance_check(value,data_storage,address):
    amount_result=amount_validator(value)
    if not amount_result["valid"]:
        return{"valid":False,
               "error":amount_result["error"],
               "success":None}
    try:
       if data_storage[address]["balance"]<=amount_result["success"]:
        return{"valid":False,
               "error":["Amount enter exceed balance"],
               "success":None}
    except KeyError:
        return{"valid":False,
               "error":["invalid input"],
               "success":None}

    return{"valid":True,
           "error":None,
           "success":value}

def withdrawal(address,security,safe,amount,choice):
    login_result = login_validator(address, security, safe)
    if not choice:
        return{"valid":False,
               "error":["NO action was entered"],
               "success":None}
    if not login_result["valid"]:
        return{"valid":False,
               "error":login_result["error"],
               "success":None}
    balance_result=balance_check(amount,safe,address)
    if not balance_result["valid"]:
        return{"valid":False,
               "error":balance_result["error"],
               "success":None}
    password_result=password_validator(security,safe,address)
    if not password_result["valid"]:
        return{"valid":False,
               "error":password_result["error"],
               "success":None}
    amount=-int(amount)
    result=apply_transaction(amount,address,safe,choice)
    return{"type":choice,
           "amount":amount,
           "balance_after":result["success"]}

def history(session, account, safe):
    if not account:
        return{"valid":False,
               "error":["No user account was entered"],
               "success":None}
    if account not in session:
        return {"valid": False,
                "error": ["User enter is not active"],
                 "success": None}

    return{"valid":True,
           "error":None,
           "success":safe[account]["history"]}


