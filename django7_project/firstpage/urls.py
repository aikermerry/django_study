from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^test1/$',views.test1,name='test1'),
    url(r'^test2$',views.test2,name='test2'),
    url(r'^test3$', views.test3, name='test3'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login_handle$', views.login_handle, name='login_handle'),
    url(r'^updata_img', views.updata_img, name='updata_img'),
    url(r'^upload$', views.upload_index, name='upload_index'),
    url(r'^ajax_index', views.ajax_index, name='ajax_index'),
    url(r'^ajax1', views.ajax1, name='ajax'),

]

