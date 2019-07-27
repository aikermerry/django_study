from django.conf.urls import url
from . import views
urlpatterns =[

    url(r'^$',views.index),
    url(r'^posttest1', views.posttest1),
    url(r'^posttest2', views.postTest2),
    url(r'^cookietest', views.cookieTest),
    url(r'^sessiontest$', views.sessionTest),
    url(r'^sessiontest2$', views.sessionTsest2),
    url(r'^sessionOut$', views.sessionLogOut),
    url(r'^regist$',views.regist),
    url(r'^registSave$', views.registSave),


]