from django.db import models

# Create your models here.
class BookManage(models.Manager):
    def get_queryset(self):
        return super(BookManage,self).get_queryset().filter(isDelete = False)

    def inster(self, title, data, breade, comment, isdelete):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = data
        b.bread = breade
        b.bcommet = comment
        b.isDelete = isdelete
        return b



class BookInfo(models.Model):
    btitle = models.CharField("目录",max_length=20)
    bpub_date = models.DateTimeField("时间")
    bread = models.IntegerField("阅读量",default=0)
    bcomment = models.IntegerField("评论量",default=0)
    isDelete = models.BooleanField("是否删除",default=0)
    class Meta():
        db_table = "bookinfo"
    def deletes(self):
        if self.isDelete:
            return "已删除"
        else:
            return "未操作"
    def __str__(self):
        return self.btitle
    books = BookManage()

class HeroInfo(models.Model):
    hname = models.CharField("姓名",max_length=20)
    hgender = models.BooleanField("性别",default=0)
    isDelete = models.BooleanField("是否删除",default=0)
    hcontent = models.CharField("简介",max_length=100)
    hbook =  models.ForeignKey(BookInfo)
    class Meta():
        db_table = "heroinfo"
    def deletes(self):
        if self.isDelete:
            return "已删除"
        else:
            return "未操作"
    def __str__(self):
        return self.hname


