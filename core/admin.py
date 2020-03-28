from django.contrib import admin
from .models import *

@admin.register(Lock)
class LockAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lock', 'time_created', 'time_remaining', 'content', 'valid_till')
