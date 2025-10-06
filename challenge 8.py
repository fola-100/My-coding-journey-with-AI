#warm-up challenge:
#Daily Journal App (Beginner File Project)
#Goal
#Create a simple journal program where you can:
#Add a new entry (append it to a text file).
#Read all previous entries (display everything in the file).
#Write a program that:
#Opens (or creates) a file called "journal.txt".
#If user picks 1, asks for input and appends it to the file.
#If user picks 2, reads and prints all entries.
#If user picks 3, exits.
#Keeps running until user chooses exit
print("Welcome to your Daily Journal")
while True:
     print("\n")
     print("1.) Add new entry")
     print("2.) View all entries")
     print("3.)Exit")
     #input checker
     choice = input("Enter your choice:")
     if choice=="1":
        with open("journal.txt","a")as file:
            file.write(input("Write your journal entry:"))
            print("journal entry has been saved. successfully.")
     elif choice=="2":
          with open("journal.txt","r") as file:
              file=file.read()
              print(file)
     elif choice=="3":
          print("Goodbye")
          break
     else:
         print("invalid choice,pls enter the option accessible.")
#AI Correction 
#🔥 That’s a great warm-up, and your code is clean, working, and well-organized.
#You’ve nailed

  
