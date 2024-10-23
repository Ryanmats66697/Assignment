import requests
from datetime import datetime
from .models import WeatherData, DailyWeatherSummary
from django.utils import timezone
from django.db import models
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Your API key (keep this secure and consider moving to a config file or environment variable)
API_KEY = 'ee0f229cfecf6497681fa362ee4a82a2'
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
TEMP_THRESHOLD = 35

def fetch_weather():
    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"  # Use metric for Celsius
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            data = response.json()

            # Process the weather data
            temperature = data['main']['temp']  # Temperature in Celsius
            condition = data['weather'][0]['main']  # Main weather condition
            icon_id = data['weather'][0]['icon']  # Get the icon ID

            # Save weather data, including icon_id
            weather_data = WeatherData(city=city, temperature=temperature, condition=condition, icon_id=icon_id)
            weather_data.save()

            # Trigger alert if temperature exceeds threshold
            if temperature > TEMP_THRESHOLD:
                logger.warning(f"Alert! {city} has exceeded the temperature threshold: {temperature:.2f}°C")

            # Summarize daily data
            summarize_daily_weather(city)

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred for {city}: {http_err}")
        except Exception as err:
            logger.error(f"An error occurred for {city}: {err}")

def summarize_daily_weather(city):
    today = timezone.now().date()
    daily_data = WeatherData.objects.filter(city=city, timestamp__date=today)

    if daily_data.exists():
        avg_temp = daily_data.aggregate(models.Avg('temperature'))['temperature__avg']
        max_temp = daily_data.aggregate(models.Max('temperature'))['temperature__max']
        min_temp = daily_data.aggregate(models.Min('temperature'))['temperature__min']

        # Dominant weather condition
        dominant_condition_data = daily_data.values('condition').annotate(count=models.Count('condition')).order_by('-count').first()
        dominant_condition = dominant_condition_data['condition'] if dominant_condition_data else "N/A"

        # Create or update the daily summary
        DailyWeatherSummary.objects.update_or_create(
            date=today, city=city,
            defaults={
                'avg_temperature': avg_temp,
                'max_temperature': max_temp,
                'min_temperature': min_temp,
                'dominant_condition': dominant_condition
            }
        )
    else:
        logger.info(f"No weather data available for {city} on {today}.")
