from django.db import models

# Create your models here.
#在模型中直接写数据库语句，
# 框架能自动映射到数据库中，不需要写任何的sql语句


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.btitle
class HeroInfo(models.Model):
    hname = models.CharField('英雄名字',max_length=10)
    hgender = models.BooleanField('性别')
    hcontent = models.CharField('简介',max_length=1000)
    hbook = models.ForeignKey(BookInfo)
    def __str__(self):
        return self.hname

    def gender(self):
        if self.hgender:
            return '♂'
        else:
            return '♀'
    def inbook(self):
        return self.hbook

    gender.short_description = '性别'
    inbook.short_description = '出自书籍'


