import requests

LAT = "<your lattitude>"
LON = "<your longitude>"

API_KEY = "<your api key>"

URL = "https://api.openweathermap.org/data/2.5/onecall"

parameter = {
    "lat":LAT,
    "lon":LON,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"

}

response = requests.get(URL,params=parameter)
data = response.json()['hourly']
weather_id = [data[i]['weather'][0]['id'] for i in range(13)]

for i in weather_id:
    if i < 700:
        print("Bring Umbrella")
