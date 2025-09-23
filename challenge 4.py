#Challenge: Student Score Tracker
#You will build a program that:
#Asks the user how many students they want to enter.
#For each student, ask for their name and score (out of 100).
#Store this information in a list.
#At the end, your program should:
#Print all student names and scores.
#Show the highest score and which student got it.
#Show the average score of the class.
#Print the list of names in alphabetical order.
#⚡Extra (if you want a small stretch):
#Allow the user to search for a student’s score by entering their name.
# ❌ My Attempt
student=int(input("how many students do you want to enter:"))
count=0
store=[]
while student>count:
     name=input("Enter your name:")
     score=int(input("Enter your score:"))
     store.append([name,score])
     count+=1
print(store)
print(sorted(store))
choice=input("\nDo you want to search for a student score?:")
if choice=="yes":
  search=input("Enter name to search for students score:")
   for i, b in store:
      if i ==search:
          print(b)
else:
    print("thank you")
    exit()

# ✅ Corrected Version (after AI Tutor feedback)
# Ask user how many students they want to enter
student = int(input("How many students do you want to enter: "))
count = 0
store = []

# Collect student names and scores
while student > count:
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    store.append([name, score])
    count += 1

# Print all data
print("\nAll students and scores:", store)

# Print sorted list by names
print("Alphabetical order:", sorted(store))

# Show highest, lowest, and average
scores = [s[1] for s in store]  # extract only the score
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores)/len(scores):.2f}")

# Search feature
choice = input("\nDo you want to search for a student score? (yes/no): ").lower()
if choice == "yes":
    search = input("Enter name to search for student’s score: ")
    found = False
    for i, b in store:
        if i == search:
            print(f"{i} scored {b}")
            found = True
    if not found:
        print("Student not found.")
else:
    print("Thank you, goodbye!")
     
#New Mini-Challenge
#Update your code so that the users get a meun of what to do:
print("Check Highest score(1)")
print("Check Lowest score(2)")
print("Check Average score(3)")
options=input("What do you want to do?:")
while options not in ("1","2","3"):
    print("invalid input,enter the three valid options available")
    options=input("What do you want to do?:")

# Ask user how many stud
# ents they want to enter
student = int(input("How many students do you want to enter: "))
count = 0
store = []

# Collect student names and scores
while student > count:
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    store.append([name, score])
    count += 1

# Print all data
print("\nAll students and scores:", store)

# Print sorted list by names
print("Alphabetical order:", sorted(store))

# Show highest, lowest, and average
scores = [s[1] for s in store]  # extract only the score

if options=="1":
    print(f"Highest score: {max(scores)}")
elif options=="2":
     print(f"Lowest score: {min(scores)}")
elif options=="3":
     print(f"Average score: {sum(scores)/len(scores):.2f}")

# Search feature
choice = input("\nDo you want to search for a student score? (yes/no): ").lower()
if choice == "yes":
    search = input("Enter name to search for student’s score: ")
    found = False
    for i, b in store:
        if i == search:
            print(f"{i} scored {b}")
            found = True
    if not found:
        print("Student not found.")
else:
    print("Thank you, goodbye!")
# we printed the options available to user
#if the user picked option 1 (we print the highest score)
#if the user picked option 2(we print the lowest score)
#if the user picked option 3(we print the average score)


#📌 Challenge: Student Score Manager 2.0
#You will extend the previous student-score program with these new features:
#Menu Options
#After entering students and scores, show this menu:
#1. View All Students & Scores
#2. View Highest Score
#3. View Lowest Score
#4. View Average Score
#5. Search for a Student
#6. Add a New Student
#7. Remove a Student
#8. Exit
#The user should pick an option by entering the number.
#Features to Implement
#View All Students & Scores → print the list in alphabetical order.
#Highest/Lowest/Average → show based on scores.
#Search → ask for a name and display the score if found.
#Add a New Student → ask for name and score, then add it to the list.
#Remove a Student → ask for a name, if found, remove that student.
#Exit → quit the program.
#Extra Rules
#Handle invalid menu inputs gracefully (don’t crash, just ask again).
#Ignore uppercase/lowercase differences when searching or deleting names.
#Keep looping the menu until the user chooses Exit.
#MY Attempt:
# Student Score Management Program

# Ask how many students the user wants to enter
try:
  student = int(input("How many students do you want to enter: "))
