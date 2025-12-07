#🔹 Project Idea: “Mini Data Processor”
#Scenario: You’re building a small program that can:
#Store a list of users with their info (name, age, favorite numbers)
#Process that data (filter, transform, summarize)
#Allow simple queries on the data
#This will let us practice:
#Lists, dictionaries, loops
#Functions and return values
#List comprehensions
#Conditionals
#user info
data_storage={"name":"","age":"","favorite_number":[]}
user_name=input("Enter your name:").lower().strip()
user_age=input("Enter your age:")
fav_number=input("Enter your favorite number:")
data_storage["name"]=user_name
data_storage["age"]=user_age
data_storage["favorite_number"]=fav_number
#My Attempt
while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Exist")
    choice=input("Enter your choice:")
    if choice=="1":
      result=data_storage["name"]
      print(f'Your name is {result}')
    elif choice=="2":
       result=data_storage["age"]
       int(result)
       print(result)
    elif choice=="3":
        result=data_storage["favorite_number"]
        print(result)
    elif choice=="4":
        print("Goodbye")
        break
#AI correction
# Points to improve:
#Favorite number
#fav_number = input("Enter your favorite number:")
#Right now, this is a string. If the user enters multiple numbers (like 1,2,3), you need to convert it into a list of integers.
#For example:
fav_number = input("Enter your favorite numbers separated by commas: ")
fav_number = [int(n.strip()) for n in fav_number.split(",")]

#2)Age conversion
result = data_storage["age"]
int(result)
print(result)
#int(result) creates an integer, but you’re not saving it back — so result is still a string.
#Better:
result = int(data_storage["age"])
print(result)

#3)Minor naming / readability
#data_storage could be called user_data — more meaningful.
#Menu printing could be inside a function later, when we expand the project.
#⭐ Next Step Challenge (Step 1 for the project)
#Goal: Make the program support multiple users (at least 3).
#Store all users in a list (users_list).
#Each user is a dictionary with the same keys as now.
#Print all users’ info nicely at the end.
#Example output:
#User 1: Name=Alice, Age=25, Numbers=[2,4,6]
#User 2: Name=Bob, Age=30, Numbers=[1,3,5]
#User 3: Name=Carol, Age=20, Numbers=[7,8,9]
#MY(Attempt)
#--------- main menu------
def menu_option():
  while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Exist")
    choice=input("Enter your choice:")
    if choice=="1":
      result=user_data["name"]
      print(f'Your name is {result}')
    elif choice=="2":
       result=user_data["age"]
       int(result)
       print(result)
    elif choice=="3":
        result=user_data["favorite_number"]
        print(result)
    elif choice=="4":
        print("Goodbye")
        break
#user of the program
def user(dic_data,user_storage_area):
    user_count={"user1":"","user2":"","user3":""}
    if user_storage_area == "user1":
        user_count["user1"]=dic_data

    elif user_storage_area=="user2":
        user_count["user2"]=dic_data
    else:
        user_count["user3"]=dic_data

def user_mode():
   print("They is only three available user storage area,Tell me which you "
         "will like to use and i will tell you if is available")
   print('\n----Storage options----')
   print("User1")
   print("User2")
   print("User3")

   choice=input("Enter your choice:").lower().strip()
   while choice not in ["user1","user2","user3"]:
       print("invalid choice")
       choice=input("Enter your choice").lower().strip()
   if choice=="user1":
       return "user1"
   elif choice=="user2":
       return "user2"
   elif choice=="user3":
        return "user3"
   return None

#asking for which mode they like to use
value=user_mode()

#saving user input data
user_name = input("Enter your name:").lower().strip()
user_age = input("Enter your age:")
fav_number = input("Enter your favorite number and separated by a comma:")
# turning fav_number into a integer
fav_number = [int(f.strip()) for f in fav_number.split(",")]

#saving users input
user_data={"name":user_name,"age":user_age,"favorite_number":fav_number}
#
user(user_data,value)
#
menu_option()
#AI Correction
#❗ IMPORTANT: The big issue in your code
def user(dic_data,user_storage_area):
    user_count={"user1":"","user2":"","user3":""}
    if user_storage_area == "user1":
        user_count["user1"]=dic_data
#This has one major problem:
#❌ user_count is created INSIDE the function
#That means every time the function runs, the dictionary resets, so you are not actually saving any user data anywhere.
#Python throws the whole dictionary away when the function finishes

