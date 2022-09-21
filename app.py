import requests

from celsius_converter import celsius_converter

api_key = '3e77de4b98cfb3b5c5e7ed7af9b06bc7'
user_input = input("Enter city: ")
print(user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])
celsius_temp = celsius_converter(temp)

print(f"The weather in {user_input} is {weather}")
print(f"The temperature in {user_input} is {celsius_temp} C")


# print(weather_data.status_code)



