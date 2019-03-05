from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/',views.new, name = "new"),
    path('creat/',views.create, name = "create"),
    path('newblog/',views.blogpost, name="newblog"),

]