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


