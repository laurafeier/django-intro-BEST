from django.shortcuts import render
from .models import Post


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': all_posts})
