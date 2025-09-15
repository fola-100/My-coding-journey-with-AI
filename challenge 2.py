#Challenge:Name Storage & Search Program
#Task from AI Tutor (ChatGpt)
#write a program that will:
#Ask the user how many names they want to store.
# Use a loop to collect those names one by one.
#Save all the names in a list.
#After all names are entered, print:
#The full list of names.
#Each name on a new line.
#Bonus (if you want extra practice):
#Print each name on a new line using a loop.
#Ask the user if they want to search for a name
# and check if it exists in the list.

# ❌My attempt
count=0
number=int(input("Enter how many name you want to store:"))
loop = []
while number>=count:
    count += 1
    names = input("Enter names:")
    loop.append(names)
print(loop)

search=input("Do you want to search for a name?:").lower()
if search not in ["yes","no"]:
    print("invalid input")
    exit()
if search=="yes":
    name=input("Enter the name you want to search:")
    if name in loop:
        print("Name exist.")
    else:
        print("Name not found.")
else:
    print("You have exited successfully")
    exit()

  # ✅ Corrected Version (after AI Tutor feedback)
count = 0
number = int(input("Enter how many names you want to store: "))
loop = []

while count < number:   # only loop as many times as the user asked
    names = input("Enter name: ")
    loop.append(names)
    count += 1

# print full list
print("\nFull list of names:", loop)

# print each name on a new line
print("\nNames one by one:")
for n in loop:
    print(n)

# bonus: first and last name
print(f"\nFirst name: {loop[0]}")
print(f"Last name: {loop[-1]}")

# search feature (extra you added, nice!)
search = input("\nDo you want to search for a name? (yes/no): ").lower()
if search == "yes":
    name = input("Enter the name you want to search: ")
    if name in loop:
        print("Name exists.")
    else:
        print("Name not found.")
else:
    print("You have exited successfully")
#New Mini-Challenge
#Update your code so that after the user enters all the names, you also:
#Sort the names alphabetically and print them.
#Sort the names in reverse order (Z → A) and print them.
#Tell the user how many names were stored in total.
# ❌My attempt
#Reverse order
print(loop[::-1]) 
#Total number of names
print(len(loop))
 # ✅ Corrected Version (after AI Tutor feedback)
print("\nAlphabetical order:", sorted(loop))
print("Reverse order:", sorted(loop, reverse=True))


    






