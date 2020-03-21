from django.contrib import admin
from .models import *

@admin.register(Lock)
class LockAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'lock', 'time_created', 'content', 'valid_till')
