#🎯 Challenge: Word Guess Game (like Hangman but simpler)
#Goal
#Create a program where the computer picks a random word, and the player must guess it letter by letter.
#Requirements
#Word Bank:
#Have a list of words (at least 5).
#The program randomly chooses one.
#Display progress:
#Show the word as underscores _ _ _ at the start.
#As the user guesses letters correctly, fill them in.
#Attempts:
#Easy mode → 10 attempts.
#Hard mode → 5 attempts.
#Each wrong guess reduces attempts.
#Win/Loss conditions:
#If the player fills all letters, they win 🎉.
#If attempts run out, they lose 😢.
#Replay option:
#After the game ends, ask if they want to play again.
#(Optional Upgrade):
#Keep a simple scoreboard: how many games won vs lost.
#My Attempts
word_storage = ["book", "dog", "soup", "pencil", "adventure"]
attempt=0
won=0
loss=0
import random
value = random.choice(word_storage)
def data_value(data_1, data_2,data_3,data_4):
     if data_1 in data_3:
         for index, letter in enumerate(data_3):
             if letter==data_1:
                 data_4[index]=letter
         print(f'Correct {" ".join(data_4)}')
         return data_2,data_4
     else:
         data_2-=1
         print("Wrong guess! You have only "+str(data_2)+" tries left")
         print(" ".join(data_4))
         return data_2, data_4

while True:
    print("Mode Available")
    print("1.Easy")
    print("2.Hard")
    count = 10
    count_two = 5
    choice = input("Enter a mode:")
    while choice not in ("1", "2"):
        print("invalid choice")
        choice = input("\nEnter your choice:")
    if choice == "1":
        hidden = ["_"] * len(value)
        print(f"The word has {len(value)} letters: {' '.join(hidden)}")
        attempt+=1
        while True:
            if count <= 0:
                print("\nYou have used all your guesses")
                #number of time lost
                loss+=1
                break
            else:
                if "_" not in hidden:
                    print("\n You guessed the word " + value)
                    #number of time won
                    won+=1
                    break
            user_input = input("\nGuess a letter in the word: ").lower()
            count, hidden = data_value(user_input, count, value, hidden)
            #replaying option
        question = input("\nWould you like to play again?:").lower()
        if question == "yes":
            #scoreboard
            print(f'\nYou have played {attempt} times in a roll winning {won} times and loosen {loss} times')
            continue
        else:
            break

    elif choice == "2":
        hidden = ["_"] * len(value)
        print(f"The word has {len(value)} letters: {' '.join(hidden)}")
        attempt+=1
        while True:
            if count_two <= 0:
                print("\nYou have used all your guesses")
                loss+=1
                break
            else:
                if "_" not in hidden:
                    print("\n You guessed the word " + value)
                    won+=1
                    break
            user_input = input("\nGuess a letter in the word: ").lower()
            count_two, hidden = data_value(user_input, count_two, value, hidden)
            #replaying option
        question = input("\nWould you like to play again?:").lower()
        if question == "yes":
            #scoreboard
            print(f'\nYou have played {attempt} times in a roll, winning {won} times and loosen {loss}times')
            continue
        else:
            break


#Ai Tutor Correction 
import random

word_storage = ["book", "dog", "soup", "pencil", "adventure"]
attempt = 0
won = 0
loss = 0

def data_value(guess, attempts, word, hidden):
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                hidden[index] = letter
        print(f'Correct! {" ".join(hidden)}')
    else:
        attempts -= 1
        print(f"Wrong guess! You have only {attempts} tries left")
        print(" ".join(hidden))
    return attempts, hidden

while True:
    print("\nMode Available")
    print("1. Easy (10 attempts)")
    print("2. Hard (5 attempts)")
    
    choice = input("Enter a mode: ").strip()
    while choice not in ("1", "2"):
        print("Invalid choice")
        choice = input("\nEnter your choice: ").strip()
    
    # reset word and attempts for each new game
    value = random.choice(word_storage)
    hidden = ["_"] * len(value)
    print(f"\nThe word has {len(value)} letters: {' '.join(hidden)}")
    
    attempt += 1
    attempts_left = 10 if choice == "1" else 5
    
    # game loop
    while attempts_left > 0:
        if "_" not in hidden:
            print(f"\n🎉 You guessed the word '{value}'!")
            won += 1
            break
        
        guess = input("\nGuess a letter in the word: ").lower()
        attempts_left, hidden = data_value(guess, attempts_left, value, hidden)
    
    else:  # only runs if while loop ends without 'break'
        print(f"\n😢 You ran out of guesses. The word was '{value}'.")
        loss += 1
    
    # replay option
    question = input("\nWould you like to play again? (yes/no): ").lower()
    print(f'\n📊 You have played {attempt} times in a row, winning {won} times and losing {loss} times.')
    
    if question != "yes":
        print("\nThanks for playing! 👋")
        break

