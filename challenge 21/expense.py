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
