
#Django
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render,redirect # se dejan de usar por que seimplento vistas con clases
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView 
from django.shortcuts import get_object_or_404

try:
    from django.utils import simplejson as json
except ImportError:
    import json
#forms
from posts.forms import CommentForm, PostForm

#models
from posts.models import Post,Comment

#utilities
from datetime import datetime 



class PostDetailView(LoginRequiredMixin,DetailView):
    """return a especified post published"""

    template_name = 'posts/detail.html'
    model = Post
    slug_field = 'id'
    slug_url_kwarg = 'id_post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comment.objects.filter(post= self.get_object()).order_by('-created')
        context['comments'] = comments        
        context['CommentForm'] = CommentForm(instance=self.request.user)
        return context

    def post(self,request,*args, **kwargs):
        new_comment =Comment(comment=request.POST.get('comment'),
                             user=self.request.user,
                             post= self.get_object())
        if new_comment.comment.__len__() >0:                             
            new_comment.save()
        return self.get(self,request,*args,**kwargs)
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
    
class LikePostView(LoginRequiredMixin,CreateView):
    def post(self,request,**kwargs):
        user = self.request.user
        post = get_object_or_404(Post,id=request.POST.get('id_post'))
        post_likes = get_object_or_404(Post,id=request.POST.get('id_post'))
        if post.like.filter(id=user.id).exists():
            #user has already liked this post
            #remove like/user
            post.like.remove(user)
            message ='0'
        else:
            #add a new like for post
            post.like.add(user)
            message = '1'        
        ctx = {'likes_count':post.total_likes,'like':message,'total_likes':post_likes.total_likes}
        #use minitype instead of content_type if django < 5
        return HttpResponse(json.dumps(ctx), content_type='application/json')