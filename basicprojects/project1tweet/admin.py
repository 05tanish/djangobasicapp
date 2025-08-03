from django.contrib import admin

# Register your models here.
from .models import Tweet  # ✅ Capital "T"



admin.site.register(Tweet)