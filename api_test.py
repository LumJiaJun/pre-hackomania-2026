import requests # make api calls
import json # reading api's response

url = "https://api.open-meteo.com/v1/forecast?latitude=1.3521&longitude=103.8198&current=temperature_2m,weathercode,windspeed_10m&timezone=Asia%2FSingapore"

print("Calling weather API...")
response = requests.get(url)

if (response.status_code == 200):
    print(f"Success! {response.status_code}\n")
else:
    print(f"Error! {response.status_code}")
    exit()

data = response.json()

# dig into nested data
current = data["current"]

print("Current Weather in Singapore")
print(f"Time:       {current['time']}")
print(f"Temperature:{current['temperature_2m']} deg C")
print(f"Wind Speed: {current['windspeed_10m']} km/h")

print("\n Raw JSON from API:")
print(json.dumps(current, indent = 2))

print("\n Python and APIs are working!")