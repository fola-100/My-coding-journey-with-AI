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


