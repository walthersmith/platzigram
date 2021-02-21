
#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

#forms
from posts.forms import PostForm

#models
from posts.models import Post

#utilities
from datetime import datetime



@login_required
def list_post(request):
    posts = Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html',{'posts':posts})

"""
    https://docs.djangoproject.com/en/2.0/ref/templates/builtins/
"""

@login_required
def create_post(request):
    """Create  new post view"""

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request=request,
        template_name= 'posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )