"""Users Views"""
#django
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Models
from django.contrib.auth.models import User
from users.models import Profile

#exceptions
from django.db.utils import IntegrityError

#forms
from users.forms import ProfileForm

@login_required
def update_profile(request):
    """Update a user's profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form,
        }
    )

def login_view(request):
    """Login View"""
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        print('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        print(username,':',password)
        print('*' * 10)   

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('posts:feed') #feed es el nombre de la url en urls.py
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})     

    return render(request,'users/login.html')


def signup(request):
    """signup view"""
    #import pdb; pdb.set_trace() #debugger 
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request,'users/signup.html',{'error':'password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username,password=password)
        except IntegrityError :
            return render(request,'users/signup.html',{'error':'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save() #guardamos el objeto usuario

        profile = Profile(user=user) #se crea  perfil al usuario
        profile.save() #guardamos el objeto perfil

        return redirect('login')


    return render(request,'users/signup.html')


@login_required
def logout_view(request):
    """Logout View"""
    logout(request)
    return redirect('login') 



