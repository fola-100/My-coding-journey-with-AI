#User Account Registration System (CLI)
#1️⃣ validate_username(username)
#Rules:
#Must be a string
#Must not be empty
#Must be at least 3 characters
#No spaces allowed
#Return:
#Username if valid
#Error message string if invalid
#2️⃣ validate_age(age_input)
#Rules:
#Must be a whole number
#Must be between 13 and 120
#Return:
#Age as int if valid
#Error message string if invalid
#3️⃣ register_user(username, age_input)
#This function:
#Calls the two validators
#If any validator returns an error → return that error
#If all valid → return a dictionary:
'''
{
    "username": "john_doe",
    "age": 25
}
'''
#MY ATTEMPT
# VALIDATING NAME
def validate_username(user_name):
    responds = []
    only_letter = all(char.isalpha() for char in user_name)
    character_len = len(user_name) >= 3
    space_condition = not any(char.isspace() for char in user_name)
    contain_value = user_name != ""
    container = {"letter": "Ensure name only contain a letter",
                 "length": "Ensure name contains more than three characters",
                 "space": "Ensure name doesn't contain any space",
                 "item": "Ensure you enter in a name"
                 }
    check_lists = [only_letter, character_len, space_condition, contain_value]
    condition = all(check for check in check_lists)
    if not condition:
        if not contain_value:
            responds.append(container["item"])
        else:
            if not only_letter:
                responds.append(container["letter"])
            if not character_len:
                responds.append(container["length"])
            if not space_condition:
                responds.append(container["space"])

        return responds
    else:
        return user_name


# VALIDATING AGE
def validate_age(user_age):
    try:
        age = int(user_age)
        return age
    except ValueError:
        return "Ensure age entered is a whole number"


def register_user(name, age):
    storage = []
    respond_vault = {}
    if not name:
        storage.append("Ensure you enter a name")
    if not age:
        storage.append("Ensure you enter a age")
    if storage:
        return storage
    name_response = validate_username(name)
    age_response = validate_username(age)
    if name_response == name and age_response == age:
        respond_vault["name"] = name_response
        respond_vault["age"] = age
        return respond_vault
    else:
        return name_response, age_response


options = input("enter one option:")
if options == "1":
    # NAME VALIDATION
    respond_value = validate_username(input("Enter a name:"))
    for respond in respond_value:
        print(respond)

if options == "2":
    # AGE VALIDATION
    print(validate_age(input("Enter your age:")))

if options == "3":
    return_value = register_user(name=input("Enter your name:"), age=input("Enter your age:"))
    for value in return_value:
        print(value)
#AI Correction
#🔴 Issue 1: validate_username returns TWO DIFFERENT TYPES
#return responds   # list
#return user_name  # string
#Why this is dangerous
#Now any code calling this function must ask:
#“Am I getting a string or a list?”
#That’s why things started breaking later.

#🔴 Issue 2: validate_age is incomplete for project needs
def validate_age(user_age):
    try:
        age=int(user_age)
        return age
    except ValueError:
         return "Ensure age entered is a whole number"

#What’s missing (based on project rules):
#Age range check (13–120)
#Empty input handling
#Consistent return type (same issue as username)

#🔴 Issue 3 (BIG ONE): Wrong function called in register_user
#age_response = validate_username(age)
#This should immediately feel wrong.
#👉 This single line explains why you said:
#“in level 3 i got stuck”
#You weren’t stuck — the program logic broke.

#🔴 Issue 4: register_user is doing too much
storage=[]
respond_vault={}
#Right now register_user:
#Re-validates empty inputs
#Calls validators
#Combines results
#Returns different shapes (list, tuple, dict)

#SECOND-ATTEMPT

