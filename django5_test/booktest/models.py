from django.db import models

# Create your models here.

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=0)
    isdelete = models.BooleanField(default=0)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
    def __str__(self):
        return self.hname

    class Meta():
        db_table = 'heroinfo'

    def show(self):
        return self.hname

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.BooleanField(default=0)

    class Meta():
        db_table = 'bookinfo'

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)

    class Meta():
        db_table ='userinfos'




