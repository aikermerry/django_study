from django.shortcuts import render
from django.http import HttpResponse

from regist_index.models import *
from .models import *


# Create your views here.
def index(request):
    id = request.COOKIES.get('user_id')
    username = None
    if id:
        find = UserInfo.objects.filter(id=id)
        username = find[0].username
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    typec0 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    typec1 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    typec2 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    typec3 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    typec4 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    typec5 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context = {'title': '主页', 'username': username, 'page': 1,
               'type0': type0, 'typec0': typec0,
               'type1': list(type1), 'typec1': typec1,
               'type2': list(type2), 'typec2': typec2,
               'type3': list(type3), 'typec3': typec3,
               'type4': list(type4), 'typec4': typec4,
               'type5': list(type5), 'typec5': typec5,

               }
    return render(request, 'show_goods/index.html', context)

def goodsList(request,id):
    user_id = request.COOKIES.get('user_id')
    username = None
    if user_id:
        find = UserInfo.objects.filter(id=user_id)
        username = find[0].username

    typeinfo = TypeInfo.objects.filter(id=id)
    typename = typeinfo[0].title
    goodsLists = typeinfo[0].goodsinfo_set.all()
    nwegoods = typeinfo[0].goodsinfo_set.order_by('-id')[0:2]

    context = {'title':'商品列表','username':username,'page':2,'typename':typename,
               'goodslists':goodsLists,'newgoods':nwegoods}
    return render(request,'show_goods/list.html',context)


def detail(request, id):
    goods = goodsInfo.objects.filter(id=int(id))[0]
    typeinfo = TypeInfo.objects.filter(id=goods.gtype_id)
    typename = typeinfo[0]


    newgoods = typeinfo[0].goodsinfo_set.order_by('-id')[0:2]

    user_id = request.COOKIES.get('user_id')
    username = None
    if user_id:
        find = UserInfo.objects.filter(id=user_id)
        username = find[0].username

    goods.gclick += 1
    goods.save()
    context = {'title':'商品详情','page':1,'goods':goods,
               'username':username,'newgoods':newgoods,
               'select':1,'typename':typename}
    return render(request,'show_goods/detail.html',context)

