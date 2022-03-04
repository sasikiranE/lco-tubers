from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Slider(models.Model):
    headline = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/slider/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.headline}'
