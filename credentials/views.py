
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):

    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pwd=request.POST['password']
        cpwd=request.POST['cpassword']
        if pwd==cpwd:
           if User.objects.filter(username = username).exists():
               messages.info(request,"Username already taken")
               return redirect('register')
           elif User.objects.filter(email =email).exists():
               messages.info(request,'email already used')
               return redirect('register')
           else:
               user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pwd)
               user.save()
               return redirect('login')

        else:
           messages.info(request, "password does not match")
           return redirect('register')
    return render(request,"register.html")

