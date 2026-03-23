import json
import expense
from main import user_info

def save_to_json(expense_info):
    if not expense_info:
        return{"result":False,
               "error":["No expense data"],
               "data":None}

    storage_format = {"expense_amount": expense_info.amount,
                       "expense_description": expense_info.description,
                       "expense_data": expense_info.data,
                       "expense_category": expense_info.category}

    try:
        with open("expenses.json", "r") as file:
            expense_record = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        expense_record = []

    expense_record.append(storage_format)


    with open("expenses.json","w")as file:
        json.dump(expense_record,file, indent=4)

    return{"result":True,
           "error":None,
           "data":storage_format}

def create_object():
    user_amount, user_category, user_description, user_data = user_info()

    expense_details = expense.ExpenseObject(
        user_amount,
        user_category,
        user_description,
        user_data
    )

    if not expense_details:
        return {
            "result": False,
            "error": ["Failed to create an expense object"],
            "data": None
        }

    return {
        "result": True,
        "error": None,
        "data": expense_details
    }

#SAVE USER EXPENSE TO STORAGE
def data_storage():
    expense_info=create_object()
    if not expense_info["result"]:
        return{"result":False,
               "error":expense_info["error"],
               "data":None}
    data=expense_info["data"]

    formate_result=save_to_json(data)
    if not formate_result["result"]:
        return{"result":False,
               "error":formate_result["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":formate_result["data"]}


# CHECK ALL EXPENSE IN SAVE
def load_saved_data():
    try:
      with open("expenses.json","r")as file:
        expense_record=json.load(file)
        if expense_record:
           return {"result":True,
                "error":None,
                "data":expense_record}
        return{"result":False,
               "error":["No expense data found"]}
    except (FileNotFoundError,json.JSONDecodeError):
        return{"result":False,
               "error":["No expense record created yet"],
               "data":None}


def review_expense():
    expenses_info=load_saved_data()
    if not expenses_info["result"]:
        return{"result":False,
               "error":expenses_info["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":expenses_info["data"]}

def total_expense():
    total=0
    expense_info=load_saved_data()
    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        total+=each_expense["expense_amount"]
    return{"result":True,
           "error":None,
           "data":total}

def view_by_category(category):
    if not category:
        return{"result":False,
               "error":["No category was entered"],
               "data":None}

    category_list = []
    expense_info=load_saved_data()
    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        if category == each_expense["expense_category"]:
          category_list.append(each_expense)

    if category_list:
        return{"result":True,
               "error":None,
               "data":category_list}

    return{"result":False,
           "error":["Category can not be found in expenses record"],
           "data":None}

if __name__=="__main__":
    data_storage()
    
#SECOND ATTEMPT 
#REDESIGN FILE AS A RESULT OF Correction made on EXPENSE.PY
import json
import expense

def save_to_json(expense_info):
    if not expense_info:
        return{"result":False,
               "error":["No expense data"],
               "data":None}

    storage_format = expense_info.to_dict()


    try:
        with open("expenses.json", "r") as file:
            expense_record = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        expense_record = []

    expense_record.append(storage_format)


    with open("expenses.json","w")as file:
        json.dump(expense_record,file, indent=4)

    return{"result":True,
           "error":None,
           "data":storage_format}

def create_object(user_amount, user_category, user_description, user_date):

    expense_details = expense.ExpenseObject(
        user_amount,
        user_category,
        user_description,
        user_date)

    return {
        "result": True,
        "error": None,
        "data": expense_details
    }

#SAVE USER EXPENSE TO STORAGE
def data_storage(user_amount,user_category,user_description,user_date):
    expense_info=create_object(user_amount,user_category,user_description,user_date)

    if not expense_info["result"]:
        return{"result":False,
               "error":expense_info["error"],
               "data":None}
    data=expense_info["data"]

    formate_result=save_to_json(data)

    if not formate_result["result"]:
        return{"result":False,
               "error":formate_result["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":formate_result["data"]}


# CHECK ALL EXPENSE IN SAVE
def load_saved_data():
    try:
      with open("expenses.json","r")as file:
        expense_record=json.load(file)
        if expense_record:
           return {"result":True,
                "error":None,
                "data":expense_record}

        return{"result":False,
               "error":["No expense data found"],
               "data":None}

    except (FileNotFoundError,json.JSONDecodeError):
        return{"result":False,
               "error":["No expense record created yet"],
               "data":None}


def review_expense():
    expenses_info=load_saved_data()
    if not expenses_info["result"]:
        return{"result":False,
               "error":expenses_info["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":expenses_info["data"]}

def total_expense():
    total=0
    debug_test=[]
    expense_info=load_saved_data()

    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}

    for each_expense in expense_info["data"]:

        total+=each_expense.get("expense_amount")
    return{"result":True,
           "error":None,
           "data":total}

def view_by_category(category):
    if not category:
        return{"result":False,
               "error":["No category was entered"],
               "data":None}

    category_list = []
    expense_info=load_saved_data()
    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        if category == each_expense.get("expense_category"):
          category_list.append(each_expense)

    if category_list:
        return{"result":True,
               "error":None,
               "data":category_list}

    return{"result":False,
           "error":["Category can not be found in expenses record"],
           "data":None}
    if __name__=="__main__":
    total_expense()
    
    #AI CORRECTION 
#Issues / Problems
#1)create_object() function ignores validation
#expense_details = expense.ExpenseObject(...)
#return {"result": True, "error": None, "data": expense_details}
#Even if creation fails, it returns result: True
#Should wrap in try/except to catch ValueError from model

#2)Function naming / responsibilities
#data_storage() is confusing — it does:
#Create object
#Save to JSON
#Consider renaming to add_expense() to be clearer

#3)Redundant checks
#In data_storage():
#if not expense_info["result"]:

#4)Currently, create_object() always returns True → dead code
#Use of get() in total_expense() and view_by_category()
#Safe, but you assume JSON always has correct keys
#Could fail if JSON manually edited
#No separation between object creation and UI input
#Currently expense_manager depends on main.py to provide all 4 parameters
#This is okay for now, but in the future manager should handle defaults / validations

#THIRD ATTEMPT 
import json
import expense

def save_to_json(expense_info):
    if not expense_info:
        return{"result":False,
               "error":["No expense data"],
               "data":None}

    storage_format = expense_info.to_dict()


    try:
        with open("expenses.json", "r") as file:
            expense_record = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        expense_record = []

    expense_record.append(storage_format)


    with open("expenses.json","w")as file:
        json.dump(expense_record,file, indent=4)

    return{"result":True,
           "error":None,
           "data":storage_format}

def create_object(user_amount, user_category, user_description, user_date):
   try:
     expense_details = expense.ExpenseObject(
        user_amount,
        user_category,
        user_description,
        user_date)
   except ValueError:
       return {"result": False,
               "error": ["data enter was incorrect"],
               "data": None}


   return {
        "result": True,
        "error": None,
        "data": expense_details
    }

#SAVE USER EXPENSE TO STORAGE
def add_expense(user_amount, user_category, user_description, user_date):
    expense_info=create_object(user_amount,user_category,user_description,user_date)

    if not expense_info["result"]:
        return{"result":False,
               "error":expense_info["error"],
               "data":None}
    data=expense_info["data"]

    formatted_result=save_to_json(data)

    if not formatted_result["result"]:
        return{"result":False,
               "error":formatted_result["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":formatted_result["data"]}


# CHECK ALL EXPENSE IN SAVE
def load_saved_data():
    try:
      with open("expenses.json","r")as file:
        expense_record=json.load(file)
        if expense_record:
           return {"result":True,
                "error":None,
                "data":expense_record}

        return{"result":False,
               "error":["No expense data found"],
               "data":None}

    except (FileNotFoundError,json.JSONDecodeError):
        return{"result":False,
               "error":["No expense record created yet"],
               "data":None}


def review_expense():
    expenses_info=load_saved_data()
    if not expenses_info["result"]:
        return{"result":False,
               "error":expenses_info["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":expenses_info["data"]}

def total_expense():
    total=0
    expense_info=load_saved_data()

    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}

    for each_expense in expense_info["data"]:
        amount = each_expense.get("expense_amount")
        if amount is not None:
           total+= amount
        else:
            return{"result":False,
                   "error":["Key error key use to call amount doesn't exist"],
                   "data":None}

    return{"result":True,
           "error":None,
           "data":total}

def view_by_category(category):
    if not category:
        return{"result":False,
               "error":["No category was entered"],
               "data":None}

    category_list = []
    expense_info=load_saved_data()
    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        if category == each_expense.get("expense_category"):
          category_list.append(each_expense)

    if category_list:
        return{"result":True,
               "error":None,
               "data":category_list}

    return{"result":False,
           "error":["Category can not be found in expenses record"],
           "data":None}

if __name__=="__main__":
    total_expense()

#AI CORRECTION THIRD ATTEMPT
#⚠️ Issue 1 — Lost Useful Error Message
'''
Your current code:

except ValueError:
    return {
        "result": False,
        "error": ["data enter was incorrect"],
        "data": None
    }

Problem:
'''
#The real error message from the model is lost.
#Issue 2 — Repeated Dictionary Structures
#You repeatedly write:
#return {"result": False, "error": ..., "data": None}
#Not wrong, but eventually we would create a helper function like:
#success(data)
#failure(error)
#Not required now, but good to know.

#ISSUE3
#⚠️ Issue 3 — if not expense_info in save_to_json
#This check is unnecessary.
#Because save_to_json() only receives ExpenseObject.
#And ExpenseObject is always truthy.
#So this check will never trigger.
#Not a bug, just dead code.

#NEW CODING CHALLENGE
# Code-Redesign For new Project 2 — Expense Manager v2
import json
import expense
from typing import List,Dict
from datetime import datetime

from expense import ExpenseObject


def save_to_json(expense_info):
    storage_format = expense_info.to_dict()

    try:
        with open("expenses.json", "r") as file:
            expense_record = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        expense_record = []

    expense_record.append(storage_format)


    with open("expenses.json","w")as file:
        json.dump(expense_record,file, indent=4)

    return{"result":True,
           "error":None,
           "data":storage_format}

def create_object(user_amount, user_category, user_description, user_date):
    # LOAD SAVED JSON AND GET LAST SAVED ID NUMBER
    last_saved_id = ""
    expense_info = load_saved_data()
    if expense_info["result"]:
        data = expense_info["data"]
        for each_expense in data:
            last_saved_id = each_expense.get("expense_id")

        # ADD IT TO THE CURRENT ID OBJECT CREATED
    try:
       expense_details = expense.ExpenseObject(
           user_amount,
           user_category,
           user_description,
           user_date,
           last_saved_id)

    except ValueError as e:
       return {"result": False,
               "error": [str(e)],
               "data": None}



    return {
        "result": True,
        "error": None,
        "data": expense_details
    }

#SAVE USER EXPENSE TO STORAGE
def add_expense(user_amount, user_category, user_description, user_date):
    expense_info : Dict[str,bool|ExpenseObject]=create_object(user_amount,user_category,user_description,user_date)

    if not expense_info["result"]:
        return{"result":False,
               "error":expense_info["error"],
               "data":None}
    data=expense_info["data"]


    formatted_result=save_to_json(data)

    if not formatted_result["result"]:
        return{"result":False,
               "error":formatted_result["error"],
               "data":None}

    return{"result":True,
           "error":None,
           "data":formatted_result["data"]}


# CHECK ALL EXPENSE IN SAVE
def load_saved_data():
    try:
      with open("expenses.json","r")as file:
        expense_record=json.load(file)
        if expense_record:
           return {"result":True,
                "error":None,
                "data":expense_record}

        return{"result":False,
               "error":["No expense data found"],
               "data":None}

    except (FileNotFoundError,json.JSONDecodeError):
        return{"result":False,
               "error":["No expense record created yet"],
               "data":None}


def review_expense():
    expenses_info=load_saved_data()
    if not expenses_info["result"]:
        return{"result":False,
               "error":expenses_info["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":expenses_info["data"]}

def total_expense():
    total=0
    expense_info=load_saved_data()

    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}

    for each_expense in expense_info["data"]:
        amount = each_expense.get("expense_amount")
        if amount is not None:
           total+= amount
        else:
            return{"result":False,
                   "error":["Key error key use to call amount doesn't exist"],
                   "data":None}

    return{"result":True,
           "error":None,
           "data":total}

def view_by_category(category):
    if not category:
        return{"result":False,
               "error":["No category was entered"],
               "data":None}

    category_list = []
    expense_info=load_saved_data()
    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        if category == each_expense.get("expense_category"):
          category_list.append(each_expense)

    if category_list:
        return{"result":True,
               "error":None,
               "data":category_list}

    return{"result":False,
           "error":["Category can not be found in expenses record"],
           "data":None}
def delete_expense(index_num):
    try:
        index_num=int(index_num)
    except ValueError:
        return{"result":False,
               "error":["Id number must be a whole number"],
               "data":None}

    expenses_info =load_saved_data()
    if not expenses_info["result"]:
       return {"result": False,
               "error": expenses_info["error"],
               "data": None}
    data=expenses_info["data"]
    for each_expense in data:
       if index_num == each_expense.get("expense_id"):
           data.remove( each_expense)
           break
    else:
       return {"result": False,
               "error": ["Expense ID not found"],
               "data": None}

    with open("expenses.json","w") as file:
       json.dump(data,file,indent=4)

    return{"result":True,
          "error":None,
          "data":each_expense}

def edit_saved_expense(id_num, field, new_value):
    expenses_info :Dict = load_saved_data()
    if not expenses_info["result"]:
        return {"result": False,
                "error": expenses_info["error"],
                "data": None}
# : List[Dict] TELL EDITOR AND ANYBODY LOOK WHAT CONTAIN INSIDE EXPENSE_INFO[DATA]
    data: List[Dict] = expenses_info["data"]

    for index_num, each_expense in enumerate(data):
        if id_num == each_expense.get("expense_id"):
           if each_expense.get(field) is None:
              return {"result": False,
                      "error": [field + " those not exist in expense"],
                      "data": None}

           amount = each_expense.get("expense_amount")
           describe = each_expense.get("expense_description")
           category=each_expense.get("expense_category")
           date=each_expense.get( "expense_date")
           if field=="expense_amount":
               amount=new_value
           elif field=="expense_description":
               describe=new_value
           elif field=="expense_category":
               category=new_value
           else:
               date=new_value

           new_expense = expense.ExpenseObject(amount, category, describe, date)
           new_expense.expense_id=each_expense.get("expense_id")
           dict_format=new_expense.to_dict()

           data[index_num] =dict_format

           with open("expenses.json", "w") as file:
               json.dump(data, file, indent=4)

           return{"result":True,
                  "error":None,
                  "data":dict_format}
    else:
          return{"result":False,
               "error":["ID number those not exist"],
               "data":None}

def monthly_summary(month):
    monthly_details={}
    found=False
    expenses_info = load_saved_data()

    if not expenses_info["result"]:
        return {"result": False,
                "error": expenses_info["error"],
                "data": None}

    data = expenses_info["data"]

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        return{"result":False,
               "error":["Wrong format,format should be(YYYY-MM)"],
               "data":None}

    for each_expense in data:
        each_date=each_expense.get("expense_date")

        if month==each_date[:7]:
            found= True
            category=each_expense.get("expense_category")
            amount=each_expense.get("expense_amount")

            monthly_details[category]=amount
    if found:
       return {"result": True,
            "error": None,
            "data": monthly_details}

    return{"result":None,
           "error":["Date not found in record"],
           'data':None}




if __name__=="__main__":
    result=edit_saved_expense(5,"expense_amount",3000)
    if result["result"]:
        print(result["data"])
    else:
        print(result["error"])
        
#Second attempt 
#REDESIGN FILE AS A RESULT OF Correction made on expense.py
expense_manager.py
import json
import expense
from typing import List,Dict
from datetime import datetime
from expense import ExpenseObject

def save_to_json(expense_info):
    storage_format = expense_info.to_dict()
    try:
        with open("expenses.json", "r") as file:
            expense_record = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        expense_record = []
    expense_record.append(storage_format)
    with open("expenses.json","w")as file:
        json.dump(expense_record,file, indent=4)
    return{"result":True,
           "error":None,
           "data":storage_format}
def create_object(user_amount, user_category, user_description, user_date):
    # LOAD SAVED JSON AND GET LAST SAVED ID NUMBER
    new_id = ""
    expense_info = load_saved_data()
    if expense_info["result"]:
        data = expense_info["data"]
        ids=[each_expense.get("expense_id",0)for each_expense in data]
        max_id=max(ids,default=0)
        new_id = max_id + 1
        # ADD IT TO THE CURRENT ID OBJECT CREATED
    try:
       expense_details = expense.ExpenseObject(
           user_amount,
           user_category,
           user_description,
           user_date,
           new_id)

    except ValueError as e:
       return {"result": False,
               "error": [str(e)],
               "data": None}
    return {
        "result": True,
        "error": None,
        "data": expense_details
    }

#SAVE USER EXPENSE TO STORAGE
def add_expense(user_amount, user_category, user_description, user_date):
    expense_info : Dict[str,bool|ExpenseObject]=create_object(user_amount,user_category,user_description,user_date)
    if not expense_info["result"]:
        return{"result":False,
               "error":expense_info["error"],
               "data":None}
    data=expense_info["data"]
    formatted_result=save_to_json(data)

    if not formatted_result["result"]:
        return{"result":False,
               "error":formatted_result["error"],
               "data":None}

    return{"result":True,
           "error":None,
           "data":formatted_result["data"]}
# CHECK ALL EXPENSE IN SAVE
def load_saved_data():
    try:
      with open("expenses.json","r")as file:
        expense_record=json.load(file)
        if expense_record:
           return {"result":True,
                "error":None,
                "data":expense_record}

        return{"result":False,
               "error":["No expense data found"],
               "data":None}

    except (FileNotFoundError,json.JSONDecodeError):
        return{"result":False,
               "error":["No expense record created yet"],
               "data":None}

def review_expense():
    expenses_info=load_saved_data()
    if not expenses_info["result"]:
        return{"result":False,
               "error":expenses_info["error"],
               "data":None}
    return{"result":True,
           "error":None,
           "data":expenses_info["data"]}

def total_expense():
    total=0
    expense_info=load_saved_data()

    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        amount = each_expense.get("expense_amount")
        if amount is not None:
           total+= amount
        else:
            return{"result":False,
                   "error":["Key error key use to call amount doesn't exist"],
                   "data":None}

    return{"result":True,
           "error":None,
           "data":total}

def view_by_category(category):
    if not category:
        return{"result":False,
               "error":["No category was entered"],
               "data":None}

    category_list = []
    expense_info=load_saved_data()
    if not expense_info["result"]:
        return {"result": False,
                "error": expense_info["error"],
                "data": None}
    for each_expense in expense_info["data"]:
        if category == each_expense.get("expense_category"):
          category_list.append(each_expense)

    if category_list:
        return{"result":True,
               "error":None,
               "data":category_list}

    return{"result":False,
           "error":["Category can not be found in expenses record"],
           "data":None}
def delete_expense(index_num):
    try:
        index_num=int(index_num)
    except ValueError:
        return{"result":False,
               "error":["Id number must be a whole number"],
               "data":None}

    expenses_info =load_saved_data()
    if not expenses_info["result"]:
       return {"result": False,
               "error": expenses_info["error"],
               "data": None}
    data=expenses_info["data"]
    for each_expense in data:
       if index_num == each_expense.get("expense_id"):
           data.remove( each_expense)
           break
    else:
       return {"result": False,
               "error": ["Expense ID not found"],
               "data": None}

    with open("expenses.json","w") as file:
       json.dump(data,file,indent=4)

    return{"result":True,
          "error":None,
          "data":each_expense}

def edit_saved_expense(id_num, field, new_value):
    expenses_info :Dict = load_saved_data()
    if not expenses_info["result"]:
        return {"result": False,
                "error": expenses_info["error"],
                "data": None}
# : List[Dict] TELL EDITOR AND ANYBODY LOOK WHAT CONTAIN INSIDE EXPENSE_INFO[DATA]
    data: List[Dict] = expenses_info["data"]

    for index_num, each_expense in enumerate(data):
        if id_num == each_expense.get("expense_id"):
           if each_expense.get(field) is None:
              return {"result": False,
                      "error": [field + " those not exist in expense"],
                      "data": None}

           amount = each_expense.get("expense_amount")
           describe = each_expense.get("expense_description")
           category=each_expense.get("expense_category")
           date=each_expense.get( "expense_date")
           if field=="expense_amount":
               amount=new_value
           elif field=="expense_description":
               describe=new_value
           elif field=="expense_category":
               category=new_value
           else:
               date=new_value

           new_expense = expense.ExpenseObject(amount, category, describe, date)
           new_expense.expense_id=each_expense.get("expense_id")
           dict_format=new_expense.to_dict()

           data[index_num] =dict_format

           with open("expenses.json", "w") as file:
               json.dump(data, file, indent=4)

           return{"result":True,
                  "error":None,
                  "data":dict_format}
    else:
          return{"result":False,
               "error":["ID number those not exist"],
               "data":None}

def monthly_summary(month):
    monthly_details={}
    found=False
    expenses_info = load_saved_data()

    if not expenses_info["result"]:
        return {"result": False,
                "error": expenses_info["error"],
                "data": None}

    data = expenses_info["data"]

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        return{"result":False,
               "error":["Wrong format,format should be(YYYY-MM)"],
               "data":None}

    for each_expense in data:
        each_date=each_expense.get("expense_date")

        if month==each_date[:7]:
            found= True
            category=each_expense.get("expense_category")
            amount=each_expense.get("expense_amount")

            monthly_details[category]=amount
    if found:
       return {"result": True,
            "error": None,
            "data": monthly_details}

    return{"result":None,
           "error":["Date not found in record"],
           'data':None}

if __name__=="__main__":
    result=edit_saved_expense(5,"expense_amount",3000)
    if result["result"]:
        print(result["data"])
    else:
        print(result["error"])

