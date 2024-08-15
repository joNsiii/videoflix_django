from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForms(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'