#Project Name
#🔐 User Authentication System (Login Engine)
#Challenge 1: Stored Users (Foundation)
#You are NOT logging in yet.
#Your task:
#Create a fake user database in Python.
#Requirements:
#Use a dictionary
#Each user must have:
#email
#password (plain text for now)
#Emails must be unique
#Structure must allow fast lookup by email
#💡 Hint: Think like a server.
#MY ATTEMPT

def check_user(vault, email,):
    if not email :
      return {"valid":False,
              "error":"Ensure you enter in a email address"}
    for each_address in vault:
        if email==each_address:
            return{"valid":False,
                   "error":"Email address already used"}
    return{"valid":True,
           "success":email}

def password_checker(lock):

    if not lock:
        return {"valid":False,
                "error":"Ensure you enter in a password"}
    condition=lock.isalpha()
    if not condition:
       return {"valid":False,
               "error":"Password must contain only letter"}
    return{"valid":True,
           "success":lock}

def store_user(email_storage,inbox,lock):
    result = {"email":check_user(email_storage,inbox),
              "password":password_checker(lock)
    }
    errors=[]
    if not result["email"]["valid"]:
        errors.append(result["email"]["error"])

    if not result["password"]['valid']:
        errors.append(result["password"]["error"])
    if errors:
        return{"valid":False,
               "error":errors}
    else:
        email_storage[result["email"]["success"]]=result["password"]["success"]
        return{"valid":True,
               "success":"email has been saved successfully"}


address = input("Enter in your email address:")
password = input("Enter in your password:")
storage = {}
response=store_user(storage,address,password)
if not response["valid"]:
    print(response["error"])
if response["valid"]:
    print(response["success"])
    print(storage)
#AI CORRECTION
#But this challenge was about data modeling, and you
#accidentally drifted into registration logic + I/O, which comes later.
#❌ Critical Issues (Must Fix)
#1️⃣ You violated the project rules (important)
#Rule you broke:
#❌ No input()
#❌ No printing
#❌ Just structure + explanation
#🚨 This turns a data-layer project into an interface-layer project.
#Why this matters
#In real systems:
#database logic ≠ user interaction
#mixing them causes bugs and security issues
#👉 Fix:
#Remove all input() and print() from this project step.

#2️⃣ Your storage structure is too weak
#You ended up with:
#storage[email] = password
#This works now, but it’s a trap.
#🚨 Why it’s a problem:
#No room for expansion
#Can’t add username, status, role, attempts, etc.
#Forces redesign later

#3️⃣ check_user does unnecessary looping
#for each_address in vault:
#    if email == each_address:
#🚨 This ignores the strength of dictionaries.
#You already chose the right data structure, but didn’t use it properly.
#👉 Ask yourself:
#How do dictionaries check existence?
#What operation is O(1) instead of looping?

#4️⃣ Password rule is unrealistic (but fixable)
#condition = lock.isalpha()
#This enforces:
#❌ no numbers
#❌ no symbols
#You already know from Project 1 this is too weak.
#👉 Fix is not “add more rules” yet —
#The real issue is where password rules belong in this project.
#(Hint: this project is about authentication, not password policy.)

#5️⃣ Inconsistent return contracts
#Sometimes you return:
#{"valid": True, "success": email}
#Other times:
#{"valid": True, "success": "email has been saved successfully"}
#🚨 This breaks predictability.
#In backend systems:
#success should mean one thing
#data should be under a consistent key (e.g. value)
#Second attempt
def check_user(vault, email,):
    if not email :
      return {"valid":False,
              "error":"Email empty"}

    if email in vault:
        return{"valid":False,
                "error":"Duplicate Name"}
    return{"valid":True,
           "success":email}

def password_checker(lock):

    if not lock:
        return {"valid":False,
                "error":"Password empty"}
    return{"valid":True,
           "success":lock}

def store_user(email_storage,inbox,lock):
    result = {"email":check_user(email_storage,inbox),
              "password":password_checker(lock)
    }
    errors=[]
    if not result["email"]["valid"]:
        errors.append(result["email"]["error"])

    if not result["password"]['valid']:
        errors.append(result["password"]["error"])
    if errors:
        return{"valid":False,
               "success":None,
               "error":errors}
    else:
        email_storage["vault"] = {result["email"]["success"]:{"password":result["password"]["success"]}
                                  }

        return{"valid":True,
               "success":email_storage["vault"],
               "error":None}
storage = {}

