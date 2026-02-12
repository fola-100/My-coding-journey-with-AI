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

#AI CORRECTIONS
#⚠️ 1. Critical Bug in balance_check
#if data_storage[address]["balance"]<=amount_result["success"]:
#This means:
#If balance is 100
#User tries to withdraw 100
#It will FAIL.
#Because you're saying:
#if balance <= amount → error

#⚠️ 2. Dangerous Assumption in apply_transaction
#data_vault[user]["history"].append(f'{action}:{amount}')
#This assumes every user has "history".
#But look at your database:
'''
"ofolaranmi@gmail.com":{"password":"mide1"}
'''
#This user has:
#❌ no balance
#❌ no history
#If you try to transact on this account → KeyError.
#So you must decide:
#either:
#Always guarantee new accounts are created like this:
#{"password": "...", "balance": 0, "history": []}
#Or:
#Add a defensive check before appending.
#Right now your structure is inconsistent.
#You return:
'''
return{"type":choice,
       "amount":value,
       "balance_after":result["success"]}
But on error you return:

return{"valid":False,
       "error":login_result["error"],
       "success":None}
'''
#So your function returns two different structures.
#That makes frontend/UI logic messy.

#⚠️ 4. choice Validation — YES, You Should Add It
#You asked:
#should i add edge case to check if spelling of deposit or withdrawal is correct?
#YES.
#Because right now:
'''
apply_transaction(value, address, safe, choice)
'''
#If someone enters:
'''
choice = "banana"
our history becomes:
["banana:500"]
That’s bad data integrity
'''
#⚠️ 5. Double Password Check in Withdrawal
#Inside withdrawal():
#You call login_validator()
#Then later you call password_validator() again
#This is redundant because login already validated password.
#Not dangerous — but inefficient design.

#🧠 Important Design Question
#Right now:
#Every deposit and withdrawal requires login again.
#Is that what you want?
#In real systems:
#User logs in once
#Session stays active
#Transactions don't require password every time
#Your earlier version used current_user.
#This version removed session tracking.
#So decide:
#Stateless model (validate every time)
#OR
#Stateful session model
#Both are valid. But choose one intentionally.

#🔥 Now I’m Going To Level You Up
#We are upgrading Project 3.
#New Rule:
#You must implement:
#login() that sets current_user
#logout() that clears current_user
#All transactions must depend on current_user
#No password check during deposit
#Withdrawal requires password re-check
#History requires active session
#SECOND ATTEMPT
data_base = {"olamide@gmail.com": {"password": "pass123!","balance": 100,"history": ["deposite=500","withdrawal=300"]},
             "ofolaranmi@gmail.com":{"password":"mide1","balance":50}
}
current_user="olamide@gmail.com"

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
def data_base_validator(data,user):
    if not data:
        return{"valid":False,
               "error":["Nothing found in data_storage"],
               "success":None}
    if user not in  data:
        return{"valid":False,
               "error":["No user found in database"],
               "success":None}
    if "password" not in data[user] or "history" not in data[user]:
        return{"valid":False,
               "error":["Data-base most have both password and history"],
               'success':None}
    return {"valid":True,
            "error":None,
            "success":user}

def activity(choice):
    if  not choice :
        return{"valid":False,
               "error":["No choice was entered"],
               "success":None}
    if choice !="deposit" and choice!="withdraw" :
        return{"valid":False,
               "error":["choice must be deposit or withdraw"],
               "success":None}
    return{"valid":True,
           "error":None,
           "success":choice}
def apply_transaction(amount, user, data_vault,action):
    amount_result=amount_validator(amount)
    if not amount_result["valid"]:
        return {"valid": False,
                "error": amount_result["error"],
                "success": None}
    data_result = data_base_validator(data_vault, user)
    if not data_result["valid"]:
        return {"valid": False,
                "error": data_result["error"],
                "success": None}
    result_session=activity(action)
    if not result_session:
        return{"valid":False,
               "error":result_session["error"],
               "success":None}

    if action=="withdraw":
        amount=-amount_result["success"]
    else:
        amount=amount_result["success"]

    data_vault[user]["balance"] += amount
    data_vault[user]["history"].append(f'{action}:{amount_result["success"]}')
    return{"valid":True,
           "error":None,
           "success":data_vault[user]["balance"]}


def deposit_check(address,status,safe,value,choice):
    if address not in  status:
        return{"valid":False,
               "error":["User must be logged in to perform transaction"],
               "success":None}
    result=apply_transaction(value, address, safe,choice)
    if not result["valid"]:
        return{"valid":False,
               "error":result["error"],
               "success":None}
    return{"valid":True,
           "error":None,
           "success":{"type":choice,"amount":value,
                      "balance_after":result["success"]}}


#WITHDRAWAL WITH HISTORY
def balance_check(value,data_storage,address):
    amount_result=amount_validator(value)
    if not amount_result["valid"]:
        return{"valid":False,
               "error":amount_result["error"],
               "success":None}
    try:
       if data_storage[address]["balance"]<amount_result["success"]:
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

def withdrawal(address,safe,status,amount,choice,lock):
    if address not in status:
        return{"valid":False,
               "error":["User must be logged in to perform transaction"],
               "success":None}

    balance_result=balance_check(amount,safe,address,)
    if not balance_result["valid"]:
        return{"valid":False,
               "error":balance_result["error"],
               "success":None}
    password_result=password_validator(lock,safe,address)
    if not password_result["valid"]:
        return{"valid":False,
               "error":password_result["error"],
               "success":None}
    result=apply_transaction(amount,address,safe,choice)
    if not result["valid"]:
        return{'valid':False,
               "error":result["error"],
               "success":None}
    return{"valid":True,
           "error":False,
           "success":{"type":choice,
                      "amount":amount,
                       "balance_after":result["success"]}
           }

def history(satus, account, safe):
    if not account:
        return{"valid":False,
               "error":["No user account was entered"],
               "success":None}
    if account not in satus:
        return {"valid": False,
                "error": ["User enter is not active"],
                 "success": None}

    return{"valid":True,
           "error":None,
           "success":safe[account]["history"]}