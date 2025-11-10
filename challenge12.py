#Chatbot Simulation
#Asks the user to type something (e.g., “Hi”, “Hello”, etc.)
#Converts the input to lowercase.
#If the message is:
#“hi” or “hello” → print “Hello there! 😊”
#“how are you” → print “I’m just a bot, but I’m doing great!”
#anything else → print “I don’t understand that yet.”
#MY Attempt
user_input=input("Type something(E.g,Hi,Hello):").lower()
if  user_input=="hi" and "hello":
    print("Hello there!")
elif user_input=="how are you":
    print("I'm just a bot,I'm doing well")
else:
    print("I don't understand that yet ")
#AI correction
#The condition
#user_input == "hi" and "hello"
#does not mean “if user_input is hi OR hello”.
#Since "hello" is a non-empty string, Python treats it as True.
#So your if will always run — even if the user types something else!
#✅ The fix:
if user_input == "hi" or user_input == "hello":
    print("Hello there!")
#or 
if user_input in ["hi", "hello"]:
    print("Hello there!")
#Stage 2: Smarter Chatbot
#🎯 Your Challenge:
#Write a chatbot that:
#Greets the user if they type hi or hello.
#Replies to “how are you”.
#Replies to “what is your name”.
#Replies to any message containing the word “weather”.
#Replies with “I don’t understand that yet” for anything else.
#My attempts 
import random
reply_options=["Hello there!","Wassup","Hello buddy","HEY friend!"]
reply_options2=["I'm doing great hope you are doing great to?","I am doing fine,are you doing good to?","just enjoying the day, are you enjoying the day?"]
save=random.choice(reply_options)
save2=random.choice(reply_options2)
user_input=input("Type something(E.g,Hi,Hello):").lower()
if  user_input in ["hi", "hello"]:
    print(save)
elif user_input=="how are you":
    print(save2)
elif user_input=="what is your name":
     print("i'm Chatbot 2.0, your python buddy.")
elif user_input=="what is the weather like?":
    print("i'm not sure, but i hope it's sunny where you are!")
else:
    print("i don't understand that yet.")
