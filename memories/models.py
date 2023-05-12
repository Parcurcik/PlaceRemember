from django.db import models
from django.contrib.auth.models import User

class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memory_name = models.CharField(max_length=100)
    memory_comment = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

