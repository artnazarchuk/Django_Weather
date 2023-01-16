from django.shortcuts import render
import requests

def index(request):
    appid = '949343008822928ceceaa147a4fd4750'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Mozyr'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)

def about(request):
    return render(request, 'weather/about.html')
