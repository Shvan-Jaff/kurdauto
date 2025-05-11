# cars/views.py
from .models import Car  # This now imports our simple Python class
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission (you can print to console)
        print(request.POST)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def cars(request):
    # Debug code - remove after use
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        print("Existing tables:", cursor.fetchall())
    
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})