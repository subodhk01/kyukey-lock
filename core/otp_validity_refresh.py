from .models import OTP, Manager
from django.contrib.auth.models import User
import datetime
import pytz

class otpRefresh(object):
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        try:
            otps = OTP.objects.all()
            if len(otps) == 0:
                response = self.get_response(request)
                return response
            for otp in otps:
                #print(otp.valid_till + datetime.timedelta(hours=5, minutes=30) ,datetime.datetime.now())
                if(otp.valid_till.replace(tzinfo=pytz.UTC) + datetime.timedelta(hours=5, minutes=30) > datetime.datetime.now().replace(tzinfo=pytz.UTC)):
                    seconds = (otp.valid_till.replace(tzinfo=pytz.UTC) + datetime.timedelta(hours=5, minutes=30) -  datetime.datetime.now().replace(tzinfo=pytz.UTC)).seconds
                    if seconds > 7200 :
                        otp.time_remaining = str(seconds//3600) + " hours " + str((seconds%3600)//60) + " minutes"
                    elif seconds > 3600 :
                        otp.time_remaining = str(seconds//3600) + " hour " + str((seconds%3600)//60) + " minutes"
                    else:
                        otp.time_remaining = str((seconds%3600)//60) + "minutes"
                else:
                    otp.time_remaining = "Expired"
                #print(otp.time_remaining)
                otp.save()
        except:
            print("Error in OTP middleware")
        users = User.objects.all()
        for user in users:
            try:
                user.manager = Manager()
                user.manager.save()
                print('saved manager for : ', user)
            except:
                print('manager already exists : ', user)

        response = self.get_response(request)
        return response