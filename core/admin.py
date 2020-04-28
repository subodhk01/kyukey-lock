from django.contrib import admin
from .models import *

@admin.register(Lock)
class LockAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lock', 'time_created', 'time_remaining', 'content', 'valid_till', 'visibility')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'lock', 'time','status', 'otp')

@admin.register(A2OJ)
class A2OJAdmin(admin.ModelAdmin):
    list_display = ('time', 'handle')
    search_fields = ('handle')