#Side task
#To continue the project, we need:
#A SINGLE list or dictionary that stores all 3 users permanently.
#My Attempt
#--------- main menu------
def menu_option(mode_value):
  while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Exist")
    choice=input("Enter your choice:")
    if choice=="1":
      result=user_data["name"][mode_value]
      print(f'Your name is {result}')
    elif choice=="2":
       result=user_data["age"][mode_value]
       int(result)
       print(result)
    elif choice=="3":
        result=user_data["favorite_number"][mode_value]
        print(result)
    elif choice=="4":
        print("Goodbye")
        break


def user_mode():
   print("They is only three available user storage area,Tell me which you "
         "will like to use and i will tell you if is available")
   print('\n----Storage options----')
   print("User1")
   print("User2")
   print("User3")

   choice=input("Enter your choice:").lower().strip()
   while choice not in ["user1","user2","user3"]:
       print("invalid choice")
       choice=input("Enter your choice").lower().strip()
   if choice=="user1":
       return "user1"
   elif choice=="user2":
       return "user2"
   elif choice=="user3":
        return "user3"
   return None


#asking for which mode they like to use
value=user_mode()

#saving user input data
user_name = input("Enter your name:").lower().strip()
user_age = input("Enter your age:")
fav_number = input("Enter your favorite number and separated by a comma:")
# turning fav_number into a integer
fav_number = [int(f.strip()) for f in fav_number.split(",")]

user_data={"name":{},"age":{},"favorite_number":{}}

if value=="user1":
  #saving users input using user mode 1
  user_data["name"]["user1"]=user_name
  user_data["age"]["user1"]=user_age
  user_data["favorite_number"]["user1"]=fav_number

elif value=="user2":
    # saving users input user mode2
   user_data["name"]["user2"]=user_name
   user_data["age"]["user2"]=user_age
   user_data["favorite_number"]["user2"]=fav_number

elif value=="user3":
    #saving users input using user mode 3
    user_data["name"]["user3"]=user_name
    user_data["age"]["user3"]=user_age
    user_data["favorite_number"]["user3"]=fav_number

#
menu_option(value)
#AI Correction
#❗ IMPORTANT PROBLEM (this is the key learning moment)
#You recreate user_data AFTER choosing the user:
user_data={"name":{},"age":{},"favorite_number":{}}
#This means:
#If you save data for user1,
#Then run the program again and save for user2,
#You will erase user1's saved data because user_data starts empty every time.
#So your program cannot really store all 3 users — it only keeps one at a time.
#My attempt
import json
#--------- main menu------
def menu_option(mode_value):
  while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Exist")
    choice=input("Enter your choice:")
    if choice=="1":
      result=user_data["name"][mode_value]
      print(f'Your name is {result}')
    elif choice=="2":
       result=user_data["age"][mode_value]
       int(result)
       print(result)
    elif choice=="3":
        result=user_data["favorite_number"][mode_value]
        print(result)
    elif choice=="4":
        print("Goodbye")
        break


def user_mode():
   print("They is only three available user storage area,Tell me which you "
         "will like to use and i will tell you if is available")
   print('\n----Storage options----')
   print("User1")
   print("User2")
   print("User3")

   choice=input("Enter your choice:").lower().strip()
   while choice not in ["user1","user2","user3"]:
       print("invalid choice")
       choice=input("Enter your choice").lower().strip()
   if choice=="user1":
       return "users1"
   elif choice=="user2":
       return "users2"
   elif choice=="user3":
        return "users3"
   return None



#asking for which mode they like to use
value=user_mode()

#saving user input data
user_name = input("Enter your name:").lower().strip()
user_age = input("Enter your age:")
fav_number = input("Enter your favorite number and separated by a comma:")
# turning fav_number into a integer
fav_number = [int(f.strip()) for f in fav_number.split(",")]
#creating a storage to store user value
user_data={"user":value,"name":{},"age":{},"favorite_number":{}}
if value=="user1":
  # saving users input using user mode 1
  user_data["name"]["user1"] = user_name
  user_data["age"]["user1"]=user_age
  user_data["favorite_number"]["user1"]=fav_number
elif value=="user2":
   # saving users input user mode2
   user_data["name"]["user2"] = user_name
   user_data["age"]["user2"] = user_age
   user_data["favorite_number"]["user2"] = fav_number
elif value=="user3":
   # saving users input using user mode 3
   user_data["name"]["user3"] = user_name
   user_data["age"]["user3"] = user_age
   user_data["favorite_number"]["user3"] = fav_number

