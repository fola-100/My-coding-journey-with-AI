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

#AI CORRECTION ON SECOND ATTEMPT 

#⚠️ Minor Issues Remaining
#These are not blocking, just improvements.
#Issue 1 — Menu Option Validation
#Right now:
#option = input("Enter option number:")
#If user enters:
#abc, 10,blank
#It still passes to logic.

#Issue 2— Printing raw data
#Right now when viewing expenses:
#print(result["data"])
#This prints raw JSON-style dictionaries.
#Example output:S
#Food | 500 | 2026-03-17 | Lunch

#NEW PROJECT2
#REDESIGN FILE for Project 2 — Expense Manager version2
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
    category = input("What type of expense was made:").strip().lower()
    while not category:
        print("Expense category was not entered")
        category = input("What type of expense was made:").strip().lower()
    return category


def get_description():
    description = input("Explain what expense was on:").strip().lower()
    while not description:
        print("NO description on expense what entered")
        description = input("Explain what expense was on:").strip().lower()
    return description


def get_date():
    while True:
        print("Enter in date when expense was made or current date will be used")
        date = input("Date format:YYYY-MM-DD:").strip()
        if not date:
            return date
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Date format is wrong")


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
           print("1)amount")
           print("2)category")
           print("3)description")
           print("4)date")
           option=input(">:")
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

def account_info():
    id_num = int(input("Enter in the expense id you want to edit:"))
    while not id_num:
        id_num = int(input("Enter in the expense id you want to edit:"))

    print("What category do you want to edit")
    print("amount")
    print("description")
    print("date")
    print("category")
    category=input(">:")
    while not category or category not in ["amount","description","date","category"]:
        category=input("What category do you want to edit:")
    if category =="amount":
        category="expense_amount"

    elif category=="description":
        category="expense_description"

    elif category=="date":
        category="expense_date"

    elif category=="category":
        category="expense_category"


    value=int(input("Enter in category new value:"))
    while not value:
        value = int(input("Enter in category new value:"))

    return id_num, category, value

def edit_expense():
    id_num, category, value = account_info()
    result = expense_manager.edit_saved_expense(id_num, category,value)
    return result

def monthly_expense():
    print("Enter in the month you want to see in this format(YYYY-MM)")
    month=input(">:")
    while not month:
        print("No month entered")
        print("Enter in the month you want to see in this format(YYYY-MM)")
        month = input(">:")
    while True:
        try:
          datetime.strptime(month,"%Y-%m")
          break
        except ValueError:
            print("Wrong formate Enter in the month you want to see in this format(YYYY-MM)")
            month = input(">:")
    return expense_manager.monthly_summary(month)




def menu():
   while True:
       print("\n----Option_menu----")
       print("1)Add expense:")
       print("2)View expenses")
       print("3)Show total expenses ")
       print("4)Filter by category")
       print("5)Delete expense")
       print("6)Edit expense")
       print("7)View expense by month")
       print("8)Exit")

       option = input("Enter option number:")
       while option not in ["1","2","3","4","5","6","7","8"]:
           option = input("Enter option number:")
       if option == "1":
           user_amount, user_category, user_description, user_date = user_info()
           result = expense_manager.add_expense(user_amount, user_category, user_description, user_date)

           if not result["result"]:
               print(result["error"])
           else:
               data = result["data"]
               user_id=data.get("expense_id")
               amount=data.get("expense_amount")
               date=data.get("expense_date")
               description=data.get("expense_description")
               category=data.get("expense_category")

               print("ID|CATEGORY|AMOUNT|DATE|DESCRIPTION")
               print(f'{user_id} |{ amount} |{date} |{description} |{category} ')

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

       elif option=="5":
           id_number=input("Enter in ID of expense to be deleted:")
           option= input("Are you sure you want to delete "+id_number+" :").lower().strip()
           while option not in ["yes","no"]:
               option = input("Are you sure you want to delete " + id_number + " :").lower().strip()
           if option=="yes":
             result=expense_manager.delete_expense(id_number)
             if not result["result"]:
               print(result["error"])
             else:
               print("EXPENSE INFO DELETED SUCCESSFULLY")
           else:
               continue

       elif option=="6":
          result=edit_expense()
          if not result["result"]:
              print(result["error"])
          else:
              print(result["data"])

       elif option=="7":
           result=monthly_expense()
           if not result["result"]:
               print(result["error"])
           else:
               print(result["data"])

       elif option == "8":
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

#AI CORRECTION ON REDESING MADE FROM Expense Manager version2
#✅ 4. FIX: delete ID type inconsistency (small but important)
#🔧 Replace:
#id_number=input("Enter in ID of expense to be deleted:")
#✅ With:
#id_number = input("Enter in ID of expense to be deleted:").strip()
#(Prevents hidden spaces causing bugs)
✅ 3. FIX: Wrong table display order
#❌ You wrote:
#print("ID|CATEGORY|AMOUNT|DATE|DESCRIPTION")
#print(f'{user_id} |{ amount} |{date} |{description} |{category} ')
#👉 Order is wrong
#✅ Fix:
#print("ID|CATEGORY|AMOUNT|DATE|DESCRIPTION")
#print(f'{user_id} |{category} |{amount} |{date} |{description}')
#✅ 1. FIX: account_info() (BIG BUG)
#❌ Problem:
#You force everything to int, even description/category.
#🔧 Replace this:
#value=int(input("Enter in category new value:"))
#while not value:
#    value = int(input("Enter in category new value:"))








