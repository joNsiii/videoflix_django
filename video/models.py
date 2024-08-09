import datetime
from platform import release
from sqlite3 import Date
from time import timezone
from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=750, blank=True)
    released_at = models.DateTimeField(datetime.datetime)
    file = models.FileField(upload_to='/videos/', blank=True, null=True)