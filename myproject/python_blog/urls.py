from django.urls import path
from .views import blog, post_detail, category_detail, tag_list

urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('tag/<slug:slug>/', tag_list, name='tag_list'),
]
