#🧮 Challenge: Build a Math Quiz Game
#The program asks the user random math questions (addition, subtraction, multiplication, maybe division).
#The player has a limited number of attempts (like lives).
#Score increases for each correct answer.
#At the end, show the total score.
#(Optional) Add difficulty scaling → e.g., Easy = small numbers, Hard = larger numbers.
#MY Attempt
def operator_check(value,value1, value2,):
    if value=="-":
        ans=value1-value2
        return ans
    elif value=="+":
        ans=value1+value2
        return ans
    elif value=="*":
        ans=value1*value2
        return ans
    else:
        ans= value1/value2
        return ans

import random
operator=["+","-","/","*"]

total=5
count=0
score=0
print("Welcome to math Quiz!")
print("\nChoose difficulty:")
print("1.Easy")
print("2.Hard")
choice=input("Enter your choice:")
if choice=="1":
   print("\nYou have 5 questions.")
   while True:
        count += 1
        num1= random.randint(1, 12)
        num2=random.randint(1,12)
        OP = random.choice(operator)
        if count > 5:
            print(f'\nYou got {score} out of the 5 questions.')
            break
        print(f'\nWhat is {num1} {OP} {num2}?')
        try:
           answer = float(input("Enter your answer:"))
        except ValueError:
            print("\n That is not a number-question skipped.")
            total-=1
            continue
        storage=operator_check(OP,num1,num2)
        #check_list
        if storage==answer:
            total -= 1
            score+=1
            print("Correct!")
            print("You have only "+str(total)+" questions left.")

        else:
            total-=1
            print("incorrect!")
            print("You have only "+str(total)+" questions left.")

if choice=="2":
    print("\nYou have 5 questions.")
    while True:
        count+=1
        num1= random.randint(1, 50)
        num2=random.randint(1,50)
        OP = random.choice(operator)
        if count > 5:
          print(f'\nYou got {score} out of the 5 questions.')
          break
        print(f'\nWhat is {num1} {OP} {num2}?')
        try:
            answer = float(input("Enter your answer:"))
        except ValueError:
                print("\n That is not a number-question skipped.")
                total -= 1
                continue
                # check_list
        storage = operator_check(OP, num1, num2)
        if storage == answer:
            total -= 1
            score += 1
            print("Correct!")
            print("You have only " + str(total) + " questions left.")

        else:
            total -= 1
            print("incorrect!")
            print("You have only " + str(total) + " questions left.")
          
#✅ Corrected Version (after AI Tutor feedback)
#you basically built a working math quiz game with two difficulty levels!
#✅ Improvements
#Division issues
#Right now num1 / num2 may give long decimals or divide by zero.
#Fix: Either round answers to 2 decimals, or only use numbers that divide evenly.
elif value == "/":
    if value2 == 0:  # avoid dividing by zero
        return None
    ans = round(value1 / value2, 2)  # round to 2 decimals
    return ans
#Consistent question counter
#You’re using both total and count, which gets confusing.
#Just use count as the question tracker.
#Replay option
#After the quiz ends, ask if the user wants to play again.
#Leaderboard (optional, advanced)
#Store player scores in a dictionary and show top players.


  
          
