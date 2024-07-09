from django.urls import path
from .views import blog, post_detail

urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>/', post_detail, name='post_detail')
]
