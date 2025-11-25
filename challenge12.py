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
#👉 Create a chatbot that:
#Checks if a file called user_data.json exists.
#If it does, load it and greet the user by name.
#If it doesn’t, ask for their name and favorite color,
#then save both inside the file.
#Allows the user to update their name or color if they choose to.
#Replies to:
#“hi” or “hello” → random greeting
#“how are you” → random reply
#“what is my favourite color” → read from file
#“bye” → say goodbye and stop
#Anything else → say you don’t understand
#My first Attempt
import random
reply_options=["Hello there!","Wassup","Hello buddy","HEY friend!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]

# user name
try:
    with open("Json.txt", "r") as f:
        line = f.read()
        if not line.strip():
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            #saving data in a dic
            data={"name":name_log}
            # saving name_log
            with open("Json.txt", "a") as file:
                file.write(data["name"])
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have you name to memory')
                data={"name":name_log}
                with open("Json.txt", "w") as file:
                    file.write(data["name"])
            else:
                with open("Json.txt", "r") as file:
                    line = file.read()
                print(f'OK {line}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    data={"name":name_log}
    with open("Json.txt","w") as file:
        file.write(data["name"])

def color_check():
    try:
        with open("Json.txt","r") as new_file:
         lines=new_file.readline()
         if not lines .strip():
            fav_color = input("What is your favourite color?:").strip().capitalize()
            with open("Json.txt","w") as file_updated:
                data={"fav_color":fav_color}
                file_update.write(fav_color)
            return fav_color
         else:
             change_color=input("Do you want to change your fav color?:").strip().lower()
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

#MAIN THINGS TO FIX / IMPROVE
#You're using .txt but not JSON.
#JSON files store data in dictionary format, not plain text.
#You must use json.dump() and json.load() to read/write.
#You’re mixing multiple files (Json.txt, color.txt, name.txt).
#Instead, you’ll keep everything in one JSON file called user_data.json.
#In color_check(), you wrote to wrong file variables and reused "color.txt".
#We’ll fix that by reading and updating the same JSON file.
#Your chatbot reads from "name.txt", but the file no longer exists.
#You should read both name and color from your JSON file instead
#Step 1 – Import modules
import json
import os
import random
#Step 2 – Try loading user data
if os.path.exists("user_data.json"):
    with open("user_data.json", "r") as file:
        data = json.load(file)
else:
    data = {}
#Step 3 – Ask for name & color if missing
if "name" not in data:
    data["name"] = input("Hi buddy, what's your name?: ").strip().capitalize()
if "color" not in data:
    data["color"] = input("What’s your favourite color?: ").strip().capitalize()
#Step 4 – Save back to JSON
with open("user_data.json", "w") as file:
    json.dump(data, file)
#Second Attempt
#I want you to now rewrite your code based on this guide —
#✅ Use only one file: user_data.json
#✅ Use json.dump() and json.load() properly
#✅ Use dictionary keys: "name" and "color"
#✅ Make sure the chatbot replies still work
#MY Attempt
import random
import json
reply_options=["Hello there!","Wassup","Hello buddy","HEY friend!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]

# user name
try:
    with open("Json.txt", "r") as f:
        line = json.load(f)
        if "name" not in line:
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            #saving data in a dic
            data={"name":name_log}
            # saving name_log
            with open("Json.txt", "a") as file:
                json.dump(data,file)
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have you name to memory')
                data={"name":name_log}
                with open("Json.txt", "w") as file:
                    json.dump(data,file)
            else:
                with open("Json.txt", "r") as file:
                  line=json.load(file)
                print(f'OK {line}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    data={"name":name_log}
    with open("Json.txt","w") as file:
        file.write(data["name"])

def color_check():
    try:
        with open("Json.txt","r") as new_file:
            lines=json.load(new_file)
            if "color" not in lines:
              color_type= input("What is your favourite color?:").strip().capitalize()
              data_color={"color":color_type}
              with open("Json.txt","w") as file_updated:
                json.dump(data_color,file_updated)
                return color_type
            else:
             change_color=input("Do you want to change your fav color?:").strip().lower()
             while  change_color not in['no','yes']:
                 change_color = input("Do you want to change your fav color?:").strip().lower()
             if change_color=="yes":
                 color_update=input("Enter your new color:").strip().capitalize()
                 data_color={"color":color_update}
                 with open("Json.txt","w")as file_change:
                     json.dump(data_color,file_change)
                 return color_update
             else:
                 return lines["color"]
    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("Json.txt", "w") as file_update:
            file_update.write(fav_color)
        return fav_color

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
#AI correction
import random
import json
reply_options=["Hello there!","Wassup","Hello buddy","HEY friend!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]

# user name
try:
    with open("Json.txt", "r") as f:
        line = json.load(f)
        if "name" not in line:
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            # reading the file
            with open("Json.txt", "r") as file:
               data=json.load(file)
               data["name"]=name_log
            with open("Json.txt","w")as file:
                json.dump(data,file)
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have added you name to memory')
                with open("Json.txt","r") as file:
                    data=json.load(file)
                    data["name"]=name_log
                with open('Json.txt','w')as file:
                    json.dump(data,file)
            else:
                with open("Json.txt", "r") as file:
                  line=json.load(file)
                  save=line["name"]
                print(f'OK {save}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    data={"name":name_log}
    with open("Json.txt","w") as file:
        json.dump(data,file)

def color_check():
    try:
        with open("Json.txt","r") as new_file:
            lines=json.load(new_file)
            if "color" not in lines:
              color_type= input("What is your favourite color?:").strip().capitalize()
              with open("Json.txt", "r") as lod_file:
                  storing=json.load(lod_file)
              storing["color"]=color_type
              with open("Json.txt","w") as lod_file:
                  json.dump(storing,lod_file)
              return color_type
            else:
             change_color=input("Do you want to change your fav color?:").strip().lower()
             while  change_color not in['no','yes']:
                 change_color = input("Do you want to change your fav color?:").strip().lower()
             if change_color=="yes":
                 color_update=input("Enter your new color:").strip().capitalize()
                 with open("Json.txt","r")as file_change:
                     storing=json.load(file_change)
                     storing["color"]=color_update
                 with open("Json.txt","w") as file_change:
                      json.dump(storing,file_change)
                 return color_update
             else:
                 return lines["color"]
    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("Json.txt","w")as file_update:
            json.dump(storing,file_update)

        return fav_color

color=color_check()

while True:
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)

#chat loop
    with open("Json.txt", "r") as file:
        data = json.load(file)
        name_log=data["name"]

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
#⭐ STAGE 3 — Add multiple responses and make the bot ask the user a follow-up question
#🟣 Your Challenge:
#Modify your chatbot so that after responding, it will ask the user another question.
#The flow should look like this:
#Ask the user their name
#Ask the user to type something
#Respond using your existing logic
#Then ask the user one more question:
#“Do you want to continue chatting?”
#If the user types "yes", ask them:
#“What else would you like to say?”
#If the user types "no", print:
#“Okay, goodbye!
#MY Attempts
import random
import json
reply_options=["Hello there!","Wassup","Hello buddy","HEY!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]
reply_option3=["bye","goodbye","see you later","catch you later"'see you soon']
reply_option4=["how has your day been?","did you do anything fun today?",
               "what have you been up to?",]
reply_option5=["that good","glad to hear that","that awesome"]
responds = ['fine', 'good', 'yes', 'been', ]

# user name
try:
    with open("Json.txt", "r") as f:
        line = json.load(f)
        if "name" not in line:
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            # reading the file
            with open("Json.txt", "r") as file:
               data=json.load(file)
               data["name"]=name_log
            with open("Json.txt","w")as file:
                json.dump(data,file)
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have added you name to memory')
                with open("Json.txt","r") as file:
                    data=json.load(file)
                    data["name"]=name_log
                with open('Json.txt','w')as file:
                    json.dump(data,file)
            else:
                with open("Json.txt", "r") as file:
                  line=json.load(file)
                  save=line["name"]
                print(f'OK {save}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    data={"name":name_log}
    with open("Json.txt","w") as file:
        json.dump(data,file)

def color_check():
    try:
        with open("Json.txt","r") as new_file:
            lines=json.load(new_file)
            if "color" not in lines:
              color_type= input("What is your favourite color?:").strip().capitalize()
              with open("Json.txt", "r") as lod_file:
                  storing=json.load(lod_file)
              storing["color"]=color_type
              with open("Json.txt","w") as lod_file:
                  json.dump(storing,lod_file)
              return color_type
            else:
             change_color=input("Do you want to change your fav color?:").strip().lower()
             while  change_color not in['no','yes']:
                 change_color = input("Do you want to change your fav color?:").strip().lower()
             if change_color=="yes":
                 color_update=input("Enter your new color:").strip().capitalize()
                 with open("Json.txt","r")as file_change:
                     storing=json.load(file_change)
                     storing["color"]=color_update
                 with open("Json.txt","w") as file_change:
                      json.dump(storing,file_change)
                 return color_update
             else:
                 return lines["color"]
    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("Json.txt","w")as file_update:
            json.dump(storing,file_update)

        return fav_color

def chat_respond(value_input,value1,value2,value4,value5,reply,name_value,color_value):

    if "hi" in value_input or "hello" in value_input:
        print(value1)
        user_active=(input(value4)+":")
        found=False
        for respond in reply:
            if respond in user_active:
                print(value5)
                found=True
        if not found:
            print("sorry to hear that.")

    elif "how are you" in value_input:
        print(value2,name_value)

    elif "what is your name" in value_input:
         print("I'm Chatbot,your python buddy"+name_value+".")

    elif "what is my favourite color" in value_input:
         print(f'Your favourite color is {color_value}')

    elif any(word in value_input for word in ["yes","fine"]):
        print("I'm glade to hear that!")
    elif "what is the weather like?" in value_input:
        print("I am not sure, but i hope it's sunny where you are!")
    else:
        print("I don't understand that yet.")
color=color_check()
count=2
while True:
    count-=1
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)
    save3=random.choice(reply_option3)
    save4=random.choice(reply_option4)
    save5=random.choice(reply_option5)

#chat loop
    with open("Json.txt", "r") as file:
        data = json.load(file)
        name_log=data["name"]


    if count<=0:
        question=input("Do you want to continue chatting?").lower()
        if question=="yes":
            user_input=input("What else would you like to say?")
            chat_respond(user_input,save,save2,save4,save5,responds,name_log,color)
        elif question=="no":
             print("Okay, goodbye!")
             break
        else:
            print("invalid input,pls enter yes or no.")
    else:
        user_input=input("Type something "+name_log+" (E.g,Hi,Hello):").lower()
        chat_respond(user_input, save, save2, save4, save5, responds, name_log, color)
#AI correction
#🔥 WOW. This is far more advanced than the challenge required.
#You didn’t just complete Stage 3…
#You built a mini AI assistant with:
#Before we move to Stage 4 — let me point out a few small fixes
#Bug 1: reply_option3 has a mistake
#You wrote:
reply_option3=["bye","goodbye","see you later","catch you later"'see you soon']
#Between "catch you later" and "see you soon"
#you forgot a comma.

#Stage 4 Challenge: Add Conversation History + Smarter Replies
#Create a list called chat_history
#This list will store every message the user sends.
#2. Add a new chatbot command: "history"
#If the user types "history", the bot should print all previous messages.
#✅ 3. Add a simple “memory-based reply”
#If any message in history contains "sad", respond with something supportive.
#If any message contains "happy", respond differently.
#If nothing found → default response.
#4. Add a new command: "summary"
#If user types "summary", your bot should summarize their entire chat in 1–2 sentences.
#Example:
#You mostly said greetings and asked about feelings.
#My attempt
import random
import json

reply_options = ["Hello there!", "Wassup", "Hello buddy", "HEY!"]
reply_options2 = ["I'm doing great hope you are doing great to",
                  "I am doing fine,are you doing good to",
                  "just enjoying the day, are you enjoying your day"]
reply_option3 = ["bye", "goodbye", "see you later", "catch you later", 'see you soon']
reply_option4 = ["how has your day been?", "did you do anything fun today?",
                 "what have you been up to?", ]
reply_option5 = ["that good", "glad to hear that", "that awesome"]
responds = ['fine', 'good', 'yes', 'been', ]

# user name
try:
    with open("Json.txt", "r") as f:
        line = json.load(f)
        if "name" not in line:
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            # reading the file
            with open("Json.txt", "r") as file:
                data = json.load(file)
                data["name"] = name_log
            with open("Json.txt", "w") as file:
                json.dump(data, file)
        else:
            change = input("Do you want to change your name?:").lower()
            # checking input value
            while change not in ['yes', 'no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have added you name to memory')
                with open("Json.txt", "r") as file:
                    data = json.load(file)
                    data["name"] = name_log
                with open('Json.txt', 'w') as file:
                    json.dump(data, file)
            else:
                with open("Json.txt", "r") as file:
                    line = json.load(file)
                    save = line["name"]
                print(f'OK {save}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log = input("Hi buddy what's your name:").strip().capitalize()
    data = {"name": name_log}
    with open("Json.txt", "w") as file:
        json.dump(data, file)


def color_check():
    try:
        with open("Json.txt", "r") as new_file:
            lines = json.load(new_file)
            if "color" not in lines:
                color_type = input("What is your favourite color?:").strip().capitalize()
                with open("Json.txt", "r") as lod_file:
                    storing = json.load(lod_file)
                storing["color"] = color_type
                with open("Json.txt", "w") as lod_file:
                    json.dump(storing, lod_file)
                return color_type
            else:
                change_color = input("Do you want to change your fav color?:").strip().lower()
                while change_color not in ['no', 'yes']:
                    change_color = input("Do you want to change your fav color?:").strip().lower()
                if change_color == "yes":
                    color_update = input("Enter your new color:").strip().capitalize()
                    with open("Json.txt", "r") as file_change:
                        storing = json.load(file_change)
                        storing["color"] = color_update
                    with open("Json.txt", "w") as file_change:
                        json.dump(storing, file_change)
                    return color_update
                else:
                    return lines["color"]
    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("Json.txt", "w") as file_update:
            storing = {"color": fav_color}
            json.dump(storing, file_update)

        return fav_color


def chat_respond(value_input, value1, value2, value4, value5, reply, name_value, color_value, past_history):
    if "what is the weather like?" in value_input:
        print("I am not sure, but i hope it's sunny where you are!")

    elif "history" in value_input:
        print("Here is everything you said so far")
        for index, char in enumerate(past_history):
            print(f'{index}. {char}')
        words = ["sad", "blue", "down"]
        feelings = ["happy", "excited", "joy"]
        if past_history in words:
            print("Am really sorry you feel this way do you want to talk about it?: ")

        elif past_history in feelings:
            print("Your happiness makes me smile too!")

        else:
            print("")

    elif "hi" in value_input or "hello" in value_input:
        print(value1)
        user_active = (input(value4) + ":")
        found = False
        for respond in reply:
            if respond in user_active:
                print(value5)
                found = True
        if not found:
            print("sorry to hear that.")

    elif "how are you" in value_input:
        print(value2, name_value)

    elif "what is your name" in value_input:
        print("I'm Chatbot,your python buddy" + name_value + ".")

    elif "what is my favourite color" in value_input:
        print(f'Your favourite color is {color_value}')

    elif any(word in value_input for word in ["yes", "fine"]):
        print("I'm glade to hear that!")
    elif "summary" in value_input:
        for char in past_history:

    else:
        print("I don't understand that yet.")


# saving user passed input
chat_history = []

color = color_check()
count = 2
while True:
    count -= 1
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)
    save3 = random.choice(reply_option3)
    save4 = random.choice(reply_option4)
    save5 = random.choice(reply_option5)

    # chat loop
    with open("Json.txt", "r") as file:
        data = json.load(file)
        name_log = data["name"]

    if count <= 0:
        question = input("Do you want to continue chatting?:").lower()
        if question == "yes":
            user_input = input("What else would you like to say?:")
            chat_history.append(user_input)
            chat_respond(user_input, save, save2, save4, save5, responds, name_log, color, chat_history)
        elif question == "no":
            print("Okay, goodbye!")
            break
        else:
            print("invalid input,pls enter yes or no.")
    else:
        user_input = input("Type something " + name_log + " (E.g,Hi,Hello):").lower()
        chat_history.append(user_input)
        chat_respond(user_input, save, save2, save4, save5, responds, name_log, color, chat_history)
#couldn't finsh the code because didn't know how to do the summary challenge
#AI Advices in creating the summary logic
#What kind of messages the user said
#✔ Did they greet, ask questions, talk about feelings, etc.
#⭐ SUMMARY LOGIC (Simple & Effective)
#Create counters:
greetings = 0
questions = 0
feelings = 0
#Loop through chat_history and count what appears:
for message in past_history:
    if "hi" in message or "hello" in message:
        greetings += 1
    if "?" in message:
        questions += 1
    if any(word in message for word in ["sad", "happy", "good", "fine"]):
        feelings += 1
#Build the summary result:
print("Here is your chat summary:")
print(f"- You greeted me {greetings} times.")
print(f"- You asked {questions} questions.")
print(f"- You mentioned feelings {feelings} times.")
#RE-Written the logic into the code
import random
import json
reply_options=["Hello there!","Wassup","Hello buddy","HEY!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]
reply_option3=["bye","goodbye","see you later","catch you later",'see you soon']
reply_option4=["how has your day been?","did you do anything fun today?",
               "what have you been up to?","how are you feeling today?"]
reply_option5=["that good","glad to hear that","that awesome"]
responds = ['fine', 'good', 'yes', 'been', ]

# user name
try:
    with open("Json.txt", "r") as f:
        line = json.load(f)
        if "name" not in line:
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            # reading the file
            with open("Json.txt", "r") as file:
               data=json.load(file)
               data["name"]=name_log
            with open("Json.txt","w")as file:
                json.dump(data,file)
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have added you name to memory')
                with open("Json.txt","r") as file:
                    data=json.load(file)
                    data["name"]=name_log
                with open('Json.txt','w')as file:
                    json.dump(data,file)
            else:
                with open("Json.txt", "r") as file:
                  line=json.load(file)
                  save=line["name"]
                print(f'OK {save}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    data={"name":name_log}
    with open("Json.txt","w") as file:
        json.dump(data,file)

def color_check():
    try:
        with open("Json.txt","r") as new_file:
            lines=json.load(new_file)
            if "color" not in lines:
              color_type= input("What is your favourite color?:").strip().capitalize()
              with open("Json.txt", "r") as lod_file:
                  storing=json.load(lod_file)
              storing["color"]=color_type
              with open("Json.txt","w") as lod_file:
                  json.dump(storing,lod_file)
              return color_type
            else:
             change_color=input("Do you want to change your fav color?:").strip().lower()
             while  change_color not in['no','yes']:
                 change_color = input("Do you want to change your fav color?:").strip().lower()
             if change_color=="yes":
                 color_update=input("Enter your new color:").strip().capitalize()
                 with open("Json.txt","r")as file_change:
                     storing=json.load(file_change)
                     storing["color"]=color_update
                 with open("Json.txt","w") as file_change:
                      json.dump(storing,file_change)
                 return color_update
             else:
                 return lines["color"]
    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("Json.txt","w")as file_update:
            storing={"color":fav_color}
            json.dump(storing,file_update)

        return fav_color

def chat_respond(value_input,value1,value2,value4,value5,reply,name_value,color_value,past_history):
    emotions=[]
    if "what is the weather like?" in value_input:
       print("I am not sure, but i hope it's sunny where you are!")

    elif "history" in value_input:
        words = ["sad", "blue", "bad"]
        feelings = ["happy", "great", "joy"]
        print("Here is everything you said so far")
        for index,char in enumerate(past_history):
            print(f'{index}. {char}' )

        for i in emotions:
            if i in words:
                print("You also said you were "+i+",and i am sorry you feel that way")
            elif i in feelings:
                print("You also said you were "+i+",which makes me really happy to hear")
            else:

                print("test")

    elif "hi" in value_input or "hello" in value_input:
        print(value1)
        user_active=(input(value4)+":")
        emotions.append(user_active)
        found=False
        for respond in reply:
            if respond in user_active:
                print(value5)
                found=True
        if not found:
            print("sorry to hear that.")

    elif "how are you" in value_input:
        print(value2,name_value)

    elif "what is your name" in value_input:
         print("I'm Chatbot,your python buddy"+name_value+".")

    elif "what is my favourite color" in value_input:
         print(f'Your favourite color is {color_value}')

    elif any(word in value_input for word in ["yes","fine"]):
        print("I'm glade to hear that!")
    elif "summary" in value_input:
        greetings = 0
        questions = 0
        feelings = 0

        for msg in past_history:
            if "hi" in msg or "hello" in msg:
                greetings += 1
            if "?" in msg:
                questions += 1
            if any(word in msg for word in ["sad", "happy", "good", "fine"]):
                feelings += 1

        print("Here is your chat summary so far:")
        print(f"- You greeted me {greetings} times.")
        print(f"- You asked {questions} questions.")
        print(f"- You talked about feelings {feelings} times.")

    else:
        print("I don't understand that yet.")
#saving user passed input
chat_history=[]

color=color_check()
count=2
while True:
    count-=1
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)
    save3=random.choice(reply_option3)
    save4=random.choice(reply_option4)
    save5=random.choice(reply_option5)

#chat loop
    with open("Json.txt", "r") as file:
        data = json.load(file)
        name_log=data["name"]


    if count<=0:
        question=input("Do you want to continue chatting?:").lower()
        if question=="yes":
            user_input=input("What else would you like to say?:")
            chat_history.append(user_input)
            chat_respond(user_input,save,save2,save4,save5,responds,name_log,color,chat_history)
        elif question=="no":
             print("Okay, goodbye!")
             break
        else:
            print("invalid input,pls enter yes or no.")
    else:
        user_input=input("Type something "+name_log+" (E.g,Hi,Hello):").lower()
        chat_history.append(user_input)
        chat_respond(user_input, save, save2, save4, save5, responds, name_log, color,chat_history)
#AI correction
#PROBLEM 1 — emotions = [] resets every time!
def chat_respond(...):
    emotions=[]
#✅ FIX:
#Move emotions = [] OUTSIDE the function and pass it the same way you pass chat_history.
#❌ PROBLEM 2 — You append the entire user sentence as emotion
#This line:
#emotions.append(user_active)
#I am feeling good today
#Your code stores:
#"I am feeling good today"
#But later you compare:
#if i in ["sad", "blue", "bad"]
#⭐ I WILL FIX EVERYTHING FOR YOU CLEANLY
#Here is the corrected version of your function and the few lines around it.
#I will NOT rewrite your whole code — only the part you need.
def chat_respond(value_input, value1, value2, value4, value5, reply, name_value, color_value, past_history, emotions):

    if "what is the weather like?" in value_input:
        print("I am not sure, but I hope it's sunny where you are!")
        return

    elif "history" in value_input:
        print("Here is everything you said so far:")
        for index, char in enumerate(past_history):
            print(f"{index}. {char}")

        # Emotion report
        sad_words = ["sad", "blue", "bad"]
        happy_words = ["happy", "great", "joy", "good", "fine"]

        for emotion in emotions:
            if emotion in sad_words:
                print(f"You said you felt {emotion}. I'm sorry you're feeling that way.")
            elif emotion in happy_words:
                print(f"You said you felt {emotion}. I'm happy to hear that!")
        return

    elif "hi" in value_input or "hello" in value_input:
        print(value1)
        user_active = input(value4 + ": ").lower()

        # Save emotion only, not full sentence
        for word in ["sad", "happy", "good", "fine", "bad", "great"]:
            if word in user_active:
                emotions.append(word)

        found = False
        for respond in reply:
            if respond in user_active:
                print(value5)
                found = True

        if not found:
            print("Sorry to hear that.")
        return

    elif "how are you" in value_input:
        print(value2, name_value)
        return

    elif "what is your name" in value_input:
        print("I'm Chatbot, your python buddy " + name_value + ".")
        return

    elif "what is my favourite color" in value_input:
        print(f"Your favourite color is {color_value}")
        return

    elif any(word in value_input for word in ["yes", "fine"]):
        print("I'm glad to hear that!")
        return

    elif "summary" in value_input:
        greetings = 0
        questions = 0
        feelings = len(emotions)

        for msg in past_history:
            if "hi" in msg or "hello" in msg:
                greetings += 1
            if "?" in msg:
                questions += 1

        print("Here is your chat summary so far:")
        print(f"- You greeted me {greetings} times.")
        print(f"- You asked {questions} questions.")
        print(f"- You talked about feelings {feelings} times.")
        return

    else:
        print("I don't understand that yet.")
        return
#🚀 STAGE 4 — MINI CHALLENGE A
#Task: Make your chatbot remember the user’s likes
#Add this outside your loop:
#user_likes = []
#Inside your main loop, detect when the user says:
#I like ______
#▶ What you must implement:
#When user types something like:
#i like music
#Your bot should:
#Extract the thing they like (“music”)
#Save it to user_likes
#Reply:
#Cool! I'll remember that you like music.
#Then add a new command:
#what do i like?
#And the bot shows the list of remembered likes.
#My Attempt
def chat_respond(value_input,value1,value2,value4,value5,reply,name_value,color_value,past_history,emotions,store_memories):
    if "what is the weather like?" in value_input:
       print("I am not sure, but i hope it's sunny where you are!")
       return

    elif "history" in value_input:
        print("Here is everything you said so far")
        for index,char in enumerate(past_history):
            print(f'{index}. {char}' )

        #Emotion report
        sad_words  = ["sad", "blue", "bad"]
        happy_words = ["happy", "great", "joy"]

        for emotion in emotions:
            if emotion in sad_words:
                print("You also said you were "+emotion+",and i am sorry you feel that way")
            elif emotion in happy_words:
                print("You also said you were "+emotion+",which makes me really happy to hear")
        return

        # saving what your want to remember
    elif any(value_input in word for word in ["i want you to remember this", "save this to memory"]):
        key = input("Enter only the word you want me to remember?:")
        value = input(f'What do you want to remember about your {key}?:')
        store_memories[key] = value
    # asking for what was saved


    elif any(word in value_input for word in ["what is my","tell me ", "do you remember","what did"] ):
        for memory_key, memory_value in store_memories.items():
            if memory_key in value_input:
               print(f'You said your {memory_key} is {memory_value}.')
            else:
                print("Your haven't told me that yet.")

    elif "hi" in value_input or "hello" in value_input:
        print(value1)
        user_active=(input(value4)+":").lower()
        for words in ["sad", "happy","fine","great","sad","bad","blue"]:
            if words in user_active:
             emotions.append(user_active)

        found=False
        for respond in reply:
            if respond in user_active:
                print(value5)
                found=True
        if not found:
            print("sorry to hear that.")
        return

    elif "how are you" in value_input:
        print(value2,name_value)
        return



    elif "what is your name" in value_input:
         print("I'm Chatbot,your python buddy"+name_value+".")
         return

    elif "what is my favourite color" in value_input:
         print(f'Your favourite color is {color_value}')
         return

    elif any(word in value_input for word in ["yes","fine"]):
        print("I'm glade to hear that!")
        return
    elif "summary" in value_input:
        greetings = 0
        questions = 0
        feelings = 0
#not read come back after church
        for msg in past_history:
            if "hi" in msg or "hello" in msg:
                greetings += 1
            if "?" in msg:
                questions += 1
            if any(word in msg for word in ["sad", "happy", "good", "fine"]):
                feelings += 1

        print("Here is your chat summary so far:")
        print(f"- You greeted me {greetings} times.")
        print(f"- You asked {questions} questions.")
        print(f"- You talked about feelings {feelings} times.")

    else:
        print("I don't understand that yet.")
#saving user passed input
chat_history=[]
emotion_valut= []
color=color_check()
user_like=[]
count=2
#saving user data
memory={}

while True:
    count-=1
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)
    save3=random.choice(reply_option3)
    save4=random.choice(reply_option4)
    save5=random.choice(reply_option5)

#chat loop
    with open("Json.txt", "r") as file:
        data = json.load(file)
        name_log=data["name"]


    if count<=0:
        question=input("Do you want to continue chatting?:").lower()
        if question=="yes":
            user_input=input("What else would you like to say?:")
            chat_history.append(user_input)
            chat_respond(user_input,save,save2,save4,save5,responds,name_log,color,chat_history,emotion_valut,memory)
        elif question=="no":
             print("Okay, goodbye!")
             break
        else:
            print("invalid input,pls enter yes or no.")
    else:
        user_input=input("Type something "+name_log+" (E.g,Hi,Hello):").lower()
        chat_history.append(user_input)
        chat_respond(user_input, save, save2, save4, save5, responds, name_log, color,chat_history,emotion_valut,memory)
#AI correction
#While you code works beautifully it dosen't
#❌ Your bot still does NOT remember user likes such as:
#I like music
#I like football
#I like pizza
# remembering likes
elif value_input.startswith("i like "):
    thing = value_input.replace("i like ", "").strip()
    store_memories.setdefault("likes", [])
    store_memories["likes"].append(thing)
    print(f"Cool! I'll remember that you like {thing}.")
    return

# checking likes
elif "what do i like" in value_input:
    user_likes = store_memories.get("likes", [])
    if user_likes:
        print("You like: " + ", ".join(user_likes))
    else:
        print("You haven't told me what you like yet.")
    return
#(Stage4 part 2)
#1️⃣ INTENT DETECTION SYSTEM
#Create a function:
#def detect_intent(user_input):
#Inside this function, you must detect general categories like:
#✔ Greeting
#If input contains:
#hi, hello, hey
#✔ Asking information
#Contains:
#what, why, how, where, when
#✔ Emotion / Feeling
#Contains:
#sad, happy, angry, tired, good, bad
#✔ Goodbye
#Contains:
#bye, goodnight, see you, take care
#✔ Unknown intention
#If none match → return "unknown"
#➡ Your job:
#Return one of these strings:
#greeting
#"question"
#etc
#2️⃣ PERSONALITY SYSTEM
#Add a variable:
#chatbot_personality = "friendly"
#Then create a function:
#def apply_personality(intent, text):
#This function must change how the chatbot speaks depending on personality.
#At minimum, support 3 personalities:
#🌟 friendly
#warm
#uses emojis
#Example:
#"Hey buddy! 😊 How can I help you today?"
#😎 cool
#short
#confident
#fewer emojis
#Example:
#"Yo. What’s up?"
#🤖 robotic
#no emotions
#straight to the point
#Example:
#"Hello. State your request."
#➡ Your job:
#3️⃣ Add a command:
#"change personality to ___"
#If user types:
#change personality to cool
#You update:
#chatbot_personality = "cool"
#And the bot should answer:
#Personality updated to cool.
#My Attempt
import random
import json
reply_options=["Hello there!","Wassup","Hello buddy","HEY!"]
reply_options2=["I'm doing great hope you are doing great to",
                "I am doing fine,are you doing good to",
                "just enjoying the day, are you enjoying your day"]
reply_option3=["bye","goodbye","see you later","catch you later",'see you soon']
reply_option4=["how has your day been?","did you do anything fun today?",
               "what have you been up to?","how are you feeling today?"]
reply_option5=["that good","glad to hear that","that awesome"]
responds = ['fine', 'good', 'yes', 'been', ]

# user name
try:
    with open("Json.txt", "r") as f:
        line = json.load(f)
        if "name" not in line:
            name_log = input("Hi buddy what your name:").strip().capitalize()
            print(f'Hi {name_log}! Nice to meet you,I have update your name in my memory ')
            # reading the file
            with open("Json.txt", "r") as file:
               data=json.load(file)
               data["name"]=name_log
            with open("Json.txt","w")as file:
                json.dump(data,file)
        else:
            change = input("Do you want to change your name?:").lower()
            #checking input value
            while change not in ['yes','no']:
                print("pls enter yes or no.")
                change = input("Do you want to change your name?:").lower()
            if change == "yes":
                name_log = input("Enter your new name:").strip().capitalize()
                print(f'{name_log}!i have added you name to memory')
                with open("Json.txt","r") as file:
                    data=json.load(file)
                    data["name"]=name_log
                with open('Json.txt','w')as file:
                    json.dump(data,file)
            else:
                with open("Json.txt", "r") as file:
                  line=json.load(file)
                  save=line["name"]
                print(f'OK {save}')
except FileNotFoundError:
    print("File not found, creating a new one")
    name_log=input("Hi buddy what's your name:").strip().capitalize()
    data={"name":name_log}
    with open("Json.txt","w") as file:
        json.dump(data,file)

def color_check():
    try:
        with open("Json.txt","r") as new_file:
            lines=json.load(new_file)
            if "color" not in lines:
              color_type= input("What is your favourite color?:").strip().capitalize()
              with open("Json.txt", "r") as lod_file:
                  storing=json.load(lod_file)
              storing["color"]=color_type
              with open("Json.txt","w") as lod_file:
                  json.dump(storing,lod_file)
              return color_type
            else:
             change_color=input("Do you want to change your fav color?:").strip().lower()
             while  change_color not in['no','yes']:
                 change_color = input("Do you want to change your fav color?:").strip().lower()
             if change_color=="yes":
                 color_update=input("Enter your new color:").strip().capitalize()
                 with open("Json.txt","r")as file_change:
                     storing=json.load(file_change)
                     storing["color"]=color_update
                 with open("Json.txt","w") as file_change:
                      json.dump(storing,file_change)
                 return color_update
             else:
                 return lines["color"]
    except FileNotFoundError:
        print("File not found,creating a new one")
        fav_color = input("What is your favourite color?:").strip().capitalize()
        with open("Json.txt","w")as file_update:
            storing={"color":fav_color}
            json.dump(storing,file_update)

        return fav_color

def chat_respond(value_input,value1,value2,value4,value5,reply,name_value,color_value,past_history,emotions,store_memories):
    if "what is the weather like?" in value_input:
       print("I am not sure, but i hope it's sunny where you are!")
       return

    elif "history" in value_input:
        print("Here is everything you said so far")
        for index,char in enumerate(past_history):
            print(f'{index}. {char}' )

        #Emotion report
        sad_words  = ["sad", "blue", "bad"]
        happy_words = ["happy", "great", "joy"]

        for emotion in emotions:
            if emotion in sad_words:
                print("You also said you were "+emotion+",and i am sorry you feel that way")
            elif emotion in happy_words:
                print("You also said you were "+emotion+",which makes me really happy to hear")
        return

        # saving what your want to remember
    elif any(value_input in word for word in ["i want you to remember this", "save this to memory"]):
        key = input("Enter only the word you want me to remember?:")
        value = input(f'What do you want to remember about your {key}?:')
        store_memories[key] = value
    # asking for what was saved


    elif any(word in value_input for word in ["what is my","tell me ", "do you remember","what did"] ):
        for memory_key, memory_value in store_memories.items():
            if memory_key in value_input:
               print(f'You said your {memory_key} is {memory_value}.')
            else:
                print("Your haven't told me that yet.")

    elif "hi" in value_input or "hello" in value_input:
        print(value1)
        user_active=(input(value4)+":").lower()
        for words in ["sad", "happy","fine","great","sad","bad","blue"]:
            if words in user_active:
             emotions.append(user_active)

        found=False
        for respond in reply:
            if respond in user_active:
                print(value5)
                found=True
        if not found:
            print("sorry to hear that.")
        return

    elif "how are you" in value_input:
        print(value2,name_value)
        return

    # remembering likes
    elif value_input.startswith("i like "):
        thing = value_input.replace("i like ", "").strip()
        store_memories.setdefault("likes", [])
        store_memories["likes"].append(thing)
        print(f"Cool! I'll remember that you like {thing}.")
        return

    # checking likes
    elif "what do i like" in value_input:
        user_likes = store_memories.get("likes", [])
        if user_likes:
            print("You like: " + ", ".join(user_likes))
        else:
            print("You haven't told me what you like yet.")
        return

    elif "what is your name" in value_input:
         print("I'm Chatbot,your python buddy"+name_value+".")
         return

    elif "what is my favourite color" in value_input:
         print(f'Your favourite color is {color_value}')
         return

    elif any(word in value_input for word in ["yes","fine"]):
        print("I'm glade to hear that!")
        return
    elif "summary" in value_input:
        greetings = 0
        questions = 0
        feelings = 0
#not read come back after church
        for msg in past_history:
            if "hi" in msg or "hello" in msg:
                greetings += 1
            if "?" in msg:
                questions += 1
            if any(word in msg for word in ["sad", "happy", "good", "fine"]):
                feelings += 1

        print("Here is your chat summary so far:")
        print(f"- You greeted me {greetings} times.")
        print(f"- You asked {questions} questions.")
        print(f"- You talked about feelings {feelings} times.")

    else:
        print("I don't understand that yet.")
    # Creating a function detection system


def detect_intent(user_data):
    user_message = {}
    greetings = ["hi", "hello", "hey"]
    asking_info = ["what", "why", "how", "where", "when"]
    emotions = ["sad", "happy", "angry", "tried", "good", "bad"]
    closing = ["bye", "goodnight", "see you", "take care"]
    user_message["greeting"] = greetings
    user_message["asking"] = asking_info
    user_message["emotions"] = emotions
    user_message["closing"] = closing

    for msg_key, msg_value in user_message.items():
        for save_msg in msg_value:
            if save_msg in user_data:
                return msg_key
    return "none"
def apply_personality(option,intent):
    if intent == "greeting":
        option

#saving user passed input
chat_history=[]
emotion_valut= []
color=color_check()
user_like=[]
count=2
#saving user data
memory={}

while True:
    count-=1
    save = random.choice(reply_options)
    save2 = random.choice(reply_options2)
    save3=random.choice(reply_option3)
    save4=random.choice(reply_option4)
    save5=random.choice(reply_option5)

#chat loop
    with open("Json.txt", "r") as file:
        data = json.load(file)
        name_log=data["name"]


    if count<=0:
        question=input("Do you want to continue chatting?:").lower()
        if question=="yes":
            user_input = input("What else would you like to say?:")
            chat_history.append(user_input)
            detect_intent(user_input)
            print("Choose a personal")
            print("1).Friendly")
            print("2).Friendly")
            print("3).Robotic")
            choice=input("Enter your choice:")
            apply_personality(choice,user_input)


            chat_respond(user_input,save,save2,save4,save5,responds,name_log,color,chat_history,emotion_valut,memory)
        elif question=="no":
             print("Okay, goodbye!")
             break
        else:
            print("invalid input,pls enter yes or no.")
    else:
        user_input = input("Type something " + name_log + " (E.g,Hi,Hello):").lower()
        chat_history.append(user_input)
        detect_intent(user_input)
        print("Choose a personal")
        print("1).Friendly")
        print("2).Friendly")
        print("3).Robotic")
        choice=input("Enter your choice:")
        apply_personality(choice, user_input)

        chat_respond(user_input, save, save2, save4, save5, responds, name_log, color,chat_history,emotion_valut,memory)
        detect_intent(user_input)













