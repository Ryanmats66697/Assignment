# Generated by Django 5.1.2 on 2024-10-23 08:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='icon',
            field=models.CharField(default='01d', max_length=10),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='condition',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
