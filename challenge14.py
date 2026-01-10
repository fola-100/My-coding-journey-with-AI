#🔐 PROJECT CHALLENGE: PASSWORD MANAGER (CLI)
#🧩 CHALLENGE — PHASE 1 (What You Must Build)
#1️⃣ Main Menu
#Show this repeatedly:
#1) Add new account
#2) View saved accounts
#3) View account details
#4) Update account password
#5) Delete account
#6) Exit
#2️⃣ Add New Account
#Ask for:
#account name (e.g. gmail, facebook)
#username
#password
#Rules:
#Account name must be unique
#If it exists → show warning and cancel
#Save to password_vault.json
#3️⃣ View Saved Accounts
#Print only account names:
#4️⃣ View Account Details
#Ask for account name
#If found → show:
#5️⃣ Update Account Password
#Ask for account name
#Ask for new password
#Overwrite old password
#Save changes
#6️⃣ Delete Account
#7️⃣ Exit
#Program ends cleanly
#My ATTEMPT
import json

while True:
     try:
        with open("account_vault", "r") as f:
            data_retriever = json.load(f)
     except ValueError:
            data_storage={}
            with open("account_vault","r")as f:
                json.dump(data_storage,f,indent=4)
            print("No account has been created yet")


    # saving data
     data_storage ={}
    #-----main menu-----
     print("\n")
     print("(1)Add new account")
     print("(2)View saved accounts")
     print("(3)View account details")
     print("(4)Update account password")
     print("(5)Delete account")
     print("(6)Exit")
     choice=input("Enter your choice:")
     while choice not in ["1","2","3","4","5","6"]:
         choice=input("Enter your choice:")

#ADDING NEW ACCOUNT
     if choice=="1":
       #TAKE USER DETAIL AND CHECK IF IT STORAGE
       user_account=input("Enter your account_name(Facebook,X):").lower().strip()
       if  user_account in data_retriever:
          print(f'An account named {user_account}  has been created already')
          continue

       username=input("Enter you name:")

       #TAKE USER PASSWORD AND CHECK IF IT CONTAIN UNIQUE CHARACTERS
       password=input("Enter password(password must contain unique characters:")
       while password.isalnum():
          print("Ensure password contains unique characters")
          password = input("Enter password(password must contain unique characters:")

       #SAVING DATA
       data_storage[user_account]={"username":username,"password":password}
       data_retriever[user_account]=data_storage[user_account]
       with open("account_vault","w")as f:
           json.dump(data_retriever,f,indent=4)

#VIWE SAVED ACCOUNTS
     if choice=="2":
         #TEST THIS
         for account in data_retriever:
          print(f'{account}')

#VIEW ACCOUNT DETAILS
     if choice=="3":
        respond=input("Enter the account name you want to see:").lower().strip()
        # CHECKING IF RESPOND IN DATA_RETRIEVER
        if respond not in data_retriever:
              print("No account name called "+respond+" has been saved")
              continue
        print('Here are your python details')
        print("username: "+data_retriever[respond]["username"])
        print(f'password:{data_retriever[respond]["password"]}')


#UPDATA ACCOUNT PASSWORD
     if choice == "4":
      # COLLECT AND CHECKING ACCOUNT TO BE UPDATE
      value_entered = input("Enter the account name you want to update:")
      while value_entered not in data_retriever:
            print("They is no record of sure account name")
            # COLLECTING NEW PASSWORD
      password_entered = input("Enter new password:")
      while password_entered.isalnum():
          print("Ensure password contains unique characters")
          password_entered = input("Enter password(password must contain unique characters")
          data_retriever["user_account"]["password"] = password_entered
          with open("account_vault", "w") as f:
                json.dump(data_retriever, f, indent=4)
                print("Password has been updated successfully.")
#DELETE ACCOUNT
     if choice=="5":
         remove_name=input("Enter the account name you want to delete:")
         #CHECKING IF NAME TO BE REMOVED EXIST
         if remove_name not in data_retriever:
            print("No sure account can be found")
         del data_retriever[remove_name]
         with open("account_vault","w") as f:
             json.dump(data_retriever,f,indent=4)
         print(f'{remove_name} has been deleted successfully')
#EXIST
     if choice=="6":
         print("Goodbye")
         break

#Lesson learnt written program
#they are many way to check if a character has a unique character inside the string enter by the user
#first method:
#1)use is the string method :isalnum()
#the second is to use a module
#2)you can use the "string" module which allows you to assign method e.g
#.punctuation, .digital
#3)any() and all() but return a true or false value but while one check if all the whole value are TRUE
#and only return if all are True the other one "any"check if one value is True and return True
#i) so set and list function the same having similar method but the only or few difference is one use {}
# and the other uses [] and if you need to store data where
# you don't want it need for it to be  arranged in index order
#4)a dic doesn't need to be created with is key, you can always add it later when you want call
#the variable you used to call it.
#QUESTION ASK WHEN WRITING CODE:
#1)how do you  check for multi-rule password checks
#What lesson learnt:
#you have to check each individually you can not have all in one line like
#string.punctuation.digits.hex-digital etc
#You can use a for loop and use and to check

