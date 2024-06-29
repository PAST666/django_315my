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
    context = {"message": category_str}
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return render(request, "python_blog/test_template.html", context=context)


def main(request):
    return render(request, "main.html")


class Developer:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

    def __str__(self):
        return f"{self.name} - {self.stack}"

    def get_rus_info(self):
        return f"Разработчик {self.name} - {self.stack}"


about_data = {
    "title": "О нас",
    "text": "Мы - команда разработчиков, которая создает сайты на Django и Flask.",
    "stack_list": ["Python", "Django", "Flask"],
    "developers": [
        {"name": "Иван", "age": 25, "stack": ["Python", "Django"]},
        {"name": "Анна", "age": 23, "stack": ["Python", "Flask"]},
        {"name": "Петр", "age": 30, "stack": ["JS", "React", "Vue"]},
    ],
}


def category(request):
    return HttpResponse(
        """<ul><li>Python</li><li>Django</li><li>Flask</li></ul>
        <a href="/">На главную</a>
        """
    )


def about(request):
    return render(request, "python_blog/about.html", about_data)


# Create your views here.
