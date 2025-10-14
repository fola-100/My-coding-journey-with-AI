k#🧩 Step Plan
#Show Menu Options
#Add new weather entry
#View past entries
#Exit program
#Record Weather Entry
#Get today’s date automatically
#Ask for weather condition (e.g., “Sunny”, “Rainy”, “Cloudy”, etc.)
#Save it in a file like this:
#2025-10-05 → Sunny
#View History
#Read from the file and show all saved entries.
#Optionally, allow user to search for a specific date later.
#MY Attempts
import datetime
while True:
     print("Option Available")
     print("1.)Add new weather entry")
     print("2.)View past entries")
     print("3.)Exit program")
     choice=input("Enter choice:")
     #Add new weather entry
     if choice=="1":
         print("---Weather Condition---")
         print("i.)Sunny")
         print("ii.)Rainy")
         print("iii.)Cloudy")
         print("iv.)Mist")
         weather=input("Enter weather condition:").lower()
         if weather not in ["sunny","rainy","cloudy","mist"]:
             print("Invalid weather condition")
             continue
         time = datetime.datetime.now().strftime("%Y-%m-%d")
         with open("weather.txt","a")as file:
             file.write(f'{time} {weather}')
         print(f'{time} Weather condition {weather} has been logged')
     elif choice=="2":
         print("Enter the date, year and month")
         search=input("What date are you searching for?:")
         with open("weather.txt","r") as file:
             saved=file.readline()
             found=False
             for line in saved:
                 if search in line:
                     print(line)
                     found=True
             if not found:
                print("No sure date saved")
                continue
     elif choice=="3":
         print("Thank you and goodbye.")
         break
#AI Correction 
import datetime

while True:
    print("\n--- Option Available ---")
    print("1.) Add new weather entry")
    print("2.) View past entries")
    print("3.) Exit program")

    choice = input("Enter choice: ").strip()

    # 1️⃣ Add new weather entry
    if choice == "1":
        print("--- Weather Conditions ---")
        print("i.) Sunny")
        print("ii.) Rainy")
        print("iii.) Cloudy")
        print("iv.) Mist")

        weather = input("Enter weather condition: ").lower()

        if weather not in ["sunny", "rainy", "cloudy", "mist"]:
            print("Invalid weather condition. Please choose from the list.")
            continue

        time = datetime.datetime.now().strftime("%Y-%m-%d")

        with open("weather.txt", "a") as file:
            file.write(f"{time} {weather}\n")

        print(f"{time}: Weather condition '{weather}' has been logged ✅")

    # 2️⃣ View past entries
    elif choice == "2":
        search = input("Enter date to search (YYYY-MM-DD): ").strip()
        found = False

        try:
            with open("weather.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if search in line:
                        print(f"✅ Found: {line.strip()}")
                        found = True

            if not found:
                print("No weather record found for that date.")

        except FileNotFoundError:
            print("No weather records found yet. Please log something first.")

    # 3️⃣ Exit
    elif choice == "3":
        print("Thank you for using Weather Journal. Goodbye! 🌤️")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")