#AI Correction
#Issues:
#ValueError should be FileNotFoundError or json.decoder.JSONDecodeError if the file is missing or empty.
#You are opening the file with "r" in the except, but it should be "w" to write the empty dictionary.
#data_storage is unnecessary here; you already have data_retriever.
#✅ Fixed version:
try:
    with open("account_vault.json", "r") as f:
        data_retriever = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_retriever = {}
    with open("account_vault.json", "w") as f:
        json.dump(data_retriever, f, indent=4)
    print("No account has been created yet")
#2)2️⃣ Adding new account
# Issues:
#Your while password.isalnum(): only ensures the password contains non-alphanumeric, not unique characters.
# That’s fine for now as a simple check.
#data_storage variable was unnecessary; you can write directly to data_retriever.

#3️⃣ Update password
#Issues:
#data_retriever["user_account"]["password"] → "user_account" is a string, not your variable. Use the variable:
# data_retriever[value_entered]["password"].
#The while loop for checking password does not prompt again correctly.
# You fixed that above, just make sure it's consistent.
#✅ Fixed:
#data_retriever[value_entered]["password"] = password_entered
#with open("account_vault.json", "w") as f:
#    json.dump(data_retriever, f, indent=4)
#print("Password has been updated successfully.")
#4️⃣ Delete account
#Issue:
#You forgot continue if account does not exist, otherwise it tries to delete anyway → error.
#5️⃣ Minor tips
#Always use .json extension for clarity.
#Make your menu loop until valid input consistently.
#You could wrap each option in a function to make code cleaner
#5)data_storage = {}
#but never use it.
#👉 This is a thinking mistake, not a syntax error.
#🔴 6). Infinite loop risk in Update (Option 4)
#This part is dangerous logically:
#while value_entered not in account_vault:
#    print("They is no record of sure account name")
#Why this is a problem
#You never ask for input again inside the loop
#User is stuck forever
#5. No confirmation for delete (safety issue)
#You delete immediately:
#del account_vault[remove_name]
#Real apps always:
#Ask for confirmation
#Allow cancel
#🔥 NEXT CHALLENGES (do these in order)
#🟢 Challenge 1: Confirmation system
#Add confirmation for:
#Delete account
#Update password
#(You already know how — reuse logic)

#🟢 Challenge 2: Search feature
#Allow user to:
#Search accounts by partial name
#Example:
#Enter: face
#Shows: facebook, faceit
#This trains loop + string thinking

#🟢 Challenge 3: Masked password display
#When viewing accounts:
#Ask: Show password? yes/no
#Default: hide password (****)
#This teaches security thinking

#🟢 Challenge 4: Password strength feedback
#Instead of just rejecting passwords:
#Tell user WHY it’s weak
#Too short
#No symbols
#Repeated characters
#This builds real-world logic

#🟢 Challenge 5: Refactor into functions (IMPORTANT)
#Turn menu options into:
#add_account()
#view_accounts()
#update_password()
#delete_account()
#This is the step that:
#Makes long code readable

#MY ATTEMPT
import json
import string

#ADDING NEW ACCOUNT
def add_account(account_safe):
    # TAKE USER DETAIL AND CHECK IF IT STORAGE
    account_name = input("Enter your account_name(Facebook,X):").lower().strip()
    if account_name in account_safe:
        print(f'An account named {account_name}  has been created already')
        return None,None,None

    username = input("Enter you name:")

    # TAKE USER PASSWORD AND CHECK IF IT CONTAIN UNIQUE CHARACTERS
    while True:
        lock  = input("Enter password:")
        no_symbols = not any(char in string.punctuation for char in lock )
        has_digit = any(char in string.digits for char in lock )
        unique = len(lock ) == len(set(lock ))
        character_len = len(lock ) >= 6
        if not (no_symbols and has_digit and unique and character_len):
            # PRINTING WHICH OPTION WASN'T ENTER
            if not no_symbols:
                print("Ensure password has no uniques characters or symbols")
            if not has_digit:
                print("Ensure password has a number")
            if not unique:
                print("Ensure you password doesn't contain unique characters")
            if not character_len:
                print("Ensure password contain greater than 5 characters")
        else:
            break

    return account_name,username,lock
#VIWE SAVED ACCOUNTS
def view_account(account_safe):
    if account_safe:
        print("No account has been saved yet")
        return
    check = input("Do you also want see password?(yes/no)?:")
    if check == "yes":
        for key, value in account_safe.items():
              print(f'account name:{key}')
              print(f'account password:{value["password"]}')

    else:
        for key in account_safe:
                print(key)
#VIEW ACCOUNT DETAILS
def account_details(account_safe):
    respond = input("Enter the account name you want to see:").lower().strip()
    # CHECKING IF RESPOND IN DATA_RETRIEVER
    if respond not in account_safe:
        print("No account name called " + respond + " has been saved")
        return

    print('Here are your '+respond+' details')
    print("username: " + account_safe[respond]["username"])
    print(f'password:{account_safe[respond]["password"]}')

