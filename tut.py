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
    weather_count={"sunny":0,"rainy":0,"windy":0,"snowing":0}
    search=input("Enter the month you are searching for in this format(YYYY-MM):")
    found=False
    try:
        with open("weather_log.txt","r")as file:
            line=file.readlines()
        for char in line:
            if search in char:
               save.append(char)
               found = True
               for weather in weather_count:
                   if weather in char.lower() :
                       weather_count[weather]+=1
        if found:
         print("\nHere is the month summary for " + search)
         for entry in save:
            print(entry.strip())
         print(f'\nWeather description for{search}')
         for weather,count in weather_count.items():
            print(f'{weather.capitalize()} {count} days')
        if not found:
            print("No record found for " + search)


    except FileNotFoundError:
        print("No file exists for that date")


while True:
     print("Available options\n")
     print("1.)Log weather condition")
     print("2.)Show past Logs")
     print("3.View monthly summary")
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

#lesson learnt
#1) tinary only work for when you to check to conditions e.g if else and not for elif
#2) you can store variable inside a function
#3)sometime you might get and error saying "An illegal target for a variable annotation"
#which means you 








































































































































































































































































































































































































































































