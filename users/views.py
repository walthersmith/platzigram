"""Users Views"""
#django
#from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
#from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post
from users.forms import SignupForm

#exceptions
from django.db.utils import IntegrityError

#forms
#from users.forms import ProfileForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail View"""

    template_name = 'users/details.html'
    slug_field = 'username'
    slug_url_kwarg= 'username' # se tiene que llamar igual  en urls.py
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self,**kwargs):
        """Add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    """Users sign up view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url =  reverse_lazy('users:login')

    def form_valid(self,form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin,UpdateView):
    """Update Profile  view"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website','biography','phone_number','picture']

    def get_object(self):
        """return user's profile"""
        return self.request.user.profile
        
    def get_success_url(self):
        """return to users profile"""
        username = self.object.user.username
        return reverse('users:detail',kwargs={'username':username})
   

class loginView(auth_views.LoginView):
    """Login View"""

    template_name = 'users/login.html'   


class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """ Logout View"""
    template_name = 'users/logged_out.html'   


