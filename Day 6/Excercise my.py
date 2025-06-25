import requests

def is_valid_city(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    try:
        response = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
        data = response.json()
        city_lower = city.lower()
        for place in data:
            if place.get("class") == "place" and place.get("type") in ["city", "town", "village"]:
                display_name = place.get("display_name", "").lower()
                # Check if city is a whole word in display_name
                if f" {city_lower} " in f" {display_name} ":
                    return True
        return False
    except requests.RequestException:
        print("Network error. Please try again later.")
        return False

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Could not retrieve weather information."
    except requests.RequestException:
        return "Network error while fetching weather."

while True:
    city = input("Enter a city name (or type 'exit' to quit): ").strip()
    if city.lower() == "exit":
        break
    if not city:
        continue
    if not is_valid_city(city):
        print("Invalid city name. Please try again.")
        continue
    print(get_weather(city))