from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=150)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name
