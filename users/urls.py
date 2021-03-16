"""Users Urls."""

# Django
from django.urls import path
#from django.views.generic import TemplateView

# views
from users import views

urlpatterns = [

    #management
    path(
        route ='login/',
        view = views.loginView.as_view(),
        name='login'
    ),
    path(
        route ='logout/',
        view = views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route ='signup/',
        view = views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route ='me/profile/', 
        view = views.UpdateProfileView.as_view(), 
        name='update'
    ),
    
    #Posts

    path(
        route='<str:username>/',
        view= views.UserDetailView.as_view(),
        name='detail'
    ),
    path(
        route='profile/follow/',
        view= views.FollowUserView.as_view(),
        name='follow' 
    ),
]
