# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 下午5:19
# @Author  : aiker
# @File    : urls.py
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
]
