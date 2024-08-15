from os import path, remove
import os
from django.dispatch import receiver

from video.tasks import convert_to_480p
from .models import Video
from django.db.models.signals import post_save, post_delete

@receiver(post_save, sender=Video)
def video_post_save(sender , instance, created, **kwargs):
    if created:
        print('Video was uploaded')
        if path.isfile(instance.file.path):
            convert_to_480p(instance.file.path)
        
        
@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, **kwargs):
        if path.isfile(instance.file.path):
            remove(instance.file.path)
