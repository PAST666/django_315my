from django.urls import path
from python_blog import views

urlpatterns = [
    path("category/", views.category, name="categories"),
    path("category/<int:category_id>/", views.category_detail, name="category"),
]
