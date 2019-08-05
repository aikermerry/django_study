from django.db import models


class ManageUserInfo(models.Manager):

    def get_queryset(self):
        return super(ManageUserInfo, self).get_queryset().all()
        #     return super(BookManage, self).get_queryset().filter(isDelete=False)
    def inserts(self,username,pawd,phone,adre,is_delete,pubdate):
        user_info = UserInfo()
        user_info.username = username
        user_info.password = pawd
        user_info.phonenum = phone
        user_info.address = adre
        user_info.is_delete = is_delete
        user_info.upub_date  = pubdate
        user_info.save()


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=20)
    phonenum = models.CharField('电话',max_length=20)
    address = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=0)
    upub_date = models.DateField()

    class Meta():
        db_table = 'userinfo'
    manage = ManageUserInfo()


