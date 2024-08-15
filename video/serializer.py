from rest_framework import serializers
from video.models import Video


class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'released_at', 'category', 'file']
        
        
