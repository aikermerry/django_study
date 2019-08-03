from django.conf.urls import url
from . import views
urlpatterns =[
    url('^$|index',views.index,name='index'),
    url(r'^picsave',views.picsave,name='picsave'),
    url(r'^page/(\d*)', views.pageDevice, name='page'),
    url(r'^area$', views.area1, name='ares'),
    url(r'^area/(\d+)', views.area2, name='ares2'),
    url(r'^textediter',views.textEditer),
    url(r'^cache', views.cache),
    url(r'modelcache',views.modelCache),
    url(r'searchtest', views.searchInfo),

]