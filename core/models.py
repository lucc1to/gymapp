from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:  # szablon do dziedziczenia, nie rób tabeli
        abstract = True
