from django.db import models


class UserInfo(models.Model):
    userInfo_name = models.CharField(max_length=50)
    userInfo_email = models.CharField(max_length=60)
    userInfo_phone = models.IntegerField()
    userInfo_comment = models.TextField()
# Create your models here.
