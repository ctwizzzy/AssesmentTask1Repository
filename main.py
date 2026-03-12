import requests



BASE_URL = "https://v3.football.api-sports.io/teams"

KEY="6d4677aed879c7c68f81b280ae6099c9"


headers = {
        'x-apisports-key': KEY
    }

params = {
    'id': '33'
}


response = requests.get(BASE_URL, headers=headers, params=params )

if response.status_code == 200:
   print(response.json())
else:
    print(f"Error {response.status_code}")