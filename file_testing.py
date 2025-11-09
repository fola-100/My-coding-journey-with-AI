#Stage 3 Challenge Description
#Make your chatbot:
#Ask the user for their name (if it doesn’t already know it).
#Store it in a variable.
#Use that name in its responses (e.g., “Hi Olamide! Nice to meet you!”).
#Still respond to things like “hi”, “how are you”, etc., just like before — but now, include the user’s name when replying.
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