#VALIDATING NAME
def validate_username(user_name):
    name_respond=[]
    #CHECKING IF CONDITION WAS MET
    only_letter= all(char.isalpha() for char in user_name)
    character_len= len(user_name)>=3
    space_condition=not any(char.isspace() for char in user_name)
    contain_value= user_name!=""
    container={"letter":"Ensure name only contain a letter",
               "length":"Ensure name contains more than three characters",
               "space":"Ensure name doesn't contain any space",
               "item":"Ensure you enter in a name"
               }
    check_lists=[only_letter,character_len,space_condition,contain_value]
    condition =all(check for check in check_lists)
    #RESPONES IF CONDITION IS NOT MET
    if not condition:
        if not contain_value:
            name_respond.append(container["item"])
        else:
            if not only_letter:
              name_respond.append(container["letter"])
            if not character_len:
               name_respond.append(container["length"])
            if not space_condition:
              name_respond.append(container["space"])
    # RETURNING RESPONSES SAVED IN LIST
        return name_respond
    else:
        name_respond.append(user_name)
        return name_respond


#VALIDATING AGE
def validate_age(user_age):
    age_vault=[]
    #CHECKING IF VALUE WAS GIVING
    if not user_age:
        age_vault.append("Ensure you enter age value")
        return age_vault
    # CHECKING IF VALUE MEET CONDITION AND RESPONSE FOR ERROR
    try:
        age=int(user_age)
        if 13<=age<=120:
            age_vault.append(age)
            return age_vault
        else:
            age_vault.append("Ensure age is between the range of 13-120")
        return age_vault

    except ValueError:
         age_vault.append( "Ensure age entered is a whole number")
         return age_vault
#REGISTER USER
def register_user(name,age):
    respond_vault={}
    #RESPONSE IF NO VALUE WAS GIVING
    if not name:
         respond_vault["name_error"]=["Ensure you enter a name"]
    if not age:
        respond_vault["age_error"]=["Ensure you enter a age"]
    if respond_vault:
        return respond_vault
    #SAVING RESPONSE AND RETURN VALUE
    name_response=validate_username(name)
    age_response=validate_age(age)
    respond_vault["name"]= name_response
    respond_vault["age"]=age_response

    return respond_vault

test=input("enter one option:")
if test=="1":
    # NAME VALIDATION
 respond_value=validate_username(input("Enter a name:"))
 for respond in respond_value:
     print(respond)

if test=="2":
#AGE VALIDATION
 respond_value=validate_age(input("Enter your age:"))
 for respond in respond_value:
     print(respond)

if test=="3":
    return_value=register_user(name=input("Enter your name:"),age=input("Enter your age:"))
    for key,value in return_value.items():
        print(value)
#AI CORRECTION
#🔴 Secondary Problems (Important but Smaller)
#Age returns the original string, not the int
#This breaks data integrity later
#register_user is doing type-detection
#Validators should tell you success/failure, not force guessing
#Errors and data are still mixed conceptually
#You fixed consistency partially, but not meaningfully
#VALIDATING NAME
def validate_username(user_name):
    error=[]
    if not user_name:
        error.append("Ensure you enter the name")
    else:
        if  not user_name.isalpha():
          error.append("Ensure name only contains letter")
        if user_name.isspace():
            error.append("Ensure name doesn't contain space")
        if len(user_name)<3:
            error.append("Ensure name contains at least three characters")
    if error:
        return{"valid":False,
               "errors":error}
    else:
        return {"valid":True,
                "value":user_name}


#VALIDATING AGE
def validate_age(user_age):
    if not user_age:
        return {
            "valid": False,
            "errors": ["Ensure you enter age value"]
        }

    try:
        age = int(user_age)
    except ValueError:
        return {
            "valid": False,
            "errors": ["Ensure age entered is a whole number"]
        }

    if not (13 <= age <= 120):
        return {
            "valid": False,
            "errors": ["Ensure age is between the range of 13–120"]
        }

    return {
        "valid": True,
        "value": age
    }

#REGISTER USER
def register_user(name,age):
    name_result = validate_username(name)
    age_result = validate_age(age)
    errors=[]
    if not age_result["valid"]:
         errors.extend(age_result["errors"])
    if not name_result["valid"]:
        errors.extend(name_result["errors"])

    if errors:
        return{"success":False,
               "error":errors
        }

    return{"success":True,
           "user":{"name":name_result["value"],
                   "age":age_result["value"]
            }
    }

#-----menu----
test=input("enter one option:")
if test=="1":
    # NAME VALIDATION
 respond_value=validate_username(input("Enter a name:"))
 if not respond_value["valid"]:
     for each_value in respond_value["errors"]:
         print(each_value)
 elif respond_value["valid"]:
      print(respond_value["value"])

