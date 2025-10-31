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