try:
   with open("Data_vault", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data={"users":{}}

#if user does not exist create it
if value not in data["users"]:
    data["users"][value]={"name":user_name,"age":user_age,"favorite_number":str(fav_number)}

with open("Data_vault","w") as file:
    json.dump(data,file,indent=4)
#
menu_option(value)
#AI correction
#import json
#⚠ Things to improve / bugs to fix
#1️⃣ User naming mismatch
#In user_mode(), you return "users1", "users2", "users3" (with an extra “s”).
#But in other places you use "user1", "user2", "user3".
#This will break checks like:
#if value not in data["users"]
#Fix: Make the naming consistent (user1, user2, user3).

#2️⃣ user_data resets every run
user_data={"user":value,"name":{},"age":{},"favorite_number":{}}

#Every time the program runs, this dictionary starts empty.
#You already save users in data["users"], so you don’t need user_data to store them again globally.
#Suggestion: Load users directly from data["users"] instead.

#3️⃣ Favorite numbers saved as string
#"favorite_number": str(fav_number)

#Storing numbers as string in JSON is unnecessary.
#You can store them as a list of integers, then load them back as list.
#"favorite_number": fav_number

#4️⃣ Menu still uses user_data
#result = user_data["name"][mode_value]
#After you add JSON storage, you should read from data["users"], not user_data.
#Otherwise, if the program restarts, all previous users are lost.

#✅ FEATURE 1 — Update User Data if User Already Exists
#Right now, your code ignores updating when user exists:
if value not in data["users"]:
    data["users"][value] = {...}
#We change it to:
#If user exists → ask: “Do you want to update this user?”
#If yes → overwrite values
#If no → keep old values
#✅ FEATURE 2 — Delete a User
#We add a new option in the menu:
#5) Delete this user
#If user chooses delete → remove from JSON → save file → exit to avoid errors.
#My Attempt
import json
#--------- main menu------
def menu_option(mode_value,user_value):
  while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Delete this user")
    print("5)Exit")
    choice=input("Enter your choice:")
    if choice=="1":
       result=user_value["users"][mode_value]["name"]
       print(result)

    elif choice=="2":
        result=user_value["users"][mode_value]["age"]
        print(result)

    elif choice=="3":
        result=user_value["users"][mode_value]["favorite_number"]
        print(result)

    elif choice=="4":
        print("User data has been deleted")
        return 'delete'

    elif choice=="4":
        print("Goodbye")
        break


def user_mode():
   print("They is only three available user storage area,Tell me which you "
         "will like to use and i will tell you if is available")
   print('\n----Storage options----')
   print("User1")
   print("User2")
   print("User3")

   choice=input("Enter your choice:").lower().strip()
   while choice not in ["user1","user2","user3"]:
       print("invalid choice")
       choice=input("Enter your choice").lower().strip()
   if choice=="user1":
       return "user1"
   elif choice=="user2":
       return "user2"
   elif choice=="user3":
        return "user3"
   return None

#asking for which mode they like to use
value=user_mode()

#saving user input data
user_name = input("Enter your name:").lower().strip()
user_age = input("Enter your age:")
fav_number = input("Enter your favorite number and separated by a comma:")
# turning fav_number into a integer
fav_number = [int(f.strip()) for f in fav_number.split(",")]
#creating a storage to store user value

try:
   with open("Data_vault", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data={"users":{}}

#if user does not exist create it
if value not in data["users"]:
    data["users"][value]={"name":user_name,"age":user_age,"favorite_number":fav_number}
    #saving data in file
    with open("Data_vault", "w") as file:
        json.dump(data, file, indent=4)

if value in data["users"]:
    print("Data already exists for "+value)
    question=input("Do you want to update this user?:").lower().strip()
    while question not in ["yes","no"]:
        question=input("Do you want to update this user?:")
    if question=="yes":
       data["users"][value]={"name":user_name,"age":user_age,"favorite_number":fav_number}
       print("Data updated")
       #saving new-data in file
       with open("Data_vault","w") as file:
           json.dump(data, file, indent=4)
       #reading saved file

    else:
        print("Data Entered will not be saved")
with open("Data_vault", "r") as file:
    user_data = json.load(file)

#
return_value=menu_option(value,user_data)
if return_value=="delete":
    with open("Data_vault","r") as file:
        delete_data=json.load(file)
        delete_data["users"][value]={"name":"test","age":"test","favorite_number":""}
    with open("Data_vault","w")as file:
         json.dump(delete_data,file,indent=4)

#AI CORRECTION
import json
#--------- main menu------
def menu_option(mode_value,user_value):
  while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Delete this user")
    print("5)Exit")
    choice=input("Enter your choice:")
    if choice=="1":
       result=user_value["users"][mode_value]["name"]
       print(result)

    elif choice=="2":
        result=user_value["users"][mode_value]["age"]
        print(result)

    elif choice=="3":
        result=user_value["users"][mode_value]["favorite_number"]
        print(result)

    elif choice=="4":
        ask=input("Are you sure you want to delete data stored in "+mode_value)
        if ask=="yes":
          with open ("Data_vault","r")as f:
              delete_data=json.load(f)
              del delete_data["users"][mode_value]
          with open("Data_vault","w")as f:
              json.dump(delete_data,f,indent=4)
          print("User data has been deleted")
          with open("Data_vault","r")as f:
               user_value=json.load(f)
          break

    elif choice=="5":
        print("Goodbye")
        break


def user_mode():
    with open("Data_vault", "r") as f:
        saved_data = json.load(f)
    while True:
         print("They is only three available user storage area,Tell me which you "
         "will like to use and i will tell you if is available")
         print('\n----Storage options----')
         print("User1")
         print("User2")
         print("User3")
         choice=input("Enter your choice:").lower().strip()
         while choice not in ["user1","user2","user3"]:
             print("invalid choice")
             choice = input("Enter your choice:").lower().strip()
         if choice not in saved_data["users"]:
             return choice
         else:
               print(f'Date already stored in{choice} ')
               continue

    return None

#asking for which mode they like to use
value=user_mode()

#saving user input data
user_name = input("Enter your name:").lower().strip()
user_age = input("Enter your age:")
fav_number = input("Enter your favorite number and separated by a comma:")
# turning fav_number into a integer
#creating a storage to store user value
fav_number = [int(f.strip()) for f in fav_number.split(",")]
try:
   with open("Data_vault", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data={"users":{}}

#if user does not exist create it
if value not in data["users"]:
    data["users"][value]={"name":user_name,"age":user_age,"favorite_number":fav_number}
    #saving data in file
    with open("Data_vault", "w") as file:
        json.dump(data, file, indent=4)


elif value in data["users"]:
    print("Data already exists for "+value)
    question=input("Do you want to update this user?:").lower().strip()
    while question not in ["yes","no"]:
        question=input("Do you want to update this user?:")
    if question=="yes":
       data["users"][value]={"name":user_name,"age":user_age,"favorite_number":fav_number}
       print("Data updated")
       #saving new-data in file
       with open("Data_vault","w") as file:
           json.dump(data, file, indent=4)
       #reading saved file

    else:
        print("Data Entered will not be saved")
with open("Data_vault", "r") as file:
    user_data = json.load(file)

#
menu_option(value,user_data)
#NEXT CHAllENGE(Level up)
#CHALLENGE: Add the ability to update only ONE field
#Example:
#Which field do you want to update?
#1) Name
#2) Age
#3) Favorite Number
#The user chooses ONE field, and only that field is updated in JSON.
#MY ATTEMPT
import json
#--------- main menu------
def menu_option(mode_value,user_value):
  while True:
    print("Here are the option Available to use")
    print("1)Check Name")
    print("2)Check age")
    print("3)Check favorite number")
    print("4)Delete this user")
    print("5)Update this user")
    print("6)Exit")
    choice=input("Enter your choice:")
    if choice=="1":
       result=user_value["users"][mode_value]["name"]
       print(result)

    elif choice=="2":
        result=user_value["users"][mode_value]["age"]
        print(result)

    elif choice=="3":
        result=user_value["users"][mode_value]["favorite_number"]
        print(result)

    elif choice=="4":
        ask=input("Are you sure you want to delete data stored in "+mode_value +":")
        if ask=="yes":
          with open ("Data_vault","r")as f:
              delete_data=json.load(f)
              del delete_data["users"][mode_value]
          with open("Data_vault","w")as f:
              json.dump(delete_data,f,indent=4)
          print("User data has been deleted")

          break

    elif choice=="5":
        print("What do you want to update?")
        print("1)Name")
        print("2)Age")
        print("3)Favorite Number")
        ask = input("Enter choice:")
        if ask not in ["1","2","3"]:
            ask = input("Enter choice:")
        with open("Data_vault","r")as f:
            if ask == "1":
              name_update = input("Enter new name:").strip().lower()
              loaded_data=json.load(f)
              loaded_data["users"][value]["name"] = name_update
            elif ask=="2":
                age_update=input("Enter new age:").strip().lower()
                loaded_data=json.load(f)
                loaded_data["users"][value]["age"]=age_update
            elif ask=="3":
                fav_update=int(input("Enter new fav_number:").strip().lower())
                fav_update=[fav_update]
                loaded_data=json.load(f)
                loaded_data["users"][value]["favorite_number"]=fav_update
        with open("Data_vault","w")as f:
            json.dump(loaded_data,f,indent=4)
        break


