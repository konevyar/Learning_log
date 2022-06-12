"""Схема URL для пользователей"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Turning on URL authorization by default (build-in Django view)
    path('', include('django.contrib.auth.urls')),
    # User registration page
    path('register/', views.register, name='register'),
]
