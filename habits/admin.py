from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """
    регистрация модели Habit в панели администратора
    """

    list_display = (
        "id",
        "title",
        "is_pleasant",
        "related_habit",
        "reward",
    )
    list_filter = ("is_pleasant",)
    search_fields = ("title",)
