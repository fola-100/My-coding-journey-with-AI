class ExpenseObject:
    def __init__(self,amount,category,description,data):
        self.amount=amount
        self.category=category
        self.description=description
        self.data=data
#AI CORRECTION ON FIRST ATTEMPT 
#There are several design and architecture problems here.
#Problem 1 — Attribute name mistake
#You used:
#data
#But the field represents:
#date
#This causes confusion in the entire system.
#Example in expense_manager.py:
#expense_info.data
#Someone reading the code will think it means data, not date.

#Problem 2 — Missing Validation
#Your design document said:
#Validation rules:
#amount > 0
#category cannot be empty
#date defaults to today
#But the class does none of this.
#Right now this code would allow:
#ExpenseObject(-500,"","",None)
#Which breaks the system.
#Validation belongs inside the model.

#Problem 3 — No Date Handling
#Your class does not handle date logic.
#The requirement was:
#If date not provided → use today's date
#This is missing.

#Problem 4 — No Dictionary Conversion Method
#The design required:
#include a method that converts the object into a dictionary so it can be saved to JSON.
#Your class does not provide this.
#So expense_manager.py had to manually build dictionaries:
storage_format = {
    "expense_amount": expense_info.amount
}
#This breaks separation of responsibility.
#The model should know how to represent itself.
#Problem 5 — No Type Safety
#The class does not ensure:
#amount is a number
#category is text
#So invalid objects can exist.
#How These Problems Affect Other Files
#These mistakes forced bad design in expense_manager.py.
#Example:
#Instead of:
#expense.to_dict()
#You had to manually do:
#storage_format = {...}
#This makes the code:
#harder to maintain
#easier to break
#harder to extend later
#What This Class Should Be Responsible For
#The Expense model should handle:
#storing expense data
#validating expense data
#managing default date
#converting itself to dictionary

#SECOND ATTEMPT 
class ExpenseObject:
    def __init__(self,amount,category,description,date):
        if amount<=0 or not isinstance(amount,int):
            raise ValueError("amount must be greater than zero")
        if not category or not isinstance(category,str):
            raise ValueError("Expense category was not entered")
        if not description or not isinstance(description,str):
            raise ValueError("NO description on expense what entered")

        self.amount=amount
        self.category=category
        self.description=description
        self.date=date

    def to_dict(self):
        return {"expense_amount": self.amount,
                       "expense_description": self.description,
                          "expense_date": self.date,
                          "expense_category":self.category} 

# AI CORRECTION 
#1)Requirement from design:
#If date is not provided → use today's date.
#Your class does not handle this.
#Right now it requires:
#ExpenseObject(amount, category, description, date)
#If date is None, the object will store None.
#This logic belongs inside the model.

#2)Problem 2 — Over-strict Amount Validation
#You wrote:
not isinstance(amount, int)
#But money values can be:
#500
#500.0
#Your code rejects floats.
#Better validation:
#int or float

#3)Problem 3 — String Validation Weakness
#You check:
#not isinstance(category,str)
#But this allows:
#"    "
#An empty string after stripping.
#Problem 4 — Model Should Normalize Data
#Right now the class trusts external input.
#Example:
#"Food"
#"FOOD"
#The model could normalize:
#category.lower()
# FULL AI CORRECTION 

#REDESIGN FILE for Project 2 — Expense Manager v2
from datetime import datetime

class ExpenseObject:

    def __init__(self, amount, category=None, description=None, date=None, id_created=None):
       expense_created = 1
       if id_created:
          try:
              int(id_created)
          except ValueError:
              raise ValueError("ID must be a whole number")

          expense_created+=id_created


       if not category or not isinstance(category, str):
            raise ValueError("Expense category was not entered or category was not a string")
       if not description or not isinstance(description, str):
            raise ValueError("NO description on expense what entered or description was not a string")
     # ENSURE DATA CONTAIN NO SPACE
       category = category.strip().lower()
       description = description.strip().lower()

       if not isinstance(amount,(int,float)):
            raise ValueError("Your number can only be float or integer")

       if amount<=0 :
            raise ValueError("amount must be greater than zero")

       if date:
            try:
              datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("date must follow this format(YYYY-MM-DD)")

       if not date:
        date=datetime.now().strftime("%Y-%m-%d")
       self.amount = amount
       self.expense_id =  expense_created
       self.category = category
       self.description = description
       self.date = date

    def to_dict(self):
        return {"expense_id":self.expense_id,
            "expense_amount": self.amount,
                       "expense_description": self.description,
                          "expense_date": self.date,
                          "expense_category":self.category} 
 #AI CORRECTIOIN 
#❌ Problem 1 — ID Logic is Wrong
#Your code:
#expense_created = 1
#if id_created:
#    expense_created += id_created
#Why this is wrong
#Example:
#last id = 5
#new id = 1 + 5 = 6 ✅ (works)
#BUT...
#What if JSON is:
#[1, 2, 5]   (missing 3,4)
#Your logic → still gives 6 ❌ (not always safe)
#Worse problem:
#expense_created = 1  # resets every time object is created
#So ID logic is not persistent or reliable.

#❌ Problem 2 — Model Should NOT Control ID Generation
#This is a big architecture mistake.
#expense_manager → passes id
#expense_object → modifies id
#That’s confusion.
#Correct Design:
#👉 Model should NOT generate IDs
#👉 Manager should generate IDs

#❌ Problem 3 — ID Validation is Weak
#You wrote:
#if id_created:
#This fails for:
#id_created = 0
#Because 0 is falsy

#❌ Problem 4 — Naming Confusion
#expense_created
#id_created
#expense_id
#Too many similar names → easy to confuse.

#SECOND ATTEMPT 
from datetime import datetime

class ExpenseObject:

    def __init__(self, amount, category=None, description=None, date=None, id_created=0):
       if id_created :
         id_created = int(id_created)

       if not category or not isinstance(category, str):
            raise ValueError("Expense category was not entered or category was not a string")
       if not description or not isinstance(description, str):
            raise ValueError("NO description on expense what entered or description was not a string")
     # ENSURE DATA CONTAIN NO SPACE
       category = category.strip().lower()
       description = description.strip().lower()

       if not isinstance(amount,(int,float)):
            raise ValueError("Your number can only be float or integer")

       if amount<=0 :
            raise ValueError("amount must be greater than zero")

       if date:
            try:
              datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("date must follow this format(YYYY-MM-DD)")

       if not date:
        date=datetime.now().strftime("%Y-%m-%d")
       self.amount = amount
       self.expense_id = id_created
       self.category = category
       self.description = description
       self.date = date

    def to_dict(self):
        return {"expense_id":self.expense_id,
            "expense_amount": self.amount,
                       "expense_description": self.description,
                          "expense_date": self.date,
                          "expense_category":self.category}

