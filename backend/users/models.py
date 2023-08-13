from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class Users(AbstractUser):
    username = models.CharField(
        'Имя пользователя',
        max_length=30,
        validators=[UnicodeUsernameValidator],
        unique=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
