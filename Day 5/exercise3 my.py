# Save valid and invalid city weather results to text files
import requests
cities = input("Enter city name separated by commas: ")
city_list = [c.strip() for c in cities.split(",")]
with open("valid_weather.txt", "a") as valid_file, open("invalid_cities.txt", "a") as invalid_file:
     for city in city_list:
        if not city:
            continue
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if "Unknown location" in response.text or "Sorry" in response.text:
            print(f"{city}: Invalid city")
            invalid_file.write(f"{city}\n")
        else:
            print(response.text)
            valid_file.write(response.text + "\n"
                             )                 
