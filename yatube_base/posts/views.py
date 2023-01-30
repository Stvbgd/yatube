from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# from django.template import loader

# Create your views here.


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request):
    return HttpResponse('Посты авторов тут')


# def group_posts_new(request, slug):
#     return HttpResponse('Та самая страница')