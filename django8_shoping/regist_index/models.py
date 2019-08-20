from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField('用户名',max_length=20)
    userpassword = models.CharField(max_length=40)
    useremal = models.CharField(max_length=25)
    address = models.TextField(max_length=100,null=True)
    youbian = models.CharField(max_length=8,null=True)
    phonenum = models.CharField(max_length=11,null=True)
    recvusername = models.CharField(max_length=20,null=True)


    class Meta():
        db_table = 'userinfo'



