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
