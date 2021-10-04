from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('api/', views.QuestionsAPI.as_view()),
    path('', views.root),
]