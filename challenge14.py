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
