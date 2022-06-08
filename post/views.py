from django.shortcuts import render
from .models import Tag, Stream, Follow, Post
from django.contrib.auth.decorators import login_required


def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    return render(request, 'index.html', {'post_items': post_items})
