# Generated by Django 5.1.2 on 2024-10-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine_logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('income', models.FloatField()),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='rule',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='rule',
            name='rule_string',
            field=models.CharField(max_length=255),
        ),
    ]