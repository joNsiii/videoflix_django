from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import VideoSerializer
from .models import Video
from rest_framework import status

# Create your views here.
class VideosViews(APIView):
    
    def get(self, request):
        if request.method == 'GET':
            videos = Video.objects.all()
            serializer = VideoSerializer(videos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
