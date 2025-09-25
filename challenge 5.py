#🚀 New Challenge Idea:
#Number Guessing Game (with Levels)
#👉 Requirements:
#The computer picks a random number between 1–100.
#Ask the user to guess the number.
#Tell them if their guess is too high or too low until they get it.
#Keep track of the number of attempts.
#Add difficulty levels:
#Easy → 10 attempts
#Hard → 5 attempts
#❌ My Attempt
import random
number=random.randint(1,100)
#import module:used help to get this though
count=10
count_two=5
print("Mode Available")
print("1.Easy")
print("2.Hard")
choice=input("Choose a mode:").lower().strip()
while choice not in ("1","2"):
    print("Invalid option enter available mode")
    choice = input("Choose a mode:").lower().strip()
if choice == "1":
  while True:
       user = int(input("Enter a number between 1-100:"))
       count-=1
       if count<=0:
           print("You have used all your attempts")
           break
       if number > user:
          print("Number entered is too low, you have only "+str(count)+" attempts left.")
       elif number < user:
            print("Number entered is high, you have only "+str(count)+" attempts left.")
       elif number == user:
           print("You got it right!!!")
           exit()
while choice=="2":
    user = int(input("Enter a number between 1-100:"))
    count_two-=1
    if count_two<=0:
        print("You have used all your attempts.")
        break
    if number>user:
        print(f'Number entered is too low, you have only {count_two} attempts left.')
    elif number<user:
        print(f'Number entered is high,you have only {count_two} attempts left.')
    else:
        print("You got it right!!!")
        exit()
 # ✅ Corrected Version (after AI Tutor feedback)
#Nicely done! You’ve built a fully working Number Guessing Game with both difficulty levels
#Small improvements
#Instead of while choice=="2":, use if choice=="2":.
#Reason: while will keep looping forever, but since you’re already controlling guesses with count_two, an if works better.
#You could put the guessing loop inside one function to avoid repeating code for Easy and Hard.

#Udate:
#Create one function (maybe call it play_game) that takes two inputs:
#number → the random number,
#attempts → how many tries (Easy = 10, Hard = 5).
#Inside the function, run the guessing loop.
#Then in your main program, just call play_game(number, 10) or play_game(number, 5) depending on the user’s choice.
#That way, no repeated code
#❌ My Attempt
import random
number=random.randint(1,100)
#import module:used help to get this though
def play_game(value,attempts):
        attempts -= 1
        if attempts <= 0:
          print("You have used all your attempts")
        if number > value:
          print("Number entered is too low, you have only " + str(count) + " attempts left.")
          return attempts
        elif number < value:
            print("Number entered is high, you have only " + str(count) + " attempts left.")
            return attempts
        elif number == value:
            print("You got it right!!!")
            exit()
count=10
count_two=5
print("Mode Available")
print("1.Easy")
print("2.Hard")
choice=input("Choose a mode:").lower().strip()
while choice not in ("1","2"):
    print("Invalid option enter available mode")
    choice = input("Choose a mode:").lower().strip()

if choice == "1":
   while True:
        user = int(input("Enter a number between 1-100:"))
        save=count(play_game(user,count))
elif choice=="2":
    user = int(input("Enter a number between 1-100:"))
    save=play_game(user,count_two)
# ✅ Corrected Version (after AI Tutor feedback)
import random

number = random.randint(1, 100)

def play_game(value, attempts):
    attempts -= 1
    if number > value:
        print(f"Number entered is too low, you have only {attempts} attempts left.")
    elif number < value:
        print(f"Number entered is too high, you have only {attempts} attempts left.")
    else:
        print("You got it right!!!")
        return 0   # signal game won
    return attempts   # return how many tries are left

print("Mode Available")
print("1. Easy (10 attempts)")
print("2. Hard (5 attempts)")

choice = input("Choose a mode: ").lower().strip()
while choice not in ("1", "2"):
    print("Invalid option. Enter 1 or 2.")
    choice = input("Choose a mode: ").lower().strip()

# set attempts based on choice
attempts = 10 if choice == "1" else 5

# main loop
while attempts > 0:
    user = int(input("Enter a number between 1-100: "))
    attempts = play_game(user, attempts)
    if attempts == 0:   # either guessed correct or ran out
        break

if attempts != 0:
    print(f"Out of attempts! The number was {number}.")







