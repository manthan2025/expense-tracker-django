from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'}),
        input_formats=['%d-%m-%Y', '%Y-%m-%d'],
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username','name', 'phone_number', 'date_of_birth', 'profile_picture')

class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'name', 'phone_number', 'date_of_birth', 'profile_picture')