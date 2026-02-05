#PROJECT 2 — Secure Wallet System (CLI)
#🗃️ Data Model (you must follow this)
#You will store users like this:
database = {
    "email@example.com": {
        "password": "hashed_or_plain_for_now",
        "balance": 0
    }
}

#🧩 REQUIRED FEATURES
#You must implement all of the following.
#1️⃣ User Registration
#Rules:
#email must be unique
#password must not be empty
#balance starts at 0
#return structured results
#2️⃣ Login System
#Rules:
#user must exist
#password must match
#once logged in, store who is logged in
#do NOT return the password
#3️⃣ Check Balance
#Rules:
#user must be logged in
#return balance only
#no password exposure
#4️⃣ Deposit Money
#Rules:
#user must be logged in
#amount must be:
#provided
#numeric
#greater than 0
#balance updates correctly
#5️⃣ Withdraw Money
#Rules:
#user must be logged in
#password must be re-entered
#amount must
#6️⃣ Logout
#Rules:
#clears current session
#user can’t perform actions afterward
#🧱 Constraints (VERY IMPORTANT)
#❌ No classes
#❌ No external libraries
#❌ No global variables for “current user” (think carefully 👀)
#❌ No printing inside logic functions
#✅ Functions must return dictionaries
#✅ CLI logic handles printing
#MY ATTEMPT
#Data_storage
data_base={}
current_user=None

def email_validator(address,data_storage):
    errors = []
    if not address:
        errors.append("No address entered")
        return{"valid":False,
               "error":errors,
               "success":None}
    if address in data_storage:
      errors.append("Email address already used")
      return{"valid":False,
             "error":errors,
             "success":None}
    #Checking format
    if " " in address:
        errors.append("email should not contain any space")
    if "@" not in address:
        errors.append("@ not found in email address")
    else:
       state=address.index("@")
       position=address.find(".",state)
       if position==-1 or  position<state:
         errors.append("email must contain dot after @")
    if errors:
        return{"valid":False,
               "error":errors,
               "success":None}
    return{"valid":True,
           "error":None,
           "success":address}

def password_checker(password):
    results={"value":True,
            "number":True,
            "no_space":True,
            "symbol":True,
            "length":True}
    if not password:
        results["value"]=False
        return results
    results["number"]=any(result.isdigit() for result in password)
    #password should not contain space so if they space it will False
    results["no_space"]=" " not in password
    results["symbol"]=not password.isalnum() and password != " "
    results["length"]=len(password)>=6
    return results

def password_validator(lock):
    errors=[]
    result_values=password_checker(lock)
    if not result_values["value"]:
        errors.append("No password entered")
    if not result_values["number"]:
        errors.append("Password must contain at least one number")
    if not result_values["no_space"]:
        errors.append("Password should not contain space")
    if not  result_values["symbol"]:
        errors.append("password must contain at least one symbol")
    if not result_values["length"]:
        errors.append("Password should contain at least 6 characters")
    if errors:
        return{"valid":False,
               "error":errors,
               "success":None}
    return{"valid":True,
           "error":None,
           "success":None}

def account_creation(gmail,data_vault,password):
    results={"email":email_validator(gmail,data_vault),
             "password":password_validator(password)}
    errors=[]
    if not results["email"]["valid"]:
        errors.extend(results["email"]["error"])
    if not results["password"]["valid"]:
        errors.extend((results["password"]["error"]))
    if errors:
        return{"valid":False,
               "error":errors,
               "success":None}
    #STORING USER INFO INTO DATA-BASE
    data_vault[gmail]={"password":password,"balance":0}
    return{"valid":True,
           "error":None,
           "success":gmail}

