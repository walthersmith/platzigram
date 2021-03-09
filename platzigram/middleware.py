"""Platzigram Middleware"""
#Django
from django.shortcuts import redirect
from django.urls import reverse

class profileCompletionMiddleware:
    """Profile completion middleware
    
    ensure every user that is interacting with the platform
    have their profile picture and biography
    """

    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self,request):
        """ Code to be executed for each request before the vire is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        response = self.get_response(request)
        return response
