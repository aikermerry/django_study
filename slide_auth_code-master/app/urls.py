from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^pc-geetest/register', pcgetcaptcha, name='pcgetcaptcha'),
    url(r'^mobile-geetest/register', pcgetcaptcha, name='mobilegetcaptcha'),
    url(r'^pc-geetest/validate$', pcvalidate, name='pcvalidate'),
    url(r'^pc-geetest/ajax_validate',pcajax_validate, name='pcajax_validate'),
    url(r'^mobile-geetest/ajax_validate',mobileajax_validate, name='mobileajax_validate'),
    url(r'^', home, name='home'),
]