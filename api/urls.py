from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.api_list, name="api_list"),
    path("ques", views.ques_list, name="ques_list"),
    path("ques/<int:pk>", views.quesDetail, name="quesDetail"),
    path("create", views.quesCreate, name="quesCreate"),
]
