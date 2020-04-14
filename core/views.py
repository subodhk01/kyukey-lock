from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404

from .models import *
import datetime
from dateutil import tz



import math, random
def OTPgenerator():
    """Generates a random 4 digit OTP"""
    digits = ['1','2','3','4','5','6','7','8','9','0']
    OTP = []
    for i in range(4):
        OTP += digits[ math.floor(random.random() * 10) ]
    return "".join(OTP)

def index(request):
    if request.user.is_authenticated:
        if request.is_ajax() and request.method == "POST":
            try:
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
            except:
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
        diff = ( datetime.datetime.strptime(djvalidity, "%Y-%m-%d %H:%M:%S.%f%z") - datetime.datetime.now().replace(tzinfo=tz.gettz('Asia/Kolkata')) )
        print(diff.days)
        print(diff.seconds)
        if diff.seconds < 0 or diff.days < 0 :
            lowerLimit = datetime.datetime.now()
            lowerLimit = (str(lowerLimit)[0:16])
            return render(request, 'generate_otp.html', {'lowerLimit': lowerLimit, 'msg':'Enter a Valid DateTime'})
        print(djvalidity)
        try:
            lock = Lock.objects.get(pk=1)
        except:
            lowerLimit = datetime.datetime.now()
            lowerLimit = (str(lowerLimit)[0:16])
            return render(request, 'generate_otp.html', {'lowerLimit': lowerLimit, 'msg':'No Lock found, contact your Administrator'})
        otp = OTP(
            name = request.POST['name'],
            content = OTPgenerator(),
            lock = Lock.objects.get(pk=1),
            valid_till = djvalidity
        )
        otp.save()
        return redirect('generation_success', id = otp.id)
    else:
        lowerLimit = datetime.datetime.now()
        lowerLimit = (str(lowerLimit)[0:16])
        return render(request, 'generate_otp.html', {'lowerLimit': lowerLimit})

def generation_success(request, id):
    try:    
        otp = OTP.objects.get(pk=id)
        if otp.visibility == False:
            return redirect('index')
    except:
        return redirect('index')
    return render(request, 'generation_success.html', {'otp':otp, 'id':id})

def hide_otp(request):
    if request.is_ajax() and request.method == "POST":
        id = request.POST["id"]
        print(id , type(id))
        otp = OTP.objects.get(pk=id)
        otp.visibility = False
        otp.save()
        return HttpResponse('success')
    else:
        redirect('index')

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


########## APIs ###########

def opt_validation(request, otp):
    otps = OTP.objects.all()
    for item in otps:
        if item.time_remaining != "Expired":
            if str(item.content) == str(otp):
                return HttpResponse('valid')
    else:
        return HttpResponse("invalid")

############ A2OJ ##########

def a2oj(request, handle):
    try:
        new_entry = A2OJ(
            handle=handle
        )
        new_entry.save()
        return HttpResponse("success")
    except:
        return HttpResponse("failed")