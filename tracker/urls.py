from django.contrib import admin
from django.urls import path
from .views import home

urlpatterns = [
    path('',home, name='home'),  # Assuming you have a home view in tracker/views.py
    path('admin/', admin.site.urls),
]