from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')

def about(request):
    return render(request, 'weather/about.html')
