from django.contrib import admin

from .models import *
# Register your models here.
class ShowHeroInfo(admin.ModelAdmin):

    list_display = ['id','hname','hgender','deletes',]
    ordering = ['id']
    list_display_links = ('hname',)




class ShowBookInfo(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date','deletes']
    ordering = ['id']
    list_display_links = ['btitle']


admin.site.register(BookInfo,ShowBookInfo)
admin.site.register(HeroInfo,ShowHeroInfo)