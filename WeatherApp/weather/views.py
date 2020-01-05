from django.shortcuts import render
import requests

def index(request):
    appid = 'beacd1985713b0ffb5f4dd505fd76f61'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Moscow'

    response = requests.get(url.format(city)).json()
    print(response)
    city_info = {
    "city" : city,
    "temp" : response["main"]["temp"],
    "icon": response["weather"][0]["icon"]
    }
    context = {'info' : city_info}
    return render(request,'weather/index.html', context)
