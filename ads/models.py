from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from category.models import Category
from user.models import User


class Ad(models.Model):
    name = models.CharField(max_length=150, null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ad')
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=500, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
