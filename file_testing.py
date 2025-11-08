#🧠 CHALLENGE 6: Auto Summary Backup System
#🎯 Goal
#When the user views a monthly summary (option 3),
#your program should automatically save that summary into a new text file named:
#summary_YYYY-MM.txt
#⚙️ Requirements
#When the user views the monthly summary (option 3):
#Collect the same information you already print (temperatures, weather counts, averages, etc.)
#Then write it into a new file (e.g., summary_2025-10.txt).
#If the file already exists for that month, overwrite it with the updated summary.
#Display a message like:
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