# LOGIN SYSTEM
def gmail_check(gmail,data_vault):
    if not gmail:
        return{"valid":False,
               "error":"No gmail address entered",
               "success":None}
    if not gmail in data_vault:
        return{"valid":False,
               "error":"email not found",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":gmail}

def password_check(gmail,key,data_vault):
    if not key:
        return{"valid":False,
               "error":"No password word entered",
               "success":None}
    try:
       if key not in data_vault[gmail]["password"]:
        return{"valid":False,
               "error":"Incorrect Password",
               "success":None}
    except KeyError:
        return{"valid":False,
               "error":"invalid input",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":None}

def login_attempt(user_email,storage,user_password):
    global current_user
    mail=gmail_check(user_email,storage)
    if not mail["valid"]:
        return{"valid":False,
               "error":mail["error"],
               "current_user":None}
    lock = password_check(user_email, user_password, storage)
    if not lock["valid"]:
        return{"valid":False,
               "error":lock["error"],
               "current_user":None}
    current_user=user_email
    return{"valid":True,
           "error":None,
           "current_user":user_email}



#BALANCE-CHECK
def get_balance(status,data_storage):
    if status is None:
        return{"valid":False,
               "error":"No user logged in",
               "value":None}
    return{"valid":True,
           "error":None,
           "value":data_storage[status]["balance"]}

#DEPOSIT_MONEY
def deposit_rules(status,value):
    conditions = {"has_user": True, "value":True,"whole_number":True,"is_positive": True,
                  }
    if status is None:
       conditions['has_user']=False
       return conditions
    if not value:
        conditions["value"]=False
        return conditions

    try:
       value=int(value)
    except ValueError:
        conditions["whole_number"] = False
        return conditions
    conditions["is_positive"]=value>0
    return conditions


def deposit_validator(log_status,amount,data_bank):
    result=deposit_rules(log_status,amount)
    if not result["has_user"]:
        return{"valid":False,
               "error":"No user logged in",
               "success":None}
    if not result["value"]:
        return{"valid":False,
               "error":"No amount was entered",
               "success":None}
    if not result["whole_number"]:
        return{"valid":False,
               "error":"Value entered is not a whole number",
               "success":None}
    if not result["is_positive"]:
        return{"valid":False,
               "error":"Number must not zero or less",
               "success":None}
    #ADDING AMOUNT TO DATA_BANK BAL
    data_bank[log_status]["balance"]+=int(amount)
    return{"valid":True,
           "error":None,
           "success":data_bank[log_status]["balance"]}

#WITHDRAWAL_MONEY
def withdrawal_rules(status,value,storage):
    if status is None:
        return{"valid":True,
               "error":"No user logged in",
               "success":None}
    if not value:
        return{"valid":False,
               "error":"No withdrawal amount was entered",
               "success":None}
    try:
        value=int(value)
    except ValueError:
        return{"valid":False,
               "error":"Value entered must be a whole number",
               "success":None}
    if value<=0:
        return{"valid":False,
               "error":"Number must be greater than zero",
               "success":None}
    if value>storage[status]["balance"]:
        return{"valid":False,
               "error":"Amount entered is greater than balance available",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":value}

def withdraw_validator(log_status,amount,data_bank,lock):
    withdrawal_confirmation=withdrawal_rules(log_status,amount,data_bank)
    if not withdrawal_confirmation["valid"]:
        return{"valid":False,
               "error":withdrawal_confirmation["error"],
               "success":None}
    password_confirmation = password_check(log_status, lock, data_bank)
    if not password_confirmation["valid"]:
        return {"valid": False,
                "error": password_confirmation["error"],
                "success": None}

    #REMOVEING AMOUNT ENTERED FROM BALANCE
    data_bank[log_status]["balance"]-=int(amount)
    return{"valid":True,
           "error":None,
           "success":data_bank[log_status]["balance"]}

def exist_account():
    status= None
    return status
#AI CORRECTION
#2️⃣ Critical Issues (these MUST be fixed) ❌
#❌ 1. Global variable violation (BIG ONE)
#current_user = None
#You explicitly broke the project constraint:
#❌ No global variables for current user
#Why this matters:
#Makes testing harder
#Breaks multi-user logic
#Causes hidden state bugs
#💡 Fix idea (not code):
#Pass current_user as a parameter and return updated state.
#❌ 2. Password check logic is WRONG
#if key not in data_vault[gmail]["password"]:
#This allows:
#partial matches
#security bypasses
#❌ 3. Inconsistent password rules (logic conflict)
#You enforce:
#password must contain symbol
#password must contain number
#But later during login:
#password_check()
#does NOT enforce the same rules — it only checks existence.
#This causes rule drift:
#user registers with strict rules
#login uses weaker rules
#⚠️ In real systems, this causes auth bugs.
#❌ 4. withdrawal_rules logic bug
#if status is None:
#    return {"valid": True, "error": "No user logged in"}
#This is logically impossible.
#If no user is logged in:
#valid must be False
#This will silently allow invalid flows.
#❌ 5. exist_account() is meaningless
'''
def exist_account():
    status = None
    return status
'''
#This function:
#doesn’t affect state
#doesn’t modify anything
#doesn’t log out
#It gives a false sense of logout security.

#3️⃣ Design Feedback (important but not “bugs”)
#⚠️ Email validation responsibility leak
#Your email validator:
#checks format
#checks uniqueness
#checks storage
#This is okay for now, but long-term:
#format validation
#existence checks
#storage rules
#should be separate layers.
#You’re close — just not split yet.

#⚠️ Mixed error shapes
#Sometimes:
#"error": "string"
#Sometimes:
#"error": []
#This forces extra checks later.
#Rule of thumb:
#errors should always be a list

#4️⃣ Questions your brain SHOULD have asked (reflection)
#These are the questions I would ask you after submission — exactly as you wanted:
#🧠 Q1: What happens if two users try to log in?
#Your global current_user breaks instantly.
#🧠 Q2: Can someone bypass password rules during login?
#Yes — partial string match bug.
#🧠 Q3: What guarantees logout actually logs out?
#Right now — nothing.
#🧠 Q4: Are validation rules reused or duplicated?
#They are duplicated in places → risk of inconsistency.
#🧠 Q5: Can I test this without user input?
#With globals → very hard.
#SECOND ATTEMPT
#Data_storage
data_base={}
current_user=None

def email_validator(address,data_storage):
    errors = []
    if not address:
        errors.append("No address entered")
        return{"valid":False,
               "error":errors,
               "success":None}
    if address in data_storage:
      errors.append("Email address already used")
      return{"valid":False,
             "error":errors,
             "success":None}
    #Checking format
    if " " in address:
        errors.append("email should not contain any space")
    if "@" not in address:
        errors.append("@ not found in email address")
    else:
       state=address.index("@")
       position=address.find(".",state)
       if position==-1 or  position<state:
         errors.append("email must contain dot after @")
    if errors:
        return{"valid":False,
               "error":errors,
               "success":None}
    return{"valid":True,
           "error":None,
           "success":address}

def password_checker(password):
    results={"value":True,
            "number":True,
            "no_space":True,
            "symbol":True,
            "length":True}
    if not password:
        results["value"]=False
        return results
    results["number"]=any(result.isdigit() for result in password)
    #password should not contain space so if they space it will False
    results["no_space"]=" " not in password
    results["symbol"]=not password.isalnum() and password != " "
    results["length"]=len(password)>=6
    return results

def password_validator(lock):
    errors=[]
    result_values=password_checker(lock)
    if not result_values["value"]:
        errors.append("No password entered")
    if not result_values["number"]:
        errors.append("Password must contain at least one number")
    if not result_values["no_space"]:
        errors.append("Password should not contain space")
    if not  result_values["symbol"]:
        errors.append("password must contain at least one symbol")
    if not result_values["length"]:
        errors.append("Password should contain at least 6 characters")
    if errors:
        return{"valid":False,
               "error":errors,
               "success":None}
    return{"valid":True,
           "error":None,
           "success":None}

def account_creation(gmail,data_vault,password):
    results={"email":email_validator(gmail,data_vault),
             "password":password_validator(password)}
    errors=[]
    if not results["email"]["valid"]:
        errors.extend(results["email"]["error"])
    if not results["password"]["valid"]:
        errors.extend((results["password"]["error"]))
    if errors:
        return{"valid":False,
               "error":errors,
               "success":None}
    #STORING USER INFO INTO DATA-BASE
    data_vault[gmail]={"password":password,"balance":0}
    return{"valid":True,
           "error":None,
           "success":gmail}

# LOGIN SYSTEM
def gmail_check(gmail,data_vault):
    if not gmail:
        return{"valid":False,
               "error":"No gmail address entered",
               "success":None}
    if not gmail in data_vault:
        return{"valid":False,
               "error":"email not found",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":gmail}

def password_check(gmail,key,data_vault):
    if not key:
        return{"valid":False,
               "error":"No password word entered",
               "success":None}
    #CHECKING IF PASSWORD MEET PASSWORD REQUIREMENT
    result=password_validator(key)
    if not result["valid"]:
        return{"valid":False,
               "error":result["error"],
               "success":None}
    try:
       if key==data_vault[gmail]["password"]:
        return{"valid":False,
               "error":"Incorrect Password",
               "success":None}
    except KeyError:
        return{"valid":False,
               "error":"invalid input",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":None}

def login_attempt(user_email,storage,user_password):

    mail=gmail_check(user_email,storage)
    if not mail["valid"]:
        return{"valid":False,
               "error":mail["error"],
               "current_user":None}
    lock = password_check(user_email, user_password, storage)
    if not lock["valid"]:
        return{"valid":False,
               "error":lock["error"],
               "current_user":None}
    return{"valid":True,
           "error":None,
           "current_user":user_email}

#BALANCE-CHECK
def get_balance(status,data_storage):
    if status is None:
        return{"valid":False,
               "error":"No user logged in",
               "value":None}
    return{"valid":True,
           "error":None,
           "value":data_storage[status]["balance"]}

#DEPOSIT_MONEY
def deposit_rules(status,value):
    conditions = {"has_user": True, "value":True,"whole_number":True,"is_positive": True,
                  }
    if status is None:
       conditions['has_user']=False
       return conditions
    if not value:
        conditions["value"]=False
        return conditions

    try:
       value=int(value)
    except ValueError:
        conditions["whole_number"] = False
        return conditions
    conditions["is_positive"]=value>0
    return conditions


def deposit_validator(log_status,amount,data_bank):
    result=deposit_rules(log_status,amount)
    if not result["has_user"]:
        return{"valid":False,
               "error":"No user logged in",
               "success":None}
    if not result["value"]:
        return{"valid":False,
               "error":"No amount was entered",
               "success":None}
    if not result["whole_number"]:
        return{"valid":False,
               "error":"Value entered is not a whole number",
               "success":None}
    if not result["is_positive"]:
        return{"valid":False,
               "error":"Number must not zero or less",
               "success":None}
    #ADDING AMOUNT TO DATA_BANK BAL
    data_bank[log_status]["balance"]+=int(amount)
    return{"valid":True,
           "error":None,
           "success":data_bank[log_status]["balance"]}

#WITHDRAWAL_MONEY
def withdrawal_rules(status,value,storage):
    if status is None:
        return{"valid":False,
               "error":"No user logged in",
               "success":None}
    if not value:
        return{"valid":False,
               "error":"No withdrawal amount was entered",
               "success":None}
    try:
        value=int(value)
    except ValueError:
        return{"valid":False,
               "error":"Value entered must be a whole number",
               "success":None}
    if value<=0:
        return{"valid":False,
               "error":"Number must be greater than zero",
               "success":None}
    if value>storage[status]["balance"]:
        return{"valid":False,
               "error":"Amount entered is greater than balance available",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":value}

def withdraw_validator(log_status,amount,data_bank,lock):
    withdrawal_confirmation=withdrawal_rules(log_status,amount,data_bank)
    if not withdrawal_confirmation["valid"]:
        return{"valid":False,
               "error":withdrawal_confirmation["error"],
               "success":None}
    password_confirmation = password_check(log_status, lock, data_bank)
    if not password_confirmation["valid"]:
        return {"valid": False,
                "error": password_confirmation["error"],
                "success": None}

    #REMOVEING AMOUNT ENTERED FROM BALANCE
    data_bank[log_status]["balance"]-=int(amount)
    return{"valid":True,
           "error":None,
           "success":data_bank[log_status]["balance"]}

def exist_account(user):
    user=None
    return {"valid":True,
            "error":None,
            "success":user}

