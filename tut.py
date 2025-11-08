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










































































































































































































































































































































































































































































