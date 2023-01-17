from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '949343008822928ceceaa147a4fd4750'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = CityForm()

    city_one = request.POST.get('name')
    res = requests.get(url.format(city_one)).json()
    if res['cod'] != '404':
        city_one_info = {
            'city': city_one,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
    else:
        city_one_info = None

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res['cod'] != '404':
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
            }
            all_cities.append(city_info)
        else:
            City.objects.filter(name=city).delete()

    context = {
        'all_info': all_cities,
        'form': form,
        'city_one': city_one_info,
    }

    return render(request, 'weather/index.html', context)

def about(request):
    return render(request, 'weather/about.html')
