from django.db import models


#定义管理器
class BookInfoManage(models.Manager):

    def get_queryset(self):
        return super(BookInfoManage,self).get_queryset().filter(isDelete = False)
    def inster(self,title,data,breade,comment,isdelete):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = data
        b.bread = breade
        b.bcommet = comment
        b.isDelete = isdelete
        return b

#定义模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table="bookinfo"
    def __str__(self):
        return self.btitle
    newmanage = BookInfoManage()

# Create your models here.
class HeroInfo(models.Model):
    hname = models.CharField("姓名",max_length=20)
    hgender = models.BooleanField("性别",default=True)
    isdelete = models.BooleanField(default=0)
    hconment = models.CharField("简介",max_length=100)
    hbook = models.ForeignKey(BookInfo)
    def book(self):
        return self.hbook
    def __str__(self):
        return self.hname
    class Meta():
        db_table = "heroinfo"
    book.short_description="书名"


