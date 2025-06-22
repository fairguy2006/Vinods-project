import requests
city =input("Enter the name of the city:")
url = f"http://api.weatherapi.com/v1/current.json
response = requests.get(url)
print(response.text)