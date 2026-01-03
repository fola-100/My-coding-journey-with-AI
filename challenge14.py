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
