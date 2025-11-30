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