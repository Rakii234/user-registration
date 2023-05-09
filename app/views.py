from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import random


# Create your views here.
from app.forms import *
def Registration(request):
    d={'uso':UserForm(), 'pso':ProfileForm()}
    if request.method=='POST' and request.FILES:
        usd=UserForm(request.POST)
        psd=ProfileForm(request.POST,request.FILES)
        if usd.is_valid() and psd.is_valid():
            nusd=usd.save(commit=False)
            nusd.set_password(usd.cleaned_data['password'])
            nusd.save()

            npsd=psd.save(commit=False)
            npsd.username=nusd   
            npsd.save()

            send_mail('Insert A Data',
                      'Registration is Done',
                      'rakeshgangaraju.234@gmail.com',
                      [nusd.email],
                      fail_silently=False)
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('DATA IS INVALID')
        
    return render(request,'Registration.html',d)

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username, password=password)

        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Username/Password')
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def dp(request):
    un=request.session['username']
    print(un)
    uno=User.objects.get(username=un)
    po=Profile.objects.get(username=uno)
    d={'uno':uno, 'po':po}
    return render(request,'dp.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        un=request.session['username']
        uno=User.objects.get(username=un)
        uno.set_password(pw)
        uno.save()
        return HttpResponse('Password Changed Successfully')
    return render(request,'change_password.html')

def forget_password(request):
    if request.method=='POST':
        email=request.POST['email']
        uno=User.objects.get(email=email)
        rn = random.randint(0, 999999)
        x = str(rn).zfill(6)
        send_mail('OTP GENERATED',
                      x,
                      'rakeshgangaraju.234@gmail.com',
                      [uno.email],
                      fail_silently=False)
        return HttpResponse('OTP sent successfully')
    return render(request,'forget_password.html')
    
