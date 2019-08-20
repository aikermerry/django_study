# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 下午4:45
# @Author  : aiker
# @File    : urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login$',views.login,name='login'),
    url(r'^register$',views.regist,name='register'),
    url(r'^regist_handle$',views.regist_handle,name='regist_handle'),
    url(r'^usercheck(.*)$', views.usercheck, name='usercheck'),
    url(r'^login_handle$',views.login_handle,name='login_handle'),
    url(r'^usercenter$',views.userCenter,name="userCenter"),
    url(r'^userCenter_handle', views.userCenter_handle, name="userCenter_handle"),


]