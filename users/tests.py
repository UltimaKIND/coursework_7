from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="user@sky.pro", telegram_id="0123456789", password="123456"
        )
        self.admin_user = User.objects.create(
            email="admin@sky.pro",
            telegram_id="123456789",
            password="123456",
            is_superuser=True,
            is_active=True,
            is_staff=True,
        )

    def test_create_user(self):
        data = {
            "email": "user2@sky.pro",
            "telegram_id": "0123456780",
            "password": "123456",
        }
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/users/{self.user.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f"/users/{self.user.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
