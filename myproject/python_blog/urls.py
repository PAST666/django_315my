from django.contrib import admin
from django.urls import path, include
from python_blog import views

urlpatterns = [
    path('', admin.site.urls),
    path('category/', views.category),
    path("category/<int:category_id>/", views.category_detail),
]