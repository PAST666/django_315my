from urllib import request
from django.shortcuts import render

from django.http import Http404, HttpResponse

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}


def category_detail(request, category_id):
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return HttpResponse(f"<h1>{category_str}</h1><a href='/blog/category/'>Назад</a>")


def index(request):
    return HttpResponse(
        """<h1>Мой блог!</h1>
        <a href="/blog/category/">Категории</a>
        """
    )


def category(request):
    return HttpResponse(
        """<ul><li>Python</li><li>Django</li><li>Flask</li></ul>
        <a href="/">На главную</a>
        """
    )


# Create your views here.
