from django.db import models

class Lock(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return "%s: %s" % (self.id, self.status)

class OTP(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_remaining = models.CharField(max_length=50, default=None, null=True)
    content = models.CharField(max_length=10)
    lock = models.ForeignKey(Lock, on_delete=models.CASCADE)
    valid_till = models.DateTimeField()
    visibility = models.BooleanField(default=1)

    def __str__(self):
        return "Lock(%s) : %s" % (self.lock, self.content)

    class Meta:
        ordering = ['lock']

class History(models.Model):
    id = models.AutoField(primary_key=True)
    lock = models.ForeignKey(Lock, on_delete=models.SET_NULL, null=True)
    otp = models.ForeignKey(OTP, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class A2OJ(models.Model):
    handle = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
