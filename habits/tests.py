from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="user@sky.pro", telegram_id="0123456789", password="123456"
        )
        self.habit = Habit.objects.create(
            id=100,
            user=self.user,
            place="bars",
            time="12:00",
            action="push-ups",
            reward="chocolate",
            period=1,
            is_published=False,
            time_to_action="120",
        )

    def test_get_list_habits(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        data = {"title": "test", "place": "home", "action": "drink water"}
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/habits/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_habit(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/habits/100/")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_list_public_habits(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/habits/public/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
