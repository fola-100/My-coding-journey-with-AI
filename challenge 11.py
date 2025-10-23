#Here’s Weather Journal – Challenge 1 (Basic Edition):
#🧩 Challenge 1: Weather Logger
#Goal:
#Create a small program that lets the user enter today’s weather and saves it in a file called weather_log.txt.
#Requirements:
#Ask the user for:
#The date (you can also auto-generate it if you want using datetime).
#The temperature (in Celsius).
#A short description of the weather (e.g., “Sunny”, “Rainy”, “Windy”).
#Save the info to a file weather_log.txt in this format:
#2025-10-05 | 30°C | Sunny
#Each time the program runs, it should add a new entry (not overwrite the old ones)
#My attempts
import datetime
temperature=int(input("Enter weather condition in Celsius:"))
print("\nWeather description available")
print("Sunny","Rainy","Windy")
weather_description=input("Enter weather description").lower().strip()
while weather_description not in ['sunny','rainy','windy']:
    print("Enter the three weather description available")
    weather_description=input("Enter weather description")
auto_generate=datetime.datetime.now().strftime('%y,%m,%d')
with open("weather_log.txt","a") as file:
    file.write(f'{auto_generate},{temperature},{weather_description}')
    print(f'Weather date {auto_generate},temperature {temperature},and description {weather_description} has been saved')
#AI corrections
#Date format
#You used '%y,%m,%d', which adds commas.
#Example: 25,10,05
#It’s better to use '%Y-%m-%d' → 2025-10-05, easier to read.
#File formatting
#Right now, all logs might appear on one line since there’s no newline (\n).
#Add \n before writing the entry.
#User experience
#When asking for input, it’s good to add a space at the end (so it looks neat).

#🌤️ Challenge 2: View Past Weather Entries
#Challenge Description
#Write a Python program that:
#Asks the user to enter a date (in the format YYYY-MM-DD — e.g., 2025-10-05).
#Opens the file weather_log.txt.
#Searches for lines that contain that date.
#If found — print all matching entries.
#If not found — show a message like "No record found for that date."
#Use a try-except block in case the file doesn’t exist yet.
#My Attempt 
import datetime
def temperature_checker():
    temperature=int(input("Enter weather condition in Celsius:"))
    print("\nWeather description available")
    print("Sunny","Rainy","Windy","Snowing")
    weather_description=input("Enter weather description:").lower().strip()
    while weather_description not in ["sunny","rainy","windy","snowing"]:
        print("Enter the three weather description available")
        weather_description=input("Enter weather description:").lower().strip()
    auto_generate=datetime.datetime.now().strftime("%Y-%m-%d")
    with open("weather_log.txt","a") as file:
        file.write(f'{auto_generate},{temperature}°C,{weather_description.capitalize()}\n')
        print(f'Weather date {auto_generate},temperature {temperature},and description {weather_description.capitalize()} has been saved')
def history_checker():
    try:
       search=input("What date are you searching for? Entry formate:(YYYY-MM-DD):")
       found=False
       with open("weather_log.txt","r") as file:
        save=file.readlines()
       for char in save:
        if search in char:
            print("\nHere is your past Weather Entries")
            print(char)
            found=True
        if not found:
           print("No record found for that date")
    except FileNotFoundError:
        print("No record found for that date.")



while True:
     print("Available options\n")
     print("1.)Log weather condition")
     print("2.)Show past Logs")
     print("3.)EXIT Program")
     option=input("What do you want to do?:")
     if option=="1":
        temperature_checker()
     elif option=="2":
        history_checker()
     elif option=="3":
        print("Goodbye")
        break
     else:
        print("invalid option.Try again.")
#AI CORRECTION 
#Excellent job, Olamide! You just built a two-feature weather journal — one for logging and one for searching past entries.
#here are a few improvement or correction 
#Small Fix (Logic in history_checker)
#Inside your loop:
#➡️ The if not found: should be after the for loop, not inside it.
#Right now, it prints “No record found” for every line that doesn’t match — even if one later matches.
def history_checker():
    try:
        search = input("What date are you searching for? Entry format (YYYY-MM-DD): ")
        found = False
        with open("weather_log.txt", "r") as file:
            save = file.readlines()
        for line in save:
            if search in line:
                if not found:
                    print("\nHere is your past Weather Entries:")
                print(line.strip())
                found = True
        if not found:
            print("No record found for that date.")
    except FileNotFoundError:
        print("No record found yet. Please log something first.")

        




 
