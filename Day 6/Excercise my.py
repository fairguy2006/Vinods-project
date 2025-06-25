import requests
def get_weather(city):
    url = f"https://wttr.in{city}?format=3"
    try:
         response = requests.get(url)
         if "Unknown location" in response.tet or "Sorry" in response.text:
            return f"{city}: Invalid city"
         else:
             return response.text
    except requests.RequestException:
        return "Network error. Please try again later."
while True:
        city = input("Enter a city name (or type'exit' to quit): ").strip()
        if city.lower() == "exit":
            break
        if not city:
            continue
        print(get_weather(city))