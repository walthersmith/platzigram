
#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

#forms
from posts.forms import PostForm

#models
from posts.models import Post

#utilities
from datetime import datetime



class PostDetailView(LoginRequiredMixin,DetailView):
    """return a especified post published"""

    template_name = 'posts/detail.html'
    model = Post
    slug_field = 'id'
    slug_url_kwarg = 'id_post'
    queryset = Post.objects.all()

class PostsFeedView(LoginRequiredMixin,ListView):
    """return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'

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
            return redirect('posts:feed')
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