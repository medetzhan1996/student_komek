from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Абстрактный модель пользователя
    """
    profession = models.CharField(max_length=180)
    is_confirmed = models.BooleanField(default=False)
