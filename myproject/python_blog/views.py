from django.shortcuts import render
from django.http import Http404
from django.http import HttpRequest
from django.template import context
from .models import Post
from django.shortcuts import get_object_or_404

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



def category_detail(request, category_id):
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    context = {"message": category_str}
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return render(request, "python_blog/test_template.html", context=context)


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

    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog",
    }
    return render(request, "python_blog/post_detail.html", context)

def tag_detail(request: HttpRequest, slug: str):
    """
    Функция - представление для страницы тега
    Принимает объект запроса HttpRequest и slug тега
    Отображает список статей с соответствующим slug

    Как это было бы на SQL (многие ко многим)

    SELECT * FROM post WHERE id IN (
        SELECT post_id FROM post_tags WHERE tag_id = (
            SELECT id FROM tag WHERE slug = slug
        )
    )
    """
    posts = Post.objects.filter(tags__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog",
    }

    return render(request, "python_blog/blog.html", context)


