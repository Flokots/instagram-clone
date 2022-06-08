from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from .forms import NewPostForm
from .models import Tag, Stream, Follow, Post

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
            image = form.cleaned_data('image')
            caption = form.cleaned_data('caption')
            tag_form = form.cleaned_data('tag')
            tags_list = list(tag_form.spli(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            
            p, created = Post.objects.get_or_create(image=image, caption=caption, user_id=user)
            p.tags_list.set(tags_objs)
            p.save()

            return redirect('index')


    else:
        form = NewPostForm()
    
    return render(request, 'newpost.html', {'form': form})

