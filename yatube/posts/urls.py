# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_post),
    path('group/<slug:pk>/', views.group_posts)
]