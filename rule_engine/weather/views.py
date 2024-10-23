from django.shortcuts import render
from .models import WeatherData, DailyWeatherSummary
import logging
import requests  # Import requests to fetch data from OpenWeatherMap API

logger = logging.getLogger(__name__)

def fetch_weather_data(city):
    # Replace with your actual OpenWeatherMap API key
    api_key = 'ee0f229cfecf6497681fa362ee4a82a2'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to fetch weather data for {city}: {response.status_code} {response.text}")
        return None

def weather_summary(request):
    temperature_threshold = None  # Default threshold to None
    selected_city = None  # Track the selected city
    summaries = []

    if request.method == 'POST':
        selected_city = request.POST.get('city')  # Get selected city
        temperature_threshold = request.POST.get('threshold')  # Get temperature threshold input

        if selected_city:
            # Fetch weather data and save to the model
            weather_data = fetch_weather_data(selected_city)
            if weather_data:
                icon = weather_data['weather'][0]['icon']  # Get icon directly
                DailyWeatherSummary.objects.update_or_create(
                    city=selected_city,
                    defaults={
                        'avg_temperature': weather_data['main']['temp'],
                        'max_temperature': weather_data['main']['temp_max'],
                        'min_temperature': weather_data['main']['temp_min'],
                        'dominant_condition': weather_data['weather'][0]['description'],
                        'icon': icon  # Save the icon directly
                    }
                )
                summaries = DailyWeatherSummary.objects.filter(city=selected_city)
        else:
            summaries = DailyWeatherSummary.objects.all()  # Show all if no city is selected
    else:
        summaries = DailyWeatherSummary.objects.all()

    # Apply the threshold logic if the user provided a threshold
    if temperature_threshold:
        try:
            temperature_threshold = float(temperature_threshold)
            for summary in summaries:
                summary.threshold_exceeded = summary.avg_temperature > temperature_threshold  # Mark if threshold exceeded
        except ValueError:
            logger.warning("Invalid temperature threshold input.")

    # Construct the icon URL for OpenWeather icons
    for summary in summaries:
        if summary.icon:  # Ensure there's a valid icon
            summary.icon_url = f"http://openweathermap.org/img/wn/{summary.icon}@2x.png"  # Using @2x for better quality
        else:
            summary.icon_url = None  # Set to None if there's no icon available

    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]  # List of cities for dropdown
    return render(request, 'summary.html', {
        'summaries': summaries,
        'cities': cities,
        'temperature_threshold': temperature_threshold,
        'selected_city': selected_city  # Pass the selected city back to the template
    })

def recent_weather(request):
    # Retrieve the most recent weather data
    recent_data = WeatherData.objects.all().order_by('-timestamp')[:10]
    # Construct the icon URL for each recent data entry
    for data in recent_data:
        if data.icon:  # Ensure there's a valid icon
            data.icon_url = f"http://openweathermap.org/img/wn/{data.icon}@2x.png"  # Using @2x for better quality
        else:
            data.icon_url = None  # Set to None if there's no icon available

    return render(request, 'recent.html', {'recent_data': recent_data})
