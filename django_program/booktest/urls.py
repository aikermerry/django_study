from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$|index',views.index),
    url(r'^(\d+)$',views.show),

]

