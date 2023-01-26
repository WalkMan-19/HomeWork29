from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
