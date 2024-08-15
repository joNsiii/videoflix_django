import datetime
from platform import release
from sqlite3 import Date
from time import timezone
from xmlrpc.client import DateTime
from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Video(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('science_fiction', 'Science Fiction'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('animation', 'Animation'),
        ('documentary', 'Documentary'),
        ('fantasy', 'Fantasy'),
        ('unknown', 'Unknown')
    ]

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=750, blank=True)
    released_at = models.DateField(blank=True)
    file = models.FileField(upload_to='videos', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='unknown')

    def __str__(self):
        return self.title