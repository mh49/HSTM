
import requests

# api_address='http://api.openweathermap.org/data/2.5/weather?lat=35.93&lon=0.09&APPID=046afe7166cc4ba51e9ef2026ce0e362'

api_address='http://api.openweathermap.org/data/2.5/weather?id=2487134&APPID=046afe7166cc4ba51e9ef2026ce0e362'

city = "Mesra"    # input('City Name :')
# url = api_address + city
json_data = requests.get(api_address).json()

print(json_data)