#UPDATA ACCOUNT PASSWORD
def update_password(account_safe):
    # COLLECT AND CHECKING ACCOUNT TO BE UPDATE
    account_name = input("Enter the account name you want to update:")
    while account_name not in account_safe:
        print("They is no record of sure account name")
        account_name = input("Enter the account name you want to update:")

    # COLLECTING NEW PASSWORD
    password_entered = input("Enter new password:")
    while True:
        #CHECKING IF PASSWORD MEET
        no_symbols=not any(letter in string.punctuation for letter in password_entered)
        digit =any(letter in string.digits  for letter in password_entered)
        unique=len(password_entered)== len(set(password_entered))
        character_len=len(password_entered)>=6
        check_list=[no_symbols,digit,unique,character_len]
        result=all(char for char in check_list)

        if result:
            return password_entered,account_name
        else:
            if not no_symbols:
                print("Ensure password has no uniques characters or symbols")
            if not digit:
                print("Ensure password contain digits")
            if not unique:
                 print("Ensure you password doesn't contain unique characters")
            if not character_len:
                print("Ensure password contain greater than 5 characters")

            password_entered = input("Enter password:")

#DELETE ACCOUNT
def delete_account(account_safe):
    remove_name = input("Enter the account name you want to delete:")
    # CHECKING IF NAME TO BE REMOVED EXIST
    if remove_name not in account_vault:
        print("No sure account can be found")
    # PASSWORD CONFIRMATION BEFORE DELETING
    check = input("Are you show you want to delete your " + remove_name + " account?:")
    while check not in ["yes", "no"]:
        print("Enter only yes or no")
        check = input("Are you show you want to delete your " + remove_name + " account?:")
    if check == "no":
       return
    # DELETING ACCOUNT
    del account_safe[remove_name]
    with open("account_vault", "w") as f:
        json.dump(account_vault, f, indent=4)
    print(f'{remove_name} has been deleted successfully')


# SEARCHING FOR ACCOUNT
def search(account_safe):
    name = input("Enter account name to search for:")
    for account in account_safe:
        if name in account:
            print(account)


while True:
     try:
        with open("account_vault", "r") as f:
            account_vault = json.load(f)
     except (FileNotFoundError,json.decoder.JSONDecodeError)  :
            account_vault={}
            with open("account_vault","w")as f:
                json.dump(account_vault, f, indent=4)
            print("No account has been created yet")

    #-----main menu-----
     print("\n")
     print("(1)Add new account")
     print("(2)View saved accounts")
     print("(3)View account details")
     print("(4)Update account password")
     print("(5)Delete account")
     print("6)Search for account ")
     print("(7)Exit")

     choice=input("Enter your choice:")
     while choice not in ["1","2","3","4","5","6"]:
         choice=input("Enter your choice:")

#ADDING NEW ACCOUNT
     if choice=="1":
         (user_account,user_name,password)=add_account(account_vault)
         # SAVING DATA
         account_vault[user_account]={"username": user_name, "password": password}

         with open("account_vault", "w") as f:
             json.dump(account_vault, f, indent=4)


#VIWE SAVED ACCOUNTS
     if choice=="2":
         view_account(account_vault)

#VIEW ACCOUNT DETAILS
     if choice=="3":
         account_details(account_vault)

#UPDATA ACCOUNT PASSWORD
     if choice == "4":
        password,account_entered=update_password(account_vault)
        account_vault[account_entered]["password"]=password
        with open("account_vault", "w") as f:
            json.dump(account_vault, f, indent=4)
            print("Password has been updated successfully.")
#DELETE ACCOUNT
     if choice=="5":
         delete_account(account_vault)

# SEARCHING FOR ACCOUNT
     if choice=='6':
         search(account_vault)

#EXIST
     if choice=="7":
         print("Goodbye")
         break

#AI-CORRECTION
'''
⚠️ Logical problem (important)
Your variable naming is misleading:
no_symbols = not any(char in string.punctuation for char in lock)
But later you say:
"Ensure password has no unique characters or symbols"
This causes confusion between meaning and name.
🧠 Thinking rule
Variable names must describe what is TRUE, not what you wish they were.

2)⚠️ Return-value danger (very important)
You return:
return None, None, None
But later you always do:
account_vault[user_account] = {...}
🧠 Thinking rule
If a function can fail, the caller MUST handle failure.
Right now:
If account exists → function returns None
Main code still tries to use it
This will crash
This is a real-world bug, not theoretical.

3)❌ Logic bug (serious)
if account_safe:
    print("No account has been saved yet")
    return
This is backwards logic.
🧠 Thinking rule
Empty dictionary → False
Non-empty dictionary → True

4)4️⃣ update_password()
⚠️ Minor logic clarity issue
result = all(char for char in check_list)
This works, but the variable name char is misleading.
🧠 Thinking rule
Names should describe what they represent.

5)5️⃣ delete_account()
❌ Very important bug
You wrote:
if remove_name not in account_vault:
But the function parameter is:
def delete_account(account_safe):
❌ Missing return on failure
If account doesn’t exist:
You print error
But still continue deletion logic
🧠 Thinking rule
Functions should not depend on global variables.
This function breaks isolation and relies on outer scope.
That’s dangerous and unscalable.
After an error, exit the function immediately.
'''
