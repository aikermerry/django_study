from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    title = models.CharField('类型',max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class goodsInfo(models.Model):
    gtitle = models.CharField('标题',max_length=20)
    gpic = models.ImageField('图片',upload_to='show_goods')
    gprice = models.DecimalField('价格',max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField('单价',max_length=20,default='500g')
    gclick = models.IntegerField('点击量')
    # gsale = models.IntegerField()
    gjianjie = models.CharField('简介',max_length=200)
    gkucun = models.IntegerField('库存')
    gcontext = HTMLField('详细描述')
    gtype = models.ForeignKey(TypeInfo)
    # gadv = models.BooleanField(default=False)
    def __str__(self):
        return self.gtitle