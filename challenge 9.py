#💰 Budget Tracker Game – Stage 1: The Basics
#Create a simple program where the user can:
#View total balance
#Add income or expense
#View transaction history
#Exit the program
#Each transaction will be saved in a file called budget.txt — so data isn’t lost when you close the program.
print("Welcome to Budget Tracker")
while True:
    print("---Option available---")
    print("1.)Add income")
    print("2.)Add Expense")
    print("3.)View Balance")
    print("4).View Transactions")
    print("5).Exit")
    choice=input("What do you want to do?:")
    if choice=="1":
       amount=float(input("How much is your income?:"))
      #reading turning file to a float and adding new value to balance
       try:
          with open("balance.txt","r") as file:
              content=file.read().strip()
              balance=float(content) if content else 0.0
       except FileNotFoundError:
           balance=0.0
       balance+=amount
       #turing add updated balance to the balance file
       with open("balance.txt","w") as file:
           file.write(str(balance))
           # saving change in balance
           print(f'"Your total balance after adding {amount} is {balance}')
       with open("transactions.txt","a") as file:
           file.write(f'\n+{amount}={balance}')

    elif choice=="2":
       amount=float(input("Enter the amount spend on expense:"))
       #reading turning file to a float and adding new value to balance
       with open("balance.txt","r") as file:
          content=file.read().strip()
          balance=float(content)
          if balance>amount:
            balance-=amount
          else:
             print(f'{amount} is to low to remove from balance')
      #storing balance after removing from amount from balance
       with open("balance.txt","w") as file:
         file.write(str(balance)+" \n")
         print(f'Your total balance after adding {amount} is  {balance}')
      #Recording transaction history
       with open("transactions.txt","a") as file:
           file.write(f'-{amount}={balance}')

    elif choice=="3":
        with open("balance.txt","r")as file:
            file=file.read()
            print(f'\nYour total balance is {file}')

    elif choice=="4":
        with open("transactions.txt","r")as file:
            file=file.read()
            print(f"\nYour total balance is {file}")

    elif choice=="5":
        print("Thank you for using our application")
        exit()
      
#AI Tutor Correction
print("Welcome to Budget Tracker 💰")

while True:
    print("\n--- Options Available ---")
    print("1) Add Income")
    print("2) Add Expense")
    print("3) View Balance")
    print("4) View Transactions")
    print("5) Exit")

    choice = input("What do you want to do?: ")

    # --- ADD INCOME ---
    if choice == "1":
        amount = float(input("Enter income amount: ₦"))
        try:
            with open("balance.txt", "r") as file:
                content = file.read().strip()
                balance = float(content) if content else 0.0
        except FileNotFoundError:
            balance = 0.0

        balance += amount

        with open("balance.txt", "w") as file:
            file.write(str(balance))

        print(f"✅ Added ₦{amount}. New balance is ₦{balance}.")

        with open("transactions.txt", "a") as file:
            file.write(f"+{amount} → balance: {balance}\n")

    # --- ADD EXPENSE ---
    elif choice == "2":
        amount = float(input("Enter expense amount: ₦"))
        try:
            with open("balance.txt", "r") as file:
                content = file.read().strip()
                balance = float(content) if content else 0.0
        except FileNotFoundError:
            balance = 0.0

        if amount > balance:
            print(f"⚠️ Not enough balance. You only have ₦{balance}.")
        else:
            balance -= amount
            with open("balance.txt", "w") as file:
                file.write(str(balance))
            print(f"💸 Expense of ₦{amount} recorded. New balance: ₦{balance}.")
            with open("transactions.txt", "a") as file:
                file.write(f"-{amount} → balance: {balance}\n")

    # --- VIEW BALANCE ---
    elif choice == "3":
        try:
            with open("balance.txt", "r") as file:
                balance = file.read().strip()
                print(f"💰 Your current balance is ₦{balance}.")
        except FileNotFoundError:
            print("No balance record found yet!")

    # --- VIEW TRANSACTIONS ---
    elif choice == "4":
        try:
            with open("transactions.txt", "r") as file:
                transactions = file.read().strip()
                if transactions:
                    print("\n📜 Transaction History:")
                    print(transactions)
                else:
                    print("No transactions recorded yet.")
        except FileNotFoundError:
            print("No transactions file found yet!")

    # --- EXIT ---
    elif choice == "5":
        print("👋 Thank you for using Budget Tracker!")
        break

    else:
        print("❌ Invalid choice, please try again.")



