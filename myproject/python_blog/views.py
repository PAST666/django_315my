from turtle import update
from django.shortcuts import render
from django.http import Http404
from django.http import HttpRequest
from django.template import context
from django.test import tag
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}

USERS_COUNT = 10

menu = [
    {
        "name":"Главная",
        "alias":"main",
    },
        {
        "name":"Блог",
        "alias":"blog",
    },
        {
        "name":"О проекте",
        "alias":"about",
    }
]

def main(request):
    posts = Post.objects.all()
    context={
        "menu":menu,
        "page_alias": "main",
        "users_count": USERS_COUNT,
        "posts": posts,
    }

    return render(request, "main.html", context)

def about(request):
    context={
        "users_count": USERS_COUNT,
        "menu":menu,
        "page_alias": "about",
    }
    return render(request, 'python_blog/about.html', context)

def blog(request):
    """
    Вьюшка для страницы "Блог" с каталогом постов.
    Обрабатываем поисковую форму, которая обрабатывается методом GET
    И пробуем получить от туда ключи:
        search
        searchInTitle
        searchInText
        searchInTags
    """
    
    if request.method == "GET":
        posts = Post.objects.all()

                
    
        context = {
            "menu": menu,
            "posts": posts,
            "page_alias": "blog",
        }
        return render(request, "python_blog/blog.html", context)

def post_detail(request, slug):
    post: Post = get_object_or_404(Post, slug=slug)
    post.views = F('views') + 1
    post.save(update_fields=['views'])

    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog",
    }
    if 'viewed_posts' not in request.session:
    request.session['viewed_posts'] = ['osnovy-python', 'osnovy-django', 'osnovy-django-2']
    
    
    
    if slug not in request.session['viewed_posts']:
        post.views = F('views') + 1
        post.save(update_fields=['views'])
        request.session['viewed_posts'].append(slug)
    
    # Отображаем пост
    return render(request, 'blog/post_detail.html', context)


def category_detail(request: HttpRequest, slug: str):
    posts = posts = Post.objects.filter(category__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog_catalog",
    }
    return render(request, "python_blog/blog.html", context)

def tag_detail(request: HttpRequest, slug: str):
    posts = Post.objects.filter(tags__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog",
        "tag": tag
    }

    return render(request, "python_blog/blog.html", context)


