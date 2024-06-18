from urllib import request
from django.shortcuts import render

from django.http import HttpResponse

CATEGORIES = {1: "Python", 2: "Django", 3: "Flask"}


def category_detail(request, category_id):
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    return HttpResponse(f"<h1>{category_str}</h1><a href='/category/'>Назад</a>")


def index(request):
    return HttpResponse(
        """<h1>Мой блог!</h1>
        <a href="/category/">Категории</a>
        """
    )


def category(request):
    return HttpResponse(
        """<ul><li>Python</li><li>Django</li><li>Flask</li></ul>
        <a href="/">На главную</a>
        """
    )


# Create your views here.
