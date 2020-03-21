from django.db import models

class Lock(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return "%s: %s" % (self.id, self.status)

class OTP(models.Model):
    id = models.AutoField(primary_key=True)
    time_created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=10)
    lock = models.ForeignKey(Lock, on_delete=models.CASCADE)
    valid_till = models.DateTimeField()

    def __str__(self):
        return "Lock(%s) : %s" % (self.lock, self.content)

    class Meta:
        ordering = ['lock']
