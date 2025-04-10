import requests

API_KEY = "cd11d6c2f2870e35a11447f30fc4c0ff"
CITY = input("Enter city name You want to know?")

url=f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(f"Weather in {CITY}: {data['weather'][0]['description']}")
print(f"Temperature: {data[main]['temp']}°C")

