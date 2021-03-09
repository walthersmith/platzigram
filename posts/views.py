
#Django
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render,redirect # se dejan de usar por que seimplento vistas con clases
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

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
    paginate_by = 30
    context_object_name = 'posts'

"""
    https://docs.djangoproject.com/en/2.0/ref/templates/builtins/
"""

class CreatePostView(LoginRequiredMixin,CreateView):
    """Create A new Post."""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self,**kwargs):
        """Add user and profile context."""
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context
        