from django.contrib import admin
from .models import *


#Register your models here.
#注册模型到哦管理界面

class HeroInfoline(admin.TabularInline):
    model = HeroInfo
    extra = 1
class Bookinfoshow(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    search_fields = ['btitle']
    list_per_page = 10
    list_filter = ['bpub_date']
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),

    ]
    inlines = [HeroInfoline]

class HeroInfoShow(admin.ModelAdmin):
    list_display = ['id','hname','gender','hcontent','inbook']



admin.site.register(BookInfo,Bookinfoshow)
admin.site.register(HeroInfo,HeroInfoShow)