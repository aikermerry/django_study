from django.shortcuts import render

from regist_index.models import *


# Create your views here.
def index(request):
    id = request.COOKIES.get('user_id')
    username = None
    if id:
        find = UserInfo.objects.filter(id=id)
        username = find[0].username
    context = {'title': '主页', 'username': username}
    return render(request, 'regist_index/index.html', context)


def good_handle(request):
    pass
