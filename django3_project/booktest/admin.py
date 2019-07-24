from django.contrib import admin
from  .models import *
# Register your models here.
class BookInfoShow(admin.ModelAdmin):
    list_display = ['id','btitle','deletes']

admin.site.register(BookInfo,BookInfoShow)
admin.site.register(HeroInfo)