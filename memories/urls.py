from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('vk_callback/', views.vk_callback, name='vk_callback'),
    path('google_callback/', views.google_callback, name='google_callback'),
    path('logout/', views.logout, name='logout'),

]