if test=="2":
#AGE VALIDATION
 respond_value=validate_age(input("Enter your age:"))
 if not respond_value["valid"]:
    for each_value in respond_value["errors"]:
     print(each_value)
 elif respond_value["valid"]:
     print(respond_value["value"])


if test=="3":
    return_value=register_user(name=input("Enter your name:"),age=input("Enter your age:"))
    if not return_value.get("success"):
      for msg in return_value["error"]:
          print(msg)
    if return_value.get("success"):
      user = return_value.get("user")
      if user:
            print(user["name"])
            print(user["age"])

#Lesson learnt
#you don't always have to return each value separately you can save it inside a
#container and return that
#making sure a function is able to protect itself when from when ever it is called
#is very important when create a function
#when check basic field ensure you use simple design do not logic
#which means the response can give the same output
#each function should have its own dedicated task
#when validating with a function the return should use different object
#to separate between error and valid data
#when creating a function you must ask yourself what the function is for
#if the function is or going to be collecting data from external source
#like api,the user, been called my other file the function should protect
#iteself but if you know the function is going to be called inside the
#file and will not get any external data it don't need to protect itself

#🧩 Phase 2 — Step 1 Coding Challenge
#🔹 Your Task
#Create two functions:
#1️⃣ check_username_rules(username)
#This function:
#Performs only checks
#Does NOT create messages
#Returns a dictionary of rule results
'''
{
    "has_value": True,
    "only_letters": False,
    "min_length": True,
    "no_spaces": True
}
'''
#2️⃣ validate_username(username)
#This function:
#Calls check_username_rules
#Translates failed rules into error messages
#Returns the same structure as Phase 1
'''
{
    "valid": False,
    "errors": [...]
}
or
{
    "valid": True,
    "value": username
}

'''
#MY ATTEMPT
#VALIDATING NAME
def validate_rules(name):
    conditions={"has_value":True,
                "only_letters":False,
                "no_space":True,
                "char_length":False,


    }

    #IF THEY VALUE IN NAME
    if not name:
      conditions["has_value"]=False

    #IF THEY ARE ONLY LETTER
    if name.isalpha():
       conditions["only_letters"]=True

    #IF THEY ARE ONLY SPACE
    if " " in name:
       conditions["no_space"]=False

    if len(name)>3:
        conditions["char_length"]=True
    return conditions


def validate_username(user_name):
    results = validate_rules(user_name)
    storage_value = {}
    if not results["has_value"]:
        storage_value["has_value"] = {"valid": False,
                                     "error":"Ensure you enter a name"
                         }
    else:
        if not results["only_letters"]:
           storage_value["only_letters"] = {"valid": False,
                            "error": "Ensure name only contains letters"
                            }
           if not results["no_space"]:
               storage_value["no_space"] = {"valid": False,
                                "error": "Ensure name doesn't contain space"
                                }
           if not results["char_length"]:
               storage_value["char_length"]={"valid": False,
                       "error": "Ensure name contains at least three characters"
                       }
    return storage_value
#AI CORRECTION
#❌ Why This Is Not Correct Yet
#There are 4 core design problems. None of them are syntax mistakes
#— they are responsibility & logic issues.
#🔴 Problem 1: validate_rules does NOT only “check rules”
#You said this function should only check, but it actually:
#Assumes string methods are safe
#Mixes default assumptions with checks
#Produces partially misleading defaults
#Example:
'''
"only_letters": False
"char_length": False
'''
#These defaults already encode failure, before checking anything.
#Right now, the function decides meaning, not just checks.

#🔴 Problem 2: Rule logic is inconsistent and unsafe
#Examples:
#name.isalpha() will crash if name is empty
#" " in name and len(name) are evaluated even when name is invalid
#Why this matters
#A rule checker must:
#Be defensive
#Respect rule dependencies (e.g. “has value” comes first)
#🔴 Problem 3: validate_username no longer returns the Phase 1 contract
#This is the biggest issue.
#Required return shape (from Phase 1):
#Mentor rule:
#Refactoring must NOT change external behavior unless explicitly allowed.
#You changed the public interface.
#🔴 Problem 4: Validation logic is now fragmented
#You created:
#validate_rules → rule results
#validate_username → error mapping
#But:
#No final decision
#No clear valid / invalid outcome
#No single place to say “this username passed”
#So the caller still cannot reliably use this function.

