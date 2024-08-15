from telnetlib import STATUS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from video import serializer


# Create your views here.

class RegisterView(APIView):
    
    def post(self, request):
        if request.method == 'POST':
            serializer = CustomUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginView(ObtainAuthToken):
    
   def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.pk,
            'email': user.email
        })