from django.contrib import admin
from .models import Rule
from .models import UserProfile

# Register your models here.
admin.site.register(Rule)
admin.site.register(UserProfile)