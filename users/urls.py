"""Схема URL для пользователей"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Включение URL авторизации по умолчанию (встроенное в Django представление)
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации пользователя
    path('register/', views.register, name='register'),
]
