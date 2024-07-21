from django.shortcuts import render
from django.http import HttpRequest
from .models import Post
from django.shortcuts import get_object_or_404

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

def about(request):
    context={
        "users_count": USERS_COUNT,
        "menu":menu,
        "page_alias": "about",
    }
    return render(request, 'python_blog/about.html', context)

def blog(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {
            "menu": menu,
            "posts": posts,
            "page_alias": "blog",
        }
        return render(request, "python_blog/blog.html", context)

def main(request):
    
    context={
        "menu":menu,
        "page_alias": "main",
        "users_count": USERS_COUNT,
        # "posts": posts,
    }
    return render(request, "main.html", context)

def post_detail(request, slug):
    get_object_or_404(Post, slug=slug)
    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog",
    }
    return render(request, "python_blog/post_detail.html", context)