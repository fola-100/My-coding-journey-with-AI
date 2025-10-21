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
 
