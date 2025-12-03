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

