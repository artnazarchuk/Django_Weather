from django.shortcuts import render
import requests

def index(request):
    appid = '949343008822928ceceaa147a4fd4750'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Minsk'
    res = requests.get(url.format(city)).json()
    print(res)
    return render(request, 'weather/index.html')

def about(request):
    return render(request, 'weather/about.html')
