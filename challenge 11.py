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

#🧠 CHALLENGE 3: Monthly Weather Summary
#You’ll add a new menu option:
#3.) View Monthly Summary”
#This feature should:
#Ask the user for a month in this format → YYYY-MM (for example, 2025-10)
#Go through the "weather_log.txt" file and find all entries that start with that month.
#Example log lines:
#2025-10-01,32°C,Sunny
#2025-10-02,28°C,Rainy
#2025-10-03,30°C,Sunny
#Count how many days were Sunny, Rainy, Windy, or Snowing.
#Then print something like this:
#Summary for 2025-10
#Sunny: 2 days
#Rainy: 1 day
#Windy: 0 days
#Snowing: 0 days
#MY Attempt 
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
    
#Challenge 4 Goal
#You’ll add a new feature to show monthly weather statistics — including:
#🌡️ Average temperature
#Lowest temperature
#🔥 Highest temperature
#🧩 How It Works
#When the user picks the option (e.g., “View monthly summary”):
#The program will:
#Search for all entries that match the selected month (YYYY-MM).
#Collect all the temperatures for that month.
#Calculate:
#The average temperature
#The lowest temperature
#The highest temperature
#Display them neatly at the end of the summary.
#My attempts 
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

def summary_review():
    save=[]
    temps=[]
    weather_count={"sunny":0,"rainy":0,"windy":0,"snowing":0}
    search=input("Enter the month you are searching for in this format(YYYY-MM):")
    found=False
    try:
        with open("weather_log.txt","r")as file:
            line=file.readlines()
        for char in line:
            if search in char:
               save.append(char)
            part=char.split(',')
            temp=int(part[1].replace('°C','').strip())
            temps.append(temp)
            found = True
            for weather in weather_count:
                   if weather in char.lower() :
                       weather_count[weather]+=1
        if found:
         print("\nHere is the month summary for " + search)
         for entry in save:
            print(entry.strip())
         print(f'\nWeather description for {search}')
         for weather,count in weather_count.items():
            print(f'{weather.capitalize()} {count} days')
        #Tempeture_cal
         avg_temp=sum(temps)/len(temps)
         lowest_temp=min(temps)
         highest_temp=max(temps)
         print("\nWeather statistics")
         print(f'average temp:{avg_temp}')
         print(f'lowest temp:{lowest_temp}')
         print(f'highest temp:{highest_temp}')
        if not found:
            print("No record found for " + search)

    except FileNotFoundError:
        print("No file exists for that date")


while True:
     print("Available options\n")
     print("1.)Log weather condition")
     print("2.)Show past Logs")
     print("3.)View monthly summary")
     print("4.)EXIT Program")
     option=input("What do you want to do?:")
     if option=="1":
        temperature_checker()
     elif option=="2":
        history_checker()
     elif option=="3":
         summary_review()
     elif option=="4":
        print("Goodbye")
        break
     else:
        print("invalid option.Try again.")

#AI Correction
#Small Issues to Fix:
#1. Temperature extraction runs for all lines — not just the searched month.
#You’re doing this:
#if search in char:
#    save.append(char)
#part = char.split(',')
#temp = int(part[1].replace('°C','').strip())
#temps.append(temp)
#✅ Fix: Move the temperature lines inside the if search in char: block:
#if search in char:
#   save.append(char)
#   part = char.split(',')
#   temp = int(part[1].replace('°C','').strip())
#    temps.append(temp)
#    found = True
#    for weather in weather_count:
#        if weather in char.lower():
#            weather_count[weather] += 1
#Handle case when there are no temperature entries
#if temps:
#    avg_temp = sum(temps) / len(temps)
#    lowest_temp = min(temps)
#    highest_temp = max(temps)
#    print("\nWeather statistics:")
#    print(f'Average temperature: {avg_temp:.1f}°C')
#    print(f'Lowest temperature: {lowest_temp}°C')
#   print(f'Highest temperature: {highest_temp}°C')
#else:
    #print("\nNo temperature data available for this month.")   
