# Challenge: Currency Converter
# Task from AI Tutor (ChatGPT):
# Write a Python program that:
# - Asks the user which conversion they want to do:
#     1. Naira → Dollar
#     2. Dollar → Naira
#     3. Exit
# - Uses functions to handle each conversion.
# - Assume 1 Dollar = 1500 Naira.
# - Keeps running in a loop until Exit.
# - Bonus: Handle wrong inputs, format results neatly.
# ❌ My Attempt
def dollar_conversion(value):
    return value * 1500

def naira_conversion(value):
    return value / 100   # mistake: wrong conversion rate

while True:
    print("----Menu Conversion option----")
    print("convert dollar to naira (1)")
    print("convert naira to dollar(2)")
    print("Exit(3)\n")

    choice = input("what would you like to do?:").strip().lower()
    if choice not in ["1", "2", "3"]:
        print("invalid option")
        continue

    if choice == "1":
        amount = float(input("Enter the amount you want to convert:"))
        b = dollar_conversion(amount)
        print(f'convert {amount} to dollar is {b}')
    elif choice == "2":
        amount = float(input("Enter the amount you want to convert:"))
        z = naira_conversion(amount)
        print(f'convert {amount} to naira is {z}')
    elif choice == "3":
        print("Goodbye!")
        exit()
      
Corrected Version (after AI Tutor feedback)
def dollar_conversion(value):
    return value * 1500

def naira_conversion(value):
    return value / 1500   # corrected rate

while True:
    print("\n---- Menu Conversion Option ----")
    print("1. Convert Dollar to Naira")
    print("2. Convert Naira to Dollar")
    print("3. Exit\n")

    choice = input("What would you like to do?: ").strip()

    if choice not in ["1", "2", "3"]:
        print("Invalid option, please try again.")
        continue

    if choice == "1":
        amount = float(input("Enter the Dollar amount: "))
        result = dollar_conversion(amount)
        print(f"{amount} Dollars = {result:.2f} Naira")

    elif choice == "2":
        amount = float(input("Enter the Naira amount: "))
        result = naira_conversion(amount)
        print(f"{amount} Naira = {result:.2f} Dollars")

    elif choice == "3":
        print("Goodbye!")
        break
