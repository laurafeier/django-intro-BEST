from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    if request.user.is_authenticated():
        all_posts = Post.objects.all()
    else:
        all_posts = Post.objects.filter(published_date__lte=timezone.now())

    all_posts = all_posts.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': all_posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})