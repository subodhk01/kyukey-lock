from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404

from .models import *
import datetime


def index(request):
    if request.user.is_authenticated:
        if request.is_ajax() and request.method == "POST":
            lock = Lock.objects.get(pk=1)
            pre_status = lock.status.lower()
            status = ""
            if pre_status == "unlocked" or pre_status == "open":
                status = 'u'
            elif pre_status == "locked" or pre_status == "closed":
                status = 'l'
            else:
                status = 'e'
            return JsonResponse({'status':status})
        otps = OTP.objects.all()
        return render(request, 'index.html', {'otps': otps})
    else:
        return redirect('login')

def remove_otp(request, otp_id):
    try:
        otp = OTP.objects.get(pk=otp_id)
        otp.delete()
        return redirect(index)
    except:
        return HttpResponse(status = 404)
    

def generate_otp(request):
    if request.method == "POST":
        validity = request.POST['validity']
        djvalidity = validity + ":00.000000+0530"
        print(djvalidity)
        otp = OTP(
            name = request.POST['name'],
            content = 1234,
            lock = Lock.objects.get(pk=1),
            valid_till = djvalidity
        )
        otp.save()
        return HttpResponse('ok')
    else:
        lowerLimit = datetime.datetime.now()
        return render(request, 'generate_otp.html', {'lowerLimit': lowerLimit})

def lock_history(request):
    history  = History.objects.all()
    return render(request, 'history.html', {'history' : history})

def user_login(request):
    """User login view."""
    if request.user.is_authenticated :
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', { 'msg': "Invalid Credentials" })
    else:
        return render(request, 'login.html')

def user_logout(request):
    """User Logout view"""
    logout(request)
    return redirect('index')