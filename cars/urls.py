from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('cars/', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]