from dataclasses import fields
from django.contrib import admin
from .forms import CustomUserCreationForms
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForms
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Infos',
            {
                'fields': (
                    'infos',
                    'address',
                    'phone',
                )
            }
        )
    )