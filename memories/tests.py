import os
from django.test import TestCase, Client
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from .models import Memory
from .views import create_memory, home, delete_memory

access_token = os.getenv("ACCESS_TOKEN")


class MemoryTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test_user1", password="test_password")

        UserSocialAuth.objects.create(
            user=self.user,
            provider='vk-oauth2',
            uid='111111111',
            extra_data={"access_token": access_token}
        )

    def test_create_memory(self):
        self.client.force_login(self.user)
        response = self.client.post("/add_memory/", {
            "memory_name": "Test Memory",
            "memory_comment": "Test Comment1",
            "latitude": "56",
            "longitude": "60",
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Memory.objects.count(), 1)

    def test_memory_list_display(self):
        memory1 = Memory.objects.create(memory_name="memory_1", memory_comment="comment_1", latitude="56",
                                        longitude="60", user=self.user)
        memory2 = Memory.objects.create(memory_name="memory_2", memory_comment="comment_2", latitude="57",
                                        longitude="61", user=self.user)

        self.client.force_login(self.user)

        response = self.client.get("/home/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, memory1.memory_name)
        self.assertContains(response, memory1.memory_comment)
        self.assertContains(response, memory2.memory_name)
        self.assertContains(response, memory2.memory_comment)

    def test_delete_memory(self):
        memory = Memory.objects.create(memory_name="memory_for_delete", memory_comment="comment", latitude="56",
                                       longitude="60", user=self.user)

        self.client.force_login(self.user)

        response = self.client.post(f"/delete_memory/{memory.id}/")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Memory.objects.count(), 0)
