import requests
from kivy.app import App
from kivy.uix.widget import Widget

api_key = "fdb74f3799bfe740d585f1fd0dd8a6e3"

location = "stockholm"

result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}")

description = result.json()["weather"][0]["description"]
temperature = round(result.json()["main"]["temp"])
feels_like = round(result.json()["main"]["feels_like"])
high = round(result.json()["main"]["temp_max"])
low = round(result.json()["main"]["temp_min"])

#print (f"{place}\n{temp}\n{ftemp}\n{desc}\n{hilo}")

class WeatherWindow(Widget) :
    stuff = "sampletext"

class WeatherApp(App) :
    place = f"{location[0].upper()}{location[1:]}"
    temp = f"{temperature}° C"
    ftemp = f"Feels like {feels_like}° C."
    desc = f"{description[0].upper()}{description[1:]}"
    hilo = f"Today's high is {high}° C and today's low is {low}° C."
    def build(self) :
        app = WeatherWindow()
        return app

if __name__ == "__main__" :
    WeatherApp().run() 