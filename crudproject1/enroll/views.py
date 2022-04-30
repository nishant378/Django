from django.http import HttpResponse
from django.shortcuts import render,HttpResponsePermanentRedirect,redirect

# Create your views here.
from enroll.models import User

from enroll.forms import StudentRegistration

from django.contrib import messages
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stu=User.objects.all()
    return render(request,"enroll/AddandShow.html",{'form':fm,'stu':stu})

def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your data has sucessfully been updated!')
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updateStudent.html',{'form':fm})


def delete_data(request,id):
    if request.method=='GET':
        pi=User.objects.get(pk=id)
        pi.delete()
        return redirect('/')
    else:
        return HttpResponse("Wrong Http Request")







    

 
