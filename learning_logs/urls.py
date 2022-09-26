from django.urls import path
from . import views

app_name = 'learning_logs'  # application, which this url belongs to

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topic list page
    path('topics/', views.topics, name='topics'),
    # Topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # New topic adding page
    path('new_topic/', views.new_topic, name='new_topic'),
    # New entry adding page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Entry editing page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
