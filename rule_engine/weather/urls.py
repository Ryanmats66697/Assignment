from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_summary, name='weather_summary'),
    path('recent/', views.recent_weather, name='recent_weather'),
]
