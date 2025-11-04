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


