import requests

# Base URL for NASA's Astronomy Picture of the Day (APOD) API
API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "YOUR_KEY"  # Replace with your NASA API key

def fetch_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day (APOD)."""
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date  # Format: YYYY-MM-DD
    
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title", "Unknown"),
            "date": data.get("date", "Unknown"),
            "explanation": data.get("explanation", "No description available."),
            "image_url": data.get("url", "No image available")
        }
    else:
        print("Error fetching data from NASA API.")
        return None

def display_apod(apod_data):
    """Display APOD details."""
    if apod_data:
        print(f"Title: {apod_data['title']}")
        print(f"Date: {apod_data['date']}")
        print(f"Description: {apod_data['explanation'][:200]}...")
        print(f"Image URL: {apod_data['image_url']}")
    else:
        print("No data to display.")