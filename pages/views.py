from django.shortcuts import render

def index(request):
    return render(request, '../templates/home.html')

def about(request):
    return render(request, '../templates/about.html')