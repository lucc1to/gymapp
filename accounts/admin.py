from django.contrib import admin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "height_cm", "default_rest_seconds"]
