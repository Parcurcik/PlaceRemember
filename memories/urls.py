from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    path('add_memory/', views.create_memory, name='create_memory'),
    path('delete_memory/<int:memory_id>/', views.delete_memory, name='delete_memory'),
    path('logout/', views.logout, name='logout'),

]
