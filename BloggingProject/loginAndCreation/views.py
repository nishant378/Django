from django.shortcuts import render




# Create your views here.
from loginAndCreation.models import Login

def index(request):
    return render(request,"login.html")


def create(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        lg=Login(username=username,password=password)
        lg.save()
    return render(request,"Create.html")







