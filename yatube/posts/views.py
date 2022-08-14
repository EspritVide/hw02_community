
from django.shortcuts import get_object_or_404, render

from .models import Group, Post
from .constants import QUANT_POSTS


def index(request):
    posts = Post.objects.select_related('group')[:QUANT_POSTS]
    text = 'Главная страница'
    context = {
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:QUANT_POSTS]
    text = 'Страница группы'
    context = {
        'group': group,
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/group_list.html', context)