#AI correction
#🩵 1. The weather check should use in instead of ==
#Right now, your code only replies if the user types exactly “what is the weather like?”.
#But what if they say “what’s the weather today?” or “tell me the weather”?
#Your bot wouldn’t respond.
#✅ Fix:
elif "weather" in user_input:
    print("I'm not sure, but I hope it's sunny where you are!"
#🩷 2. Improve formatting and tone consistency
#Tiny polish to make output feel smoother:
#Start your bot’s name with a capital letter (“I’m ChatBot 2.0…”).
#Add a space after commas for readability.
#✅ Fix:
elif user_input == "what is your name":
    print("I'm ChatBot 2.0, your Python buddy.")          
# (Optional improvement)
#You could also make the bot respond to messages that contain those phrases (not just match exactly)
#🧠 Stage 3 Challenge Description
#Make your chatbot:
#Ask the user for their name (if it doesn’t already know it).
#Store it in a variable.
#Use that name in its responses (e.g., “Hi Olamide! Nice to meet you!”).
#Still respond to things like “hi”, “how are you”, etc., just like before — but now, include the user’s name when replying.
#My attempts 
import random
reply_options=["Hello there!","Wassup","Hello buddy","HEY friend!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying the day1"]

save=random.choice(reply_options)
save2=random.choice(reply_options2)
#user name
name_log=input("Hi buddy what your name:").strip().capitalize()
print(f'Hi {name_log}!Nice to meet you, i have saved your name to '
      f'to my memory and i will never forget ')
user_input=input("Type something "+name_log+" (E.g,Hi,Hello):").lower()

if  'hi'in user_input or 'hello'in user_input :
    print(save,name_log)
elif "how are you" in user_input:
    print(save2,name_log)
elif  "what is your name"in user_input :
     print("I'm Chatbot 2.0, your python buddy "+name_log+".")

elif user_input in "what is the weather like?":
    print("i'm not sure, but i hope it's sunny where you are!")
else:
    print("i don't understand that yet.")
    
#AI correction 
while True:
    user_input = input(f"What would you like to say, {name_log}? ").lower()

    if 'hi' in user_input or 'hello' in user_input:
        print(save, name_log)
    elif "how are you" in user_input:
        print(save2, name_log)
    elif "bye" in user_input:
        print(f"Goodbye {name_log}, talk soon!")
        break
    else:
        print("I don't understand that yet.")
#That way, the chatbot keeps chatting until the user says “bye.”
#This turns it into a real conversation loop 🗣️      

#🧠 Challenge: “Memory Chatbot (Smart Reply)”
#We’ll make your chatbot remember the user’s name for next time and respond differently when they return.
#🧩 Requirements
#When the program starts:
#It should check if a file called user_data.txt exists.
#If it does, read the stored name and greet the user by name.
#If it doesn’t, ask for their name, save it to the file, and greet them.
#After greeting:
#Ask the user how they’re doing.
#If they say something like “good” or “fine”, reply positively.
#If they say “bad” or “not good”, reply with something encouraging.
#End the chat politely.
#My Attempt
import random
reply_options=["Hello there!","Wassup","Hello buddy","HEY friend!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]

# user name
try:
    with open("name.txt", "r") as f:
        line = f.read()
        if not line.strip():
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you, i have saved your name to '
                  f'to my memory and i will never forget ')
            # saving name_log
            with open("name.txt", "a") as file:
                file.write(name_log)
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have you name to memory')
                with open("name.txt", "w") as file:
                    file.write(name_log)
            else:
                with open("name.txt", "r") as file:
                    line = file.read()
                print(f'OK {line}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    with open("name.txt","w") as file:
        file.write(name_log)

def color_check():
    try:
        with open("color.txt","r") as new_file:
         lines=new_file.readline()
         if not lines .strip():
            fav_color = input("What is your favourite color?:").strip().capitalize()
            with open("color.txt","w") as file_update:
               file_update.write(fav_color)
            return fav_color
         else:
             change_color=input("Do you want to change your fav color?:test").strip().lower()
             while  change_color not in['no','yes']:
                 change_color = input("Do you want to change your fav color?:").strip().lower()
             if change_color=="yes":
                 color_update=input("Enter your new color:").strip().capitalize()
                 with open("color.txt","w")as file_change:
                     file_change.write(color_update)
                 return color_update
             else:
                 return lines.strip()


    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("color.txt", "w") as file_update:
            file_update.write(fav_color)
        return fav_color

color_check()
color=color_check()

while True:
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)

#chat loop
    with open("name.txt", "r") as file:
        name_log = file.read()
    user_input=input("Type something "+name_log+" (E.g,Hi,Hello):").lower()
    if  'hi'in user_input or 'hello'in user_input :
      print(save,name_log)
    elif "how are you" in user_input:
      print(save2,name_log)
    elif  "what is your name"in user_input :
      print("I'm Chatbot 2.0, your python buddy "+name_log+".")
    elif "what is my favourite color" in user_input:
        print(f'Your favourite color is {color}')
    elif "bye" in user_input:
        print(f'Goodbye,{name_log},talk soon!')
        break
    elif any(word in user_input for word in ["yes","fine"]):
        print("I'm glade to hear that!")
    elif  "what is the weather like?" in user_input:
      print("i'm not sure, but i hope it's sunny where you are!")
    else:
      print("i don't understand that yet.")
#AI Correction
#1. Fix a small typo and logic in your color section
#You accidentally left "test" inside this line:
change_color = input("Do you want to change your fav color?:test").strip().lower()
#✅ Replace it with:
change_color = input("Do you want to change your fav color?: ").strip().lower()
#2. Avoid calling color_check() twice
#Right now you have:
color_check()
color = color_check()
#That means it runs the function two times — so it might ask the question twice or behave oddly.
#✅ Replace those two lines with just:
color = color_check()
#3. Small grammar and polish updates
#You can slightly adjust your prints for smoother English:
print(f"Hi {name_log}! Nice to meet you. I’ve saved your name to my memory and won’t forget it.")
#and
print(f"{name_log}, I’ve updated your name in my memory.")






