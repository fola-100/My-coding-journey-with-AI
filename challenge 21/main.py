import expense_manager
from datetime import datetime

def get_amount():
    while True:
        try:
           amount=int(input("Enter in amount expense:"))
           if amount > 0:
               return amount
           print("Amount must be greater than zero")
        except ValueError:
           print("Amount enter must be a whole number")

def get_category():
    while True:
        category=input("What type of expense was made:").strip().lower()
        if not category:
            print("Expense category was not entered")
            category = input("What type of expense was made:").strip().lower()
        return category

def get_description():
    while True:
        description = input("Explain what expense was on:").strip().lower()
        if not description:
            print("NO description on expense what entered")
            description = input("Explain what expense was on:").strip().lower()
        return description

def get_date():
    while True:
        print("Enter in date when expense was made or current date will be used")
        date = input("Date format:YYYY-MM-DD:").strip()
        if not date:
           return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")


def user_info():
    amount=get_amount()
    category=get_category()
    description=get_description()
    date=get_date()
    while True:
        edit=input("Do you want to change any info entered?:")
        while edit not in["yes","no"]:
             edit = input("Do you want to change any info entered?:")
        if edit=="yes":
           print("Edit options")
           option=input("(1)amount),(2)category),(3)description),4)date):")
           if option=="1":
               amount=get_amount()
           elif option=="2":
                category=get_category()
           elif option=="3":
                description=get_description()
           elif option=="4":
                date=get_date()
        else:
            break

    return amount, category, description, date


def menu():
   while True:
       print("\n----Option_menu----")
       print("1)Add expense:")
       print("2)View expenses")
       print("3) Show total expenses ")
       print("4)Filter by category")
       print("5)Exist")
       option = input("Enter option number:")
       if option == "1":
           result = expense_manager.data_storage()
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "2":
           result = expense_manager.review_expense()
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "3":
           result = expense_manager.total_expense()
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "4":
           category = input("What category do you want to see:").strip().lower()
           result = expense_manager.view_by_category(category)
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "5":
           check = input("Are you sure you want to close the program?:").lower().strip()
           while check not in  ["yes","no"]:
               check = input("Are you sure you want to close the program?:").lower().strip()

           if check == "yes":
               print("Good bye")
               break
       else:
           print("Number entered is not part of the available option ")


if __name__=="__main__":
   menu()
    
#SECOND ATTEMPT 
# REDESIGN FILE AS A RESULT OF Correction made on expense.py

main.py
import expense_manager
from datetime import datetime

def get_amount():
    while True:
        try:
           amount=int(input("Enter in amount expense:"))
           if amount > 0:
               return amount
           print("Amount must be greater than zero")
        except ValueError:
           print("Amount enter must be a whole number")

def get_category():
    while True:
        category=input("What type of expense was made:").strip().lower()
        if not category:
            print("Expense category was not entered")
            category = input("What type of expense was made:").strip().lower()
        return category

def get_description():
    while True:
        description = input("Explain what expense was on:").strip().lower()
        if not description:
            print("NO description on expense what entered")
            description = input("Explain what expense was on:").strip().lower()
        return description

def get_date():
    while True:
        print("Enter in date when expense was made or current date will be used")
        date = input("Date format:YYYY-MM-DD:").strip()
        if not date:
           return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")


def user_info():
    amount=get_amount()
    category=get_category()
    description=get_description()
    date=get_date()
    while True:
        edit=input("Do you want to change any info entered?:")
        while edit not in["yes","no"]:
             edit = input("Do you want to change any info entered?:")
        if edit=="yes":
           print("Edit options")
           option=input("(1)amount),(2)category),(3)description),4)date):")
           if option=="1":
               amount=get_amount()
           elif option=="2":
                category=get_category()
           elif option=="3":
                description=get_description()
           elif option=="4":
                date=get_date()
        else:
            break

    return amount, category, description, date


def menu():
   while True:
       print("\n----Option_menu----")
       print("1)Add expense:")
       print("2)View expenses")
       print("3) Show total expenses ")
       print("4)Filter by category")
       print("5)Exist")
       option = input("Enter option number:")
       if option == "1":
           user_amount, user_category, user_description, user_date = user_info()
           result = expense_manager.data_storage(user_amount,user_category,user_description,user_date)

           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "2":
           result = expense_manager.review_expense()
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "3":
           result = expense_manager.total_expense()
           print(result)
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "4":
           category = input("What category do you want to see:").strip().lower()
           result = expense_manager.view_by_category(category)
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "5":
           check = input("Are you sure you want to close the program?:").lower().strip()
           while check not in  ["yes","no"]:
               check = input("Are you sure you want to close the program?:").lower().strip()

           if check == "yes":
               print("Good bye")
               break
       else:
           print("Number entered is not part of the available option ")


if __name__=="__main__":
   menu()


