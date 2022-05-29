from django.urls import path
from . import views

app_name = 'learning_logs' # название приложения, к которому принадлежит данный urls

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по каждой теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]