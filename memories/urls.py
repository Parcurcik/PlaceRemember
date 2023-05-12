from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('add_memory/', views.create_memory, name='create_memory'),
    path('delete_memory/<int:memory_id>/', views.delete_memory, name='delete_memory'),
    path('logout/', views.logout, name='logout'),

]
