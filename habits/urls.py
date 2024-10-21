from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, PublicHabitsListAPIView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"habits", HabitsViewSet, basename="habits")

urlpatterns = [
    path("habits/public/", PublicHabitsListAPIView.as_view(), name="public_habits_list")
] + router.urls
