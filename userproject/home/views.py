from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate,login
#password for test user->Harry$$$***000

from django.contrib.auth import logout


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request):
    if request.method=="POST":
        user=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
             # A backend authenticated the credentials
             login(request,user)
             return redirect('/')
        else:
            # No backend authenticated the credentials
             return render(request,'login.html')
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")