#SECOND ATTEMPT
def validate_rules(name):
    # VALIDATING NAME
    conditions = {"has_value": True,
                  "only_letters": True,
                  "no_space": True,
                  "char_length": True,

                      }

    # IF THEY VALUE IN NAME
    if not name:
        conditions["has_value"] =False
        return conditions

    # IF THEY ARE ONLY LETTER
    conditions["only_letters"] = name.isalpha()

    # IF THEY ARE ONLY SPACE
    conditions["no_space"] = not  " " in name

    conditions["char_length"]=  len(name) > 3
    return conditions


def validate_username(user_name):
    results = validate_rules(user_name)
    error=[]
    if not results["has_value"]:
        error.append("Ensure you enter a name")
    if not results["only_letters"]:
        error.append("Ensure name only contains letters")
    if not results["no_space"]:
        error.append("Ensure name doesn't contain space")
    if not results["char_length"]:
        error.append( "Ensure name contains at least three characters")

    if error:
        return{"valid":False,
               "errors":error
        }
    return{"valid":True,
           "value":user_name}
#Excellent — this passes Phase 2 – Step 1 ✅
#✅ APPROVED
#You are officially operating at early–intermediate developer level now.
#🚀 Project #1 — Phase 2, Step 2
#🎯 Your Next Task
#Refactor age validation to match the username pattern.
#You must create:
#1️⃣ check_age_rules(age_input)
#Only evaluates rules
#Returns booleans such as:
#has_value
#is_number
#in_range
#2️⃣ validate_age(age_input)
#Calls check_age_rules
#Translates failures into messages
#Returns the same structure as before:
#MY ATTEMPT
#validating age rule
def check_age_rules(age_input):
    condition={"has_value":True,
               "whole_number":True,
               "in_range":True,
    }

    if not age_input:
      condition["has_value"]=False
      return condition

    try:
        condition["whole_number"]=age_input.isdigit()
        if not condition["whole_number"]:
           return condition
        else:
            age = int(age_input)
    except ValueError:
         condition["whole_number"]=False
         return condition



    condition["in_range"]= 13<age<=120


    return condition

#responds
def validate_age(user_age):
    result=check_age_rules(user_age)
    if not result["has_value"]:
        return{"valid":False,
               "error":"Ensure you enter in a age value"
        }
    if not result["whole_number"]:
        return{"valid":False,
               "error":"Ensure age entered is a whole number"
        }
    if not result["in_range"]:
         return{"valid":False,
                "error":"Ensure age is between the range of 13-120"
        }
    return{"valid":True,
           "value":user_age
        }
#AI CORRECTIONS
#Important improvement(Real-world level fixes)
#🔴 Issue 1: isdigit() + try/except duplication
#You currently do both:
#condition["whole_number"] = age_input.isdigit()
#and
#try:
#   age = int(age_input)
#except ValueError:
#👉 You only need ONE.
'''
Better (real-world style):
try:
    age = int(age_input)
    condition["whole_number"] = True
except ValueError:
    condition["whole_number"] = False
    return condition
'''
#Why?
#isdigit() fails for negative numbers (-1)
#2)You already converted it to int(age) earlier.
#Always return the cleaned value.
#✅ Better:
''''
return {
    "valid": True,
    "value": age
}
'''
#This avoids bugs later when math is needed
#🔴 Issue 3: Magic numbers should be constants
#Instead of:
#13 < age <= 120
#Use:
'''
MIN_AGE = 13
MAX_AGE = 120
condition["in_range"] = MIN_AGE < age <= MAX_AGE
'''
#This is professional-level code clarity

#4️⃣ Your Next Challenge (DO THIS NEXT) 🧠💻
#🎯 Challenge 1 (continue same project):
#Create email validation using the SAME pattern:
#Rules:
#Has value
#Contains exactly one @
#Contains . after @
#No spaces
#STRUCTURE:
#check_email_rules(email)
#validate_email(email)

