from django.db import models

from ads.models import Ad
from user.models import User


class Selection(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    items = models.ManyToManyField(Ad)

    class Meta:
        unique_together = ['name', 'owner']
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
