from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

from users.models import User

# константа для полей с возможно нулевыми значениями
NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    title = models.CharField(max_length=200, verbose_name="Привычка")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель", **NULLABLE
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(
        verbose_name="Время выполнения привычки", default=datetime.now().time()
    )
    action = models.CharField(max_length=100, verbose_name="Действие")
    is_pleasant = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="habit",
        verbose_name="Связанная приятная привычка",
        **NULLABLE
    )
    period = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(7)],
        verbose_name="Периодичность привычки",
        default=1,
    )
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    time_to_action = models.DurationField(
        default=timezone.timedelta(seconds=120),
        verbose_name="Продолжительность выполнения привычки",
    )
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")
    next_date = models.DateField(
        verbose_name="дата следующего выполнения привычки",
        default=datetime.today().date(),
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.title
