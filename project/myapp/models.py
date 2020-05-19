from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    name = models.TextField(max_length=30)
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name