from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import NewPostForm
from .models import Tag, Stream, Follow, Post, Likes

def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    return render(request, 'index.html', {'post_items': post_items})



def newPost(request):
    user = request.user
    tags_objs = []

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tag')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            
            p, created = Post.objects.get_or_create(image=image, caption=caption, user_id=user.id)
            p.tag.set(tags_objs)
            p.save()

            return redirect('index')


    else:
        form = NewPostForm()
    
    return render(request, 'newpost.html', {'form': form})


def postDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'postdetail.html', {'post': post})


def tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tag=tag).order_by('-posted')


    return render(request, 'tags.html', {'posts': posts, 'tag': tag})


def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.likes = current_likes
    post.save()
    
    return HttpResponseRedirect(reverse('post-details', args=[post_id]))
