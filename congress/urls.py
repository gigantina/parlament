from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('meetings/', views.meeting_list, name="meeting_list"),
    path('meetings/<str:date>/', views.meeting_detail, name="meeting_detail"),
    path('votings/', views.voting_list, name="voting_list"),
    path('votings/<str:title>/', views.voting_detail, name="voting_detail")
]