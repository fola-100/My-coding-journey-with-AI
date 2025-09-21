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