#Challenge 5
# enhancement idea (for Challenge 5 😉)
#Add a “delete log entry” or “update entry” feature to practice reading, editing, and rewriting a file — that’s going to be our next step 😎
#My Attempt
import datetime
def temperature_checker():
    temperature=int(input("Enter weather condition in Celsius:"))
    print("\nWeather description available")
    print("Sunny","Rainy","Windy","Snowing")
    weather_description=input("Enter weather description:").lower().strip()
    while weather_description not in ["sunny","rainy","windy","snowing"]:
        print("Please enter one of the available weather descriptions:")
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

def summary_review():
    save=[]
    temps=[]
    weather_count={"sunny":0,"rainy":0,"windy":0,"snowing":0}
    search=input("Enter the month you are searching for in this format(YYYY-MM):")
    found=False
    try:
        with open("weather_log.txt","r")as file:
            line=file.readlines()
        for char in line:
            if search in char:
               save.append(char)
               part=char.split(',')
               temp=int(part[1].replace('°C','').strip())
               temps.append(temp)
               found = True
               for weather in weather_count:
                   if weather in char.lower() :
                       weather_count[weather]+=1
        if found:
         print("\nHere is the month summary for " + search)
         for entry in save:
            print(entry.strip())
         print(f'\nWeather description for {search}')
         for weather,count in weather_count.items():
            print(f'{weather.capitalize()} {count} days')
        #Tempeture_cal
         if temps:
          avg_temp=sum(temps)/len(temps)
          lowest_temp=min(temps)
          highest_temp=max(temps)
          print("\nWeather statistics")
          print(f'average temp:{avg_temp}')
          print(f'lowest temp:{lowest_temp}')
          print(f'highest temp:{highest_temp}')
        else:
            print("No date on temp for the month of "+search)
        if not found:
            print("No record found for " + search)

    except FileNotFoundError:
        print("No file exists for that date")

def deleting_file():
   search=input("Enter record of the month you are searching for in this format(YYYY-MM-DD):")
   try:
      with open("weather_log.txt","r")as file:
       line=file.readlines()
       for char in line:
           if not char.startswith(search):
              with open("weather_log.txt","w")as new_file:
                    file.writelines(f'{char}')
                    print("Weather record for "+search+" deleted successfully.")
   except FileNotFoundError:
       print("No file exist for that date yet.")
while True:
     print("Available options\n")
     print("1.)Log weather condition")
     print("2.)Show past Logs")
     print("3.)View monthly summary")
     print("4.)Delete entry")
     print("5.)EXIT Program")
     option=input("What do you want to do?:")
     if option=="1":
        temperature_checker()
     elif option=="2":
        history_checker()
     elif option=="3":
         summary_review()
     elif option =="4":
         deleting_file()
     elif option=="5":
        print("Goodbye")
        break
     else:
        print("invalid option.Try again.")
