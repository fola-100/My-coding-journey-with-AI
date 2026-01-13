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


