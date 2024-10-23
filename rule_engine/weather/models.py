from django.db import models
from django.utils import timezone


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='01d')  # Set a default value here
    timestamp = models.DateTimeField(default=timezone.now)  # Store in UTC

    class Meta:
        ordering = ['-timestamp']  # Order by latest timestamp first

    def __str__(self):
        return f"{self.city} - {self.temperature}°C - {self.condition}"


class DailyWeatherSummary(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=100)
    avg_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    dominant_condition = models.CharField(max_length=50)
    icon = models.CharField(max_length=10, null=True, blank=True)  # Changed icon_id to icon for consistency

    def __str__(self):
        return f"{self.date} - {self.city}"
