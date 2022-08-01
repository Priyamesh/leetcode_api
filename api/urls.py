from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginpage, name="login"),
    path("logout", views.logoutpage, name="logout"),
    path("register", views.registerpage, name="register"),
    path("api/", views.api_endpoints, name="api_list"),
    path("api/ques", views.ques_list, name="ques_list"),
    path("api/ques/<int:pk>", views.quesDetail, name="quesDetail"),
    path("api/create", views.quesCreate, name="quesCreate"),
    path("api/update/<int:pk>", views.quesUpdate, name="quesUpdate"),
]
