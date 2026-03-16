# import requests
# import pandas as pd

# BASE_URL = "https://v3.football.api-sports.io/teams"
# # API key
# KEY="6d4677aed879c7c68f81b280ae6099c9"

# headers = {
#         'x-apisports-key': KEY
#     }
# # The question the terminal will ask the user when the code is run
# user_wants_team = input("What team you would like to find").capitalize()

# # 
# params = {
#    "name": user_wants_team
# }

# response = requests.get(BASE_URL, headers=headers, params=params )

# data = response.json()

# if data.get('results') == 0:
#     print("Failed to find an accurate result check your spelling and fix it for a result")
# elif response.status_code == 200:
#    print(response.json())
# else:
#     print(f"Error {response.status_code}")

# def print_info(data):
#     print(f'Team Name is {data["name"]}')
    
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

api_key = "92bac66084657b12ee8a93b11129c2a5"

file_name = "history.csv"


# Weather function
def get_weather():

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

        save_history(city,temp,humidity,weather)

    else:
        print("Error:", data.get("message"))


# Save history using pandas
def save_history(city,temp,humidity,weather):

    df = pd.DataFrame([[city,temp,humidity,weather]],
                      columns=["City","Temperature","Humidity","Weather"])

    if os.path.exists(file_name):
        df.to_csv(file_name,mode="a",header=False,index=False)
    else:
        df.to_csv(file_name,index=False)


# View history
def view_history():

    if os.path.exists(file_name):

        df = pd.read_csv(file_name)
        print("\nSearch History\n")
        print(df)

    else:
        print("No history found.")


# Temperature graph
def show_graph():

    if os.path.exists(file_name):

        df = pd.read_csv(file_name)

        plt.figure()

        plt.bar(df["City"],df["Temperature"])

        plt.title("Temperature by City")

        plt.xlabel("City")

        plt.ylabel("Temperature °C")

        plt.show()

    else:
        print("No data available")


# Menu system
while True:

    print("\n====== Weather App ======")
    print("1. Search Weather")
    print("2. View History")
    print("3. Show Temperature Graph")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        get_weather()

    elif choice == "2":
        view_history()

    elif choice == "3":
        show_graph()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice")