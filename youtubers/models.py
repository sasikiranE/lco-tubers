from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    CREW_SMALL = 'small'
    CREW_SOLO = 'solo'
    CREW_LARGE = 'large'

    CREW_CHOICES = (
        (CREW_SMALL, 'SMALL'),
        (CREW_SOLO, 'SOLO'),
        (CREW_LARGE, 'LARGE'),
    )

    CAMERA_CANNON = 'cannon'
    CAMERA_PANASONIC = 'panasonic'
    CAMERA_HASSELBLAD = 'hasselblad'
    CAMERA_RED = 'red'
    CAMERA_NIKON = 'nikon'
    CAMERA_OTHER = 'other'

    CAMERA_CHOICES = (
        (CAMERA_PANASONIC, 'PANASONIC'),
        (CAMERA_CANNON, 'CANNON'),
        (CAMERA_HASSELBLAD, 'HASSELBLAD'),
        (CAMERA_RED, 'RED'),
        (CAMERA_NIKON, 'NIKON'),
        (CAMERA_OTHER, 'OTHER')
    )

    CATEGORY_VLOGGING = 'vlogging'
    CATEGORY_COOKING = 'cooking'
    CATEGORY_GAMING = 'gaming'
    CATEGORY_FILM_MAKING = 'film making'
    CATEGORY_OTHER = 'other'

    CATEGORY_CHOICES = (
        (CATEGORY_COOKING, 'COOKING'),
        (CATEGORY_GAMING, 'GAMING'),
        (CATEGORY_FILM_MAKING, 'VLOGGING'),
        (CATEGORY_FILM_MAKING, 'FILM MAKING'),
        (CATEGORY_OTHER, 'OTHER'),
    )

    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=200)
    height = models.FloatField()
    subs_count = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    photo_link = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    description = RichTextField()
    crew = models.CharField(max_length=20, choices=CREW_CHOICES)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    camera_type = models.CharField(max_length=50, choices=CAMERA_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'