#MY ATTEMPT
#EMAIL-VALIDATION
def check_email_rules(address):
    record={"has_value":True,
               "symbol":True,
               "dot": True,
               "no_spaces":True
    }
    if not address:
        record["has_value"]=False
        return record

    #CHECKING IF ONLY @ CONTAINS ONE
    if not "@" in address:
        record["symbol"]=False
        return record
    record["symbol"]=address.count("@")<=1

    #CHECKING IF DOT COMES AFTER @
    if record["symbol"]:
      if "." not in address:
        record["dot"]=False
        return record
      at=0
      dot=0
      for index,char in enumerate(address):
          if "@" == char:
              at=index
          if "." == char:
              dot=index
      record["dot"]=at<dot

    #CHECKING SPACES
    record["no_spaces"] = not " " in address
    return record

#Response
def validate_email(email):
    result=check_email_rules(email)
    if not result["has_value"]:
        return{"valid":False,
               "error":"Ensure you enter in a email address"
        }
    if not result["symbol"]:
        return{"valid":False,
               "error":"Ensure you enter in only one @"
        }
    if not result["dot"]:
        return{"valid":False,
               "error":"Ensure you enter in a dot after the @ symbol"
        }
    if not result["no-space"]:
        return{"valid":False,
               "error":"Ensure you remove all space"
               }
    return{"valid":True,
           "value":email}

#AI CORRECTION
#❌ Issue 1: Typo bug that will CRASH your code(KEY-ERROR)
#In check_email_rules you used:
"no_spaces"
#But in validate_email you used:
'''
result["no-space"]
FIX
if not result["no_spaces"]:
'''
#❌ Issue 2: @ logic is incorrect for multiple @
#You wrote:
'''
if not "@" in address:
    record["symbol"] = False
    return record
'''
#record["symbol"] = address.count("@") <= 1
#This allows zero @ to pass the second check if the first block didn’t return.
#✅ Correct logic
'''
record["symbol"] = address.count("@") == 1
'''
#One line. No ambiguity.
#❌ Issue 3: Dot logic finds the LAST dot, not the FIRST after @
#Your loop:
'''
for index, char in enumerate(address):
    if "@" == char:
        at = index
    if "." == char:
        dot = index
'''
#If email is:
#name@gmail.co.uk
#dot becomes the last dot, not the one after @.
'''
at = address.index("@")
dot = address.find(".", at)
record["dot"] = dot != -1
'''
#❌ Issue 4: Space check should happen EARLY
#Spaces make everything invalid.
#You should check it before complex logic.

#❌ Issue 5: You return raw email, not cleaned email
#Later in real systems you may want:
#email = email.strip().lower()
#For now, at least be consistent.

#5️⃣ NEXT PROJECT STEP (Do This Next) 🔐
#🎯 Password Validation (same project)
#Rules:
#Has value
#Minimum 8 characters
#At least one number
#At least one letter
#No spaces
#Structure:
#check_password_rules(password)
#validate_password(password)
#MY ATTEMPT
def check_password_rules(password):
    record={"has_value":False,
            "no-space":True,
            "char_length":True,
            "number":True,
            "letter":True
    }
    #CHECKING FOR VALUE
    if password:
        record["has_value"]=True
        # CHECKING IF VALUE CONTAINS SPACE
        record["no-space"] = " " not in password
        # CHECKING LENGTH
        record["char_length"] = len(password) >= 8
        # CHECKING NUMBER
        record["number"] = any(char.isdigit() for char in password)
        # CHECKING LETTER
        record["letter"] = any(char.isalpha() for char in password)
    return record


def validate_password(user_input):
    result=check_password_rules(user_input)
    error_vault=[]
    user_input=user_input.lower()
    if not result["has_value"]:
     error_vault.append("Ensure you enter in a password value")

    if not result["no-space"]:
        error_vault.append("Ensure password dose not contain any space")

    if not result["char_length"]:
        error_vault.append("Ensure password contain at least eight character")

    if not result["number"]:
        error_vault.append("Ensure password contain at least one number")

    if not result["letter"]:
        error_vault.append("Ensure password contain at one letter")

    if error_vault:
        return {"valid":False,
                "errors":error_vault
        }

    return{"valid":True,
           "value":user_input
       }

