# Generated by Django 5.1.2 on 2024-10-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWeatherSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('avg_temperature', models.FloatField()),
                ('max_temperature', models.FloatField()),
                ('min_temperature', models.FloatField()),
                ('dominant_condition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('condition', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]