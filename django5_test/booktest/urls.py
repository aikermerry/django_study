from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^bar(\d)',views.bar,name='bar'),
    url(r'^base', views.base, name='base'),
    url(r'^test1', views.test1, name='test1'),
    url(r'^test2', views.test2, name='test2'),
    url(r'^codetest', views.codetest),

]