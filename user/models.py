from django.db import models

from location.models import Location


class User(models.Model):
    ROLES = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLES, default="member")
    age = models.SmallIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # ordering = ['username']

    def __str__(self):
        return self.username
