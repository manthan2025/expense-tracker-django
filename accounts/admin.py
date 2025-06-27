from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'profile_picture')}),
    )
    list_display = ['email', 'username','name', 'phone_number', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)