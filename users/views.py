"""Users Views"""
#django
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
            return redirect('feed') #feed es el nombre de la url en urls.py
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})     

    return render(request,'users/login.html')

@login_required
def logout_view(request):
    """Logout View"""
    logout(request)
    return redirect('login') 
