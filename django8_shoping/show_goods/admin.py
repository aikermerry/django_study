from django.contrib import admin
from .models import *


# Register your models here.

class Goods(admin.ModelAdmin):
    list_display = ['gtitle','gpic', 'gprice', 'gunit', 'gclick']

class Type(admin.ModelAdmin):
    list_display = ['id','title']



admin.site.register(goodsInfo,Goods)

admin.site.register(TypeInfo,Type)
