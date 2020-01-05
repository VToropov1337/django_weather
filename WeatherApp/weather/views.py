from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = 'beacd1985713b0ffb5f4dd505fd76f61'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        try:
            form = CityForm(request.POST)
            form.save()
        except Exception:
            pass
            
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        response = requests.get(url.format(city)).json()
        city_info = {
        "city" : city.name,
        "temp" : response["main"]["temp"],
        "icon": response["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    
    context = {'all_info' : all_cities, 'form' : form}
    return render(request,'weather/index.html', context)
