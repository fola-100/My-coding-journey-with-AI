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




    
