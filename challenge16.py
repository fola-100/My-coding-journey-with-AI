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


