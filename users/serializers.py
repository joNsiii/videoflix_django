from rest_framework import serializers
from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'infos', 'address', 'phone', 'id']
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user
        