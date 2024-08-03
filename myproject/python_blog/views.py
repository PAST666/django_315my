from django.shortcuts import render
from django.http import HttpRequest
from django.test import tag
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F, Q

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
    
    if request.method == "GET":
        posts = Post.objects.prefetch_related("tags","category").all().order_by("-published_date")
        search = request.GET.get("search")
        if search:
            search_in_title = request.GET.get("search_in_title")
            search_in_text = request.GET.get("search_in_text")
            search_in_tags = request.GET.get("search_in_tags")

            query = Q()
            if search_in_title:
                query|=Q(title__icontains=search)
            if search_in_text:
                query|=Q(text__icontains=search)
            if search_in_tags:
                query|=Q(tags__name__icontains=search)
            if not search_in_title and not search_in_text and not search_in_tags:
                query=Q(text__icontains=search)
            posts = posts.filter(query)

                
    
        context = {
            "menu": menu,
            "posts": posts,
            "page_alias": "blog",
        }
        return render(request, "python_blog/blog.html", context)

def post_detail(request, slug):
    post =Post.objects.prefetch_related("tags","category").get(slug=slug)
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
        request.session.modified = True
    
    # Отображаем пост
    return render(request, 'python_blog/post_detail.html', context)


def category_detail(request: HttpRequest, slug: str):
    posts = posts = Post.objects.filter(category__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog",
    }
    return render(request, "python_blog/blog.html", context)

def tag_list(request: HttpRequest, slug: str):
    posts = Post.objects.prefetch_related("tags", "category").filter(tags__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog",
        "tag": tag
    }
    return render(request, "python_blog/blog.html", context)


