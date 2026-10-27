from django.db import models
from django.conf import settings

from core.models import TimeStampedModel


# Create your models here.
class Profile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )  # jeden uzytkownik ma dokladnie 1 profil
    height_cm = models.PositiveSmallIntegerField(null=True, blank=True)
    default_rest_seconds = models.PositiveSmallIntegerField(default=90)

    def __str__(self):
        return self.user.username
