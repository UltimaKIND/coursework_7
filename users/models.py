from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    first_name = models.CharField(
        max_length=50, verbose_name="Имя пользователя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Фамилия пользователя", **NULLABLE
    )
    telegram_id = models.PositiveIntegerField(
        verbose_name="id чата телеграмм", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
