from django.contrib import admin
from .models import *
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','username','phonenum','is_delete']
    list_display_links = ['username']


admin.site.register(UserInfo,UserInfoAdmin)