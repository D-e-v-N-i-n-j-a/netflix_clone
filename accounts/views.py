from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.


def register(request):
    
    return render(request,'register.html')




def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
    
    
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')





