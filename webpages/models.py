from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Slider(models.Model):
    headline = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=20)
    photo_link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.headline}'


class Team(models.Model):

    ROLE_CHOICES  = (
        ('CEO', 'CEO'),
        ('FRONTEND', 'frontend'),
        ('BACKEND', 'backend'),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)
    fb_link = models.CharField(max_length=200, null=True, blank=True)
    photo_link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'