#AI CORRECTION
#❌ Issue 1: Inconsistent key naming ("no-space")
#You used:
"no-space"
#Everywhere else in your project you used:
"no_spaces"
#🚨 This will cause mental overhead and bugs in larger systems.
#✅ Fix:
"no_spaces"
#❌ Issue 2: Lowercasing the password ❗❗❗
#This is very important.
#user_input = user_input.lower()
#⚠️ This is NOT allowed in real systems.

#❌ Issue 3: has_value should start as True
#Your record starts as:
#record = {"has_value": False, ...}
#This is logically backwards and inconsistent with your other validators.
#Better pattern:
'''
record = {
    "has_value": True,
    "no_spaces": True,
    "char_length": True,
    "number": True,
    "letter": True
}
'''
#Then flip values when rules fail.
#5️⃣ FINAL STEP OF THIS PROJECT 🚀
#🎯 Build a register_user() function that uses:
#validate_username
#validate_age
#validate_email
#validate_password
#Return:
'''
{
  "valid": False,
  "errors": {
     "username": [...],
     "email": "...",
     "password": [...]
  }
}
{
  "valid": True,
  "user": {
      "username": "...",
      "age": ...,
      "email": "..."
  }
}
'''
#MY ATTEMPT
#VALIDATING NAME
def validate_rules(name):
    # VALIDATING NAME
    conditions = {"has_value": True,
                  "only_letters": True,
                  "no_space": True,
                  "char_length": True,

                      }

    # IF THEY VALUE IN NAME
    if not name:
        conditions["has_value"] =False
        return conditions

    # IF THEY ARE ONLY LETTER
    conditions["only_letters"] = name.isalpha()

    # IF THEY ARE ONLY SPACE
    conditions["no_space"] = not  " " in name

    conditions["char_length"]=  len(name) > 3
    return conditions

#Reponse
def validate_username(name):
    results = validate_rules(name)
    error=[]
    if not results["has_value"]:
        error.append("Ensure you enter a name")
    if not results["only_letters"]:
        error.append("Ensure name only contains letters")
    if not results["no_space"]:
        error.append("Ensure name doesn't contain space")
    if not results["char_length"]:
        error.append( "Ensure name contains at least three characters")

    if error:
        return{"valid":False,
               "errors":error
        }
    return{"valid":True,
           "value":user_name}

#validating age rule
def check_age_rules(age_input):
    condition={"has_value":True,
               "whole_number":True,
               "in_range":True,
    }

    if not age_input:
      condition["has_value"]=False
      return condition

    try:
        condition["whole_number"]=age_input.isdigit()
        if not condition["whole_number"]:
           return condition
        else:
            age = int(age_input)
    except ValueError:
         condition["whole_number"]=False
         return condition
    minimum=13
    maximum=120
    condition["in_range"]= minimum<age<=maximum


    return condition

#responds
def validate_age(age):
    # VALIDATING AGE
    result=check_age_rules(age)
    if not result["has_value"]:
        return{"valid":False,
               "error":["Ensure you enter in a age value"]
        }
    if not result["whole_number"]:
        return{"valid":False,
               "error":["Ensure age entered is a whole number"]
        }
    if not result["in_range"]:
         return{"valid":False,
                "error":["Ensure age is between the range of 13-120"]
        }
    return{"valid":True,
           "value":user_age
        }
#EMAIL-VALIDATION
def check_email_rules(address):
    record={"has_value":True,
               "symbol":True,
               "dot": True,
               "no_spaces":True
    }
    if not address:
        record["has_value"]=False
        return record
        # CHECKING SPACES
    if " " in address:
        record["no_spaces"] =False
        return record

        #CHECKING IF ONLY @ CONTAINS ONE
    record["symbol"]=address.count("@")==1
    if not record["symbol"]:
        return record
    #CHECKING IF DOT COMES AFTER @
    at = address.index("@")
    dot = address.find(".", at)
    record["dot"] = dot != -1
    return record

#Response
def validate_email(email):
    result=check_email_rules(email)
    error=[]
    if not result["has_value"]:
      error.append("Ensure you enter in a email address")

    if not result["no_spaces"]:
        error.append("Ensure you remove all space")

    if not result["symbol"]:
        error.append("Ensure you enter in only one @")

    if not result["dot"]:
        error.append("Ensure you enter in a dot after the @ symbol")
    if error:
        return{"valid":False,
               "error":error

               }

    return{"valid":True,
           "value":email}