#AI Correction
#for char in line:
#   if not char.startswith(search):
#        with open("weather_log.txt","w")as new_file:
#             file.writelines(f'{char}')
#Here’s what happens:
#For every line, you open the file in “write” mode ('w'), which erases everything that was written before.
#So at the end, only the last line survives in your file 😅
#correct version
def deleting_file():
    search = input("Enter record date to delete (YYYY-MM-DD): ").strip()
    try:
        with open("weather_log.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("weather_log.txt", "w") as new_file:
            for line in lines:
                if search not in line:
                   new_file.write(line)
                else:
                    found = True

        if found:
            print(f"✅ Weather record for {search} deleted successfully.")
        else:
            print(f"❌ No record found for {search}.")
    except FileNotFoundError:
        print("⚠️ No weather log file exists yet. Please log some entries first.")

#🧠 CHALLENGE 6: Auto Summary Backup System
#When the user views a monthly summary (option 3),
#your program should automatically save that summary into a new text file named:
#summary_YYYY-MM.txt
#⚙️ Requirements
#When the user views the monthly summary (option 3):
#Collect the same information you already print (temperatures, weather counts, averages, etc.)
#Then write it into a new file (e.g., summary_2025-10.txt).
#If the file already exists for that month, overwrite it with the updated summary.
#Display a message like:
#Monthly summary for 2025-10 saved to summary_2025-10.txt
#My Attempt
  save=[]
    temps=[]
    weather_count={"sunny":0,"rainy":0,"windy":0,"snowing":0}
    search=input("Enter the month you are searching for in this format(YYYY-MM):")
    found=False
    try:
        with open("weather_log.txt","r")as file:
            line=file.readlines()
        for char in line:
            if search in char:
               save.append(char)
               part=char.split(',')
               temp=int(part[1].replace('°C','').strip())
               temps.append(temp)
               found = True
               for weather in weather_count:
                   if weather in char.lower() :
                       weather_count[weather]+=1
        if found:
         print("\nHere is the month summary for " + search)
         for entry in save:
            print(entry.strip())
         print(f'\nWeather description for {search}')
         for weather,count in weather_count.items():
            print(f'{weather.capitalize()} {count} days')
        #Tempeture_cal
         if temps:
          avg_temp=sum(temps)/len(temps)
          lowest_temp=min(temps)
          highest_temp=max(temps)
          print("\nWeather statistics")
          print(f'average temp:{avg_temp:.2f}')
          print(f'lowest temp:{lowest_temp}')
          print(f'highest temp:{highest_temp}')
          #collecting summary:I put it here because of avg_temp
          with open(f'summary{search}.txt,'"r") as file:
              lines=file.readlines()
              for line in lines:
                  if search not in line:
                    with open(f'summary{search}.txt','a')as new_file:
                      file.write(f'Monthly Summary for {search}\n')
                      file.write(f'{temps} {weather_count} {avg_temp}')
                  else: 
        else:
            print("No date on temp for the month of "+search)
        if not found:
            print("No record found for " + search)
    except FileNotFoundError:
        print("No file exists for that date")
#i think of the logic to complete the code this is what i was able to write 
#AI Correction
def summary_review():
    save = []
    temps = []
    weather_count = {"sunny": 0, "rainy": 0, "windy": 0, "snowing": 0}
    search = input("Enter the month you are searching for in this format (YYYY-MM): ")
    found = False

    try:
        with open("weather_log.txt", "r") as file:
            lines = file.readlines()

        for char in lines:
            if search in char:
                save.append(char)
                part = char.split(',')
                temp = int(part[1].replace('°C', '').strip())
                temps.append(temp)
                found = True
                for weather in weather_count:
                    if weather in char.lower():
                        weather_count[weather] += 1

        if found:
            print(f"\nHere is the month summary for {search}")
            for entry in save:
                print(entry.strip())

            print(f"\nWeather description for {search}")
            for weather, count in weather_count.items():
                print(f"{weather.capitalize()}: {count} days")

            # Temperature calculations
            if temps:
                avg_temp = sum(temps) / len(temps)
                lowest_temp = min(temps)
                highest_temp = max(temps)

                print("\nWeather statistics")
                print(f"Average temp: {avg_temp:.2f}°C")
                print(f"Lowest temp: {lowest_temp}°C")
                print(f"Highest temp: {highest_temp}°C")

                # Save the summary to a new file
                summary_file = f"summary_{search}.txt"
                with open(summary_file, "w") as file:
                    file.write(f"Monthly Weather Summary for {search}\n\n")
                    for entry in save:
                        file.write(entry)
                    file.write("\nWeather Counts:\n")
                    for weather, count in weather_count.items():
                        file.write(f"{weather.capitalize()}: {count} days\n")
                    file.write("\nTemperature Stats:\n")
                    file.write(f"Average: {avg_temp:.2f}°C\n")
                    file.write(f"Lowest: {lowest_temp}°C\n")
                    file.write(f"Highest: {highest_temp}°C\n")

                print(f"\n✅ Monthly summary saved to {summary_file}")

            else:
                print("No temperature data found for that month.")
        else:
            print("No record found for " + search)

    except FileNotFoundError:
        print("No file exists for that date.")








 
