import requests

cities = input("Enter city names separated by commas: ")
city_list = [c.strip() for c in cities.split(",")]
valid_count = 0
invalid_count = 0
for city in city_list:
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    if "Unknown location" in response.text or "Sorry" in response.text:
        print(f"{city}: Invalid city")
        invalid_count += 1
    else:
        print(response.text)
        valid_count += 1
    print(f"\nvalid cities: {valid_count}")
    print(f"Invalid cities: {invalid_count}")
