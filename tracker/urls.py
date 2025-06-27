from django.contrib import admin
from django.urls import path ,include
from .views import home,expense_dashboard

urlpatterns = [
    path('',home, name='home'),  # Assuming you have a home view in tracker/views.py
    # path('admin/', admin.site.urls),
    path('dashboard/', expense_dashboard, name='expense_dashboard'),
]