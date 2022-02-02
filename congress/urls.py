from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('meetings/', views.meeting_list, name="meeting_list")
]