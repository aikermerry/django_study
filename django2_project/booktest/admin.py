from django.contrib import admin
from booktest.models import *
# Register your models here.

class show_hero(admin.ModelAdmin):
    list_display = ['id','hname','book']
    ordering = ['id']
    pass


admin.site.register(HeroInfo,show_hero)
admin.site.register(BookInfo)