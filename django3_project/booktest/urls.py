from django.conf.urls import url
from . import views
urlpatterns =[
    url(r"^$",views.index),
    url(r'^test1',views.test1),
    url(r'^test2',views.test2),
]