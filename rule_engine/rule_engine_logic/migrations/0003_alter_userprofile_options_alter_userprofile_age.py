# Generated by Django 5.1.2 on 2024-10-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine_logic', '0002_userprofile_remove_rule_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