except ValueError:
    print("invalid input.pls enter correct value")
    student = int(input("How many students do you want to enter: "))
count = 0
store = []

# Collect names and scores
while count < student:
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    store.append([name, score])   # store as [name, score]
    count += 1
while True:
#meun option
           print("\n Meun Options available")
           print("1.View ALL Students and scores")
           print("2.View Highest Score")
           print("3.View lowest Score")
           print("4.View Average score")
           print("5.Search for a student")
           print("6.Add a New student")
           print("7.Remove a student")
           print("8.Exit")
           choice=input("What would you like to do?:")
           while choice not in ["1","2","3","4","5","6","7","8"]:
               print("Option is not included,Pls.enter right option")
               choice = input("What would you like to do?:")
            #option one
           if choice=="1":
            # Print all entered students
            print("\nAll Students and Scores:")
            print(f' Student score Alphabetical{sorted(store)} ')
           elif choice=="2":
               score=[(name, int(score))for name,score in store]
               top_student = max(score, key=lambda x: x[1])
               print(f'{top_student[0]} has the Highest score of {top_student[1]}')
               #scores = []
             #  for name, score in store:
                 #  scores.append(int(score))
               #print(f'Highest score is {max(scores)}')
           elif choice=="3":
               score = [int(score) for name, score in store]
               print(f'\nLowest score is {min(score)}')
           elif choice=="4":
                score = [int(score) for name, score in store]
                print(f'\nAverage score is {sum(score) / (len(score))}')
           elif choice=="5":
               search=(input("Enter student name to search:"))
               for name, score in store:
                   flag = False
                   if name==search:
                       print(f'\nStudent name{name} {score}')
                       flag=True
                   if not flag:
                       print("\nStudent not found")
           elif choice=="6":
               name = input("Enter student name: ")
               score = int(input("Enter student score: "))
               store.append([name, score])
           elif choice=="7":
               remove=(input("Enter student name to remove:"))
               store.remove(remove)
           elif choice=="8":
                print("\nGoodbye!!!,")
                exit()
             
#Corrected Version(after AI Tutor feedback)
# Student Score Management Program

# Ask how many students the user wants to enter
try:
    student = int(input("How many students do you want to enter: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    student = int(input("How many students do you want to enter: "))

count = 0
store = []

# Collect names and scores
while count < student:
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    store.append([name, score])
    count += 1

# Menu loop
while True:
    print("\nMenu Options:")
    print("1. View ALL Students and Scores")
    print("2. View Highest Score")
    print("3. View Lowest Score")
    print("4. View Average Score")
    print("5. Search for a Student")
    print("6. Add a New Student")
    print("7. Remove a Student")
    print("8. Exit")

    choice = input("What would you like to do?: ")
    while choice not in ["1","2","3","4","5","6","7","8"]:
        print("Invalid option. Please enter a valid choice.")
        choice = input("What would you like to do?: ")

    if choice == "1":
        sorted_store = sorted(store, key=lambda x: x[0].lower())
        print("\nAll Students and Scores (Alphabetical):")
        for name, score in sorted_store:
            print(f"{name} → {score}")

    elif choice == "2":
        top_student = max(store, key=lambda x: x[1])
        print(f"\n{top_student[0]} has the highest score: {top_student[1]}")

    elif choice == "3":
        low_student = min(store, key=lambda x: x[1])
        print(f"\n{low_student[0]} has the lowest score: {low_student[1]}")

    elif choice == "4":
        scores = [score for _, score in store]
        avg = sum(scores) / len(scores)
        print(f"\nAverage score is: {avg:.2f}")

    elif choice == "5":
        search = input("Enter student name to search: ")
        flag = False
        for name, score in store:
            if name.lower() == search.lower():
                print(f"{name} scored {score}")
                flag = True
                break
        if not flag:
            print("Student not found.")

    elif choice == "6":
        name = input("Enter new student name: ")
        score = int(input("Enter new student score: "))
        store.append([name, score])
        print(f"{name} added successfully!")

    elif choice == "7":
        remove = input("Enter student name to remove: ")
        found = False
        for s in store:
            if s[0].lower() == remove.lower():
                store.remove(s)
                print(f"{remove} has been removed.")
                found = True
                break
        if not found:
            print("Student not found in list.")

    elif choice == "8":
        print("\nGoodbye!")
        break






