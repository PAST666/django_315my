from django.contrib import admin
from django.urls import path
from python_blog import views

urlpatterns = [
    path("", views.index),
    path("category/", views.category),
    path("category/<int:category_id>/", views.category_detail),
]
