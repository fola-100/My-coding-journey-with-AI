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

#update Challenge
#🧠 New Features to Add
#Multiple Pages (Topics)
#Each “page” is a separate text file, e.g.
#ideas.txt
#goals.txt
#dreams.txt
#notes.txt
#Switch Pages
#User can “flip” to another file (topic) to write or read entries there.
#View Current Page
#Display which topic (file) they’re currently writing in.
#My attempt
print("Welcome to your Daily Journal")
while True:
     print("\n")
     print("1.) Create a new entry or erase details in existing entry")
     print("2.) View all entries")
     print("3.) Update jornal entry")
     print("4.)Exit")
     #input checker
     choice = input("Enter your choice:").strip()
     if choice=="1":
         name = input("What name do you want to save the page has:")
         with open(name + ".txt", "w") as file:
             decision=input("Do you want to write in the jornal now?:").lower().strip()
             if decision=="yes":
               file.write(input("What do you want to write in your jornal entry: "))
             else:
                 print("Name saved. successfully.")
                 continue
     #reading file
     elif choice == "2":
         name=input("Enter the page in the journal you are looking for:").strip().lower()
         try:
            with open(name+".txt","r") as file:
                file = file.read()
                print(file)
         except FileNotFoundError:
             print("NO such page like "+name)

     #appending file
     elif choice=="3":
         name=input("Enter the page in the journal you are looking for:").strip().lower()
         with open(name+"txt.", "a") as file:
             file.write(input("Write your journal entry:"))
             print("\njournal entry has been updated. successfully.")

     #Exist 
     elif choice=="4":
          print("Goodbye")
          break
     else:
         print("invalid choice,pls enter the option accessible.")
 #AI CORRECTION 
#1️⃣ Tiny Typo in File Extension (line under elif choice == "3":)
#You wrote:
#with open(name+"txt.", "a") as file:
#That’s missing the dot before “txt”.
#✅ Correct version:
#with open(name + ".txt", "a") as file:
#🧩 2️⃣ Lower/Upper Case Mismatch
#You’re converting names to lowercase when reading:
#name = input("Enter the page in the journal you are looking for:").strip().lower()
#…but not when creating the file:
#name = input("What name do you want to save the page has:")
#That means if you create a file like “Dreams.txt”, but later search for “dreams”,
#Python won’t find it on systems that are case-sensitive (like Linux or macOS).
#✅ Easiest fix — keep it consistent:
#name = input("What name do you want to save the page has:").strip().lower()
#🧠 Optional Improvement (Just for clarity)
#You might want to print a short message after creating or appending to confirm the file name:
#print(f"'{name}.txt' has been saved successfully.")



  
