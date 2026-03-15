import requests



BASE_URL = "https://v3.football.api-sports.io/teams"

KEY="6d4677aed879c7c68f81b280ae6099c9"


headers = {
        'x-apisports-key': KEY
    }

user_wants_team = input("What team you would like to find").capitalize()



params = {
   "name": user_wants_team
}


response = requests.get(BASE_URL, headers=headers, params=params )

data = response.json()

if data.get('results') == 0:
    print("Failed to find an accurate result check your spelling and fix it for a result")
elif response.status_code == 200:
   print(response.json())
else:
    print(f"Error {response.status_code}")