#SECOND ATTEMPT
def check_user(vault, email,):
    if not email :
      return {"valid":False,
              "error":"Email empty"}

    if email in vault:
        return{"valid":False,
                "error":"Duplicate Name"}
    return{"valid":True,
           "success":email}

def password_checker(lock):

    if not lock:
        return {"valid":False,
                "error":"Password empty"}
    return{"valid":True,
           "success":lock}

def store_user(email_storage,inbox,lock):
    result = {"email":check_user(email_storage,inbox),
              "password":password_checker(lock)
    }
    errors=[]
    if not result["email"]["valid"]:
        errors.append(result["email"]["error"])

    if not result["password"]['valid']:
        errors.append(result["password"]["error"])
    if errors:
        return{"valid":False,
               "success":None,
               "error":errors}
    else:
        email_storage["vault"] = {result["email"]["success"]:{"password":result["password"]["success"]}
                                  }

        return{"valid":True,
               "success":email_storage["vault"],
               "error":None}




storage = {}

#AI Correction
#1️⃣ The Core Problem (Big Picture)
#You are still solving the wrong problem.
#What the task WAS:
#Model stored users
#No validation. No creation. No passwords rules. No “duplicate email” checks.
#What your code is STILL doing:
#Registration logic ❌
#Validation logic ❌
#Password checking ❌
#Writing into storage ❌
#You built a mini registration system again, just lighter.

#2️⃣ Specific Issues in Your Code
#❌ Issue 1: check_user should not exist (yet)
'''
def check_user(vault, email):
'''
#This function:
#checks empty email
#checks duplicates
#🚨 That is registration behavior, not storage modeling.
#At the data layer:
#users either exist or don’t
#the storage does not care why

#❌ Issue 2: Password checker is out of scope
'''
def password_checker(lock):
'''
#Again — validation logic.
#Stored data assumes:
#“This data already passed validation earlier”

#❌ Issue 3: You are mutating storage inside logic
#email_storage["vault"] = { ... }
#This:
#overwrites previous users
#nests storage awkwardly
#makes lookup harder, not easier

#❌ Issue 4: Storage shape is unstable
#After calling store_user, your storage becomes:
'''
{
  "vault": {
     "email": { "password": "123" }
  }
}
'''
#But earlier you were checking:
#if email in vault:
#🚨 That check is now wrong.
#This means your data model fights your logic — a red flag.

#4️⃣ ✅ PROFESSIONAL DATA MODEL (Correct Solution)
#Here is the correct, clean, expandable user storage model:
'''
users = {
    "alice@example.com": {
        "password": "hashed_password_here",
        "active": True,
        "login_attempts": 0
    },
    "bob@example.com": {
        "password": "another_hash",
        "active": False,
        "login_attempts": 3
    }
}
'''
#5 Edge Cases (What You Should Be Thinking)
#These are NOT coded yet, only understood:
#empty users dictionary
#email not found during lookup
#user exists but inactive
#malformed lookup request (non-string email)
#You will handle these — just not at the storage layer.

#🚀 What Happens Next (Project 2 — Step 2)
#Now that storage is correctly modeled, next challenge:
#🔐 Login Verification Engine
#You will:
#accept email + password
#look up user in users
#compare credentials
#return structured success/error responses
#⚠️ No hashing yet
#⚠️ No input()
#⚠️ No printing
#MY ATTEMPT
def password_check(address,data_storage,lock,):
    if not lock:
        return{"valid":False,
               "error":"No password enter",
               "success":None}

    if  lock not in data_storage[address]["password"]:
        return{"valid":False,
               "error":"invalid password",
               "success":None}
    return{"valid":True,
           "error":None,
           "success":lock}


def email_check(email, data_vault):
    if not email:
        return{"valid":False,
               "error":"email address empty",
               "success":None}
    if email not in data_vault:
        return {"valid": False,
                "error": "email dose to exist",
                "success": None}
    return{"valid":True,
           "error":None,
           "success":email}


def login_verification(address,password,data_base):
    email_result=email_check(address,data_base)
    errors = []
    if not email_result["valid"]:
        errors.append(email_result["error"])
        return{"valid":False,
               "error":errors,
               "login":None}

    password_result = password_check(address, data_base, password)
    if not password_result["valid"]:
        errors.append(password_result["error"])
        return{"valid":False,
               "error":errors,
               "login":None}

    return{"valid":True,
            "error":None,
            "login":"login successful"}