def check_password_rules(password):
    record = {
        "has_value": True,
        "no_spaces": True,
        "char_length": True,
        "number": True,
        "letter": True
    }

    if not password:
        record["has_value"] = False
        return record

    record["no_spaces"] = " " not in password
    record["char_length"] = len(password) >= 8
    record["number"] = any(char.isdigit() for char in password)
    record["letter"] = any(char.isalpha() for char in password)

    return record


def validate_password(user_input):
    result = check_password_rules(user_input)
    errors = []

    if not result["has_value"]:
        errors.append("Ensure you enter a password value")

    if not result["no_spaces"]:
        errors.append("Ensure password does not contain spaces")

    if not result["char_length"]:
        errors.append("Ensure password contains at least 8 characters")

    if not result["number"]:
        errors.append("Ensure password contains at least one number")

    if not result["letter"]:
        errors.append("Ensure password contains at least one letter")

    if errors:
        return {"valid": False, "errors": errors}

    return {"valid": True, "value": user_input}


#REGISTER USER
def register_user(name,age,email,password):
    name_result = validate_username(name)
    age_result = validate_age(age)
    email_result=validate_email(email)
    password_result=validate_password(password)

    errors=[]
    if not age_result["valid"]:
         errors.extend(age_result["error"])
    if not name_result["valid"]:
        errors.extend(name_result["errors"])
    if not email_result["valid"]:
         errors.extend(email_result["error"])
    if not password_result["valid"]:
        errors.extend(password_result["errors"])
    if errors:
        return{"success":False,
               "error":errors
        }
    return {"success":True,
            "value":{"name":name_result["value"],
                     "age": age_result["value"],
                      "email":email_result["value"],
                       "password":password_result["value"]
             }

    }

if test=="4":
    user_name = input("Enter your name:").lower()
    user_age = input("Enter your age:")
    user_email=input("Enter in your email-address:")
    user_password=input("Enter in your password:")

    return_value=register_user(user_name, user_age, user_email, user_password)
    if not return_value.get("success"):
      for msg in return_value["error"]:
          print(msg)
    if return_value.get("success"):
      user= return_value["value"]
      if isinstance(user, dict):
          print("name: "+user["name"])
          print("age"+user["age"])
          print("email"+user["email"])
          print("password"+user["password"])
#AI CORRECTION
def validate_rules(name):
    # VALIDATING NAME
    conditions = {"has_value": True,
                  "only_letters": True,
                  "no_space": True,
                  "char_length": True,

                      }

    # IF THEY VALUE IN NAME
    if not name:
        conditions["has_value"] =False
        return conditions

    # IF THEY ARE ONLY LETTER
    conditions["only_letters"] = name.isalpha()

    # IF THEY ARE ONLY SPACE
    conditions["no_space"] = not  " " in name

    conditions["char_length"]=  len(name) > 3
    return conditions

#Reponse
def validate_username(name):
    results = validate_rules(name)
    errors = []

    if not results["has_value"]:
        errors.append("Ensure you enter a name")
    if not results["only_letters"]:
        errors.append("Ensure name only contains letters")
    if not results["no_space"]:
        errors.append("Ensure name doesn't contain spaces")
    if not results["char_length"]:
        errors.append("Ensure name contains at least three characters")

    if errors:
        return {"valid": False, "errors": errors}

    return {"valid": True, "value": name}



#validating age rule
def check_age_rules(age_input):
    condition={"has_value":True,
               "whole_number":True,
               "in_range":True,
    }

    if not age_input:
      condition["has_value"]=False
      return condition

    try:
        condition["whole_number"]=age_input.isdigit()
        if not condition["whole_number"]:
           return condition
        else:
            age = int(age_input)
    except ValueError:
         condition["whole_number"]=False
         return condition
    minimum=13
    maximum=120
    condition["in_range"]= minimum<=age<=maximum

    return condition

