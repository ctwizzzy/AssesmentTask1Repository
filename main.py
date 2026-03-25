import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# api_key to access the openweathermap api
api_key = "e876a78b187169afe904665924052543"

# The file name for the csv file which will be used to store the input history of the user
history_file_name = "weather_history.csv"


# Retreives real time weather data based on the city name provided by the user
def retreive_weather_by_city_name():

    city = input("Enter city: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\nCity:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity)
        print("Weather:", weather)

        save_weather_search(city,temp,humidity,weather)

    else:
        print("Error:", data.get("message"))


# Uses pandas to save the search history of the users inputs to a csv file. 
def save_weather_search(city,temp,humidity,weather):

    df = pd.DataFrame([[city,temp,humidity,weather]],
                      columns=["City","Temperature","Humidity","Weather"])

    if os.path.exists(history_file_name):
        df.to_csv(history_file_name,mode="a",header=False,index=False)
    else:
        df.to_csv(history_file_name,index=False)


# Displays previously searched cities by the user and displays the weather data for those cities using pandas
def display_user_weather_search_history():

    if os.path.exists(history_file_name):

        df = pd.read_csv(history_file_name)
        print("\nSearch History\n")
        print(df)

    else:
        print("No history found.")


# Generates a city temperature graph using matoplotlib 
def create_temperature_graph():

    if os.path.exists(history_file_name):

        df = pd.read_csv(history_file_name)

        plt.figure()

        plt.bar(df["City"],df["Temperature"])

        plt.title("Temperature by City")

        plt.xlabel("City")

        plt.ylabel("Temperature °C")

        plt.show()

    else:
        print("No weather data available")


# The main menu system which the user interacts with
while True:

    print("\n====== Weather App ======")
    print("1. Search Weather Of City")
    print("2. View Search History")
    print("3. Generate City Temperature Graph")
    print("4. Exit Program")

    choice = input("Choose option: ")

    if choice == "1":
        retreive_weather_by_city_name()

    elif choice == "2":
        display_user_weather_search_history()

    elif choice == "3":
        create_temperature_graph()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid city choice, please try again and check for spelling errors")