#responds
def validate_age(age):
    result = check_age_rules(age)

    if not result["has_value"]:
        return {"valid": False, "error": ["Ensure you enter an age value"]}

    if not result["whole_number"]:
        return {"valid": False, "error": ["Ensure age is a whole number"]}

    if not result["in_range"]:
        return {"valid": False, "error": ["Ensure age is between 13 and 120"]}

    return {"valid": True, "value": int(age)}

#EMAIL-VALIDATION
def check_email_rules(address):
    record={"has_value":True,
               "symbol":True,
               "dot": True,
               "no_spaces":True
    }
    if not address:
        record["has_value"]=False
        return record
        # CHECKING SPACES
    if " " in address:
        record["no_spaces"] =False
        return record

        #CHECKING IF ONLY @ CONTAINS ONE
    record["symbol"]=address.count("@")==1
    if not record["symbol"]:
        return record
    #CHECKING IF DOT COMES AFTER @
    at = address.index("@")
    dot = address.find(".", at)
    record["dot"] = dot != -1 and dot> at+1
    return record

#Response
def validate_email(email):
    result = check_email_rules(email)
    errors = []

    if not result["has_value"]:
        errors.append("Ensure you enter an email address")
    if not result["no_spaces"]:
        errors.append("Ensure email has no spaces")
    if not result["symbol"]:
        errors.append("Ensure email contains exactly one @")
    if not result["dot"]:
        errors.append("Ensure dot appears after @")

    if errors:
        return {"valid": False, "error": errors}

    return {"valid": True, "value": email}


def check_password_rules(password):
    record = {
        "has_value": True,
        "no_spaces": True,
        "char_length": True,
        "number": True,
        "letter": True
    }

    if not password:
        record["has_value"] = False
        return record

    record["no_spaces"] = " " not in password
    record["char_length"] = len(password) >= 8
    record["number"] = any(char.isdigit() for char in password)
    record["letter"] = any(char.isalpha() for char in password)

    return record


def validate_password(user_input):
    result = check_password_rules(user_input)
    errors = []

    if not result["has_value"]:
        errors.append("Ensure you enter a password value")

    if not result["no_spaces"]:
        errors.append("Ensure password does not contain spaces")

    if not result["char_length"]:
        errors.append("Ensure password contains at least 8 characters")

    if not result["number"]:
        errors.append("Ensure password contains at least one number")

    if not result["letter"]:
        errors.append("Ensure password contains at least one letter")

    if errors:
        return {"valid": False, "errors": errors}

    return {"valid": True, "value": user_input}


#REGISTER USER
def register_user(name, age, email, password):
    results = {
        "name": validate_username(name),
        "age": validate_age(age),
        "email": validate_email(email),
        "password": validate_password(password)
    }

    errors = {}
    for field, result in results.items():
        if not result["valid"]:
            errors[field] = result.get("errors") or result.get("error")

    if errors:
        return {"success": False, "errors": errors}

    return {
        "success": True,
        "user": {
            "name": results["name"]["value"],
            "age": results["age"]["value"],
            "email": results["email"]["value"]
        }
    }


#-----menu----
test=input("enter one option:")
if test=="1":
    # NAME VALIDATION
 respond_value=validate_username(input("Enter a name:"))
 if not respond_value["valid"]:
    for each_value in respond_value["error"]:
     print(each_value)

 elif respond_value["valid"]:
      print(respond_value["value"])

if test=="2":
#AGE VALIDATION
 respond_value=validate_age(input("Enter your age:"))
 if not respond_value["valid"]:
    print(respond_value["error"])

 elif respond_value["valid"]:
     print(respond_value["value"])

if test == "3":
    respond = validate_email(input("Enter your email address:"))
    if respond["valid"]:
        print(respond["value"])
    if not respond["valid"]:
        print(respond["error"])

if test=="4":
    user_name = input("Enter your name:")
    user_age = input("Enter your age:")
    user_email=input("Enter in your email-address:")
    user_password=input("Enter in your password:")

    return_value=register_user(user_name, user_age, user_email, user_password)
    if not return_value.get("success"):
        for key, value in return_value["errors"].items():
            print(f'{key}:{value}')
    if return_value.get("success"):
        user = return_value["value"]
        if isinstance(user, dict):
            print("name: " + user["name"])
            print("age" + user["age"])
            print("email" + user["email"])
#project completed
