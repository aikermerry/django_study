from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from django.conf import settings
from django.views.decorators.cache import cache_page
import os


from .models import *

def index(resquese):
    return render(resquese,'booktest/index.html')

#上传文件
def picsave(request):
    if request.method == "POST":
        f1 = request.FILES['pic']
        fname = '%s' % os.path.join(settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse(f1,'image/jpg')
    else:
        return HttpResponse("error")

#分页


def pageDevice(request,pindex):
    if pindex =='':
        pindex='1'
    list = HeroInfo.objects.all()
    paginator = Paginator(list,5)#分成5个数据一页
    page = paginator.page(int(pindex))#选择页数
    context = {'page':page,'page_num':int(pindex)}
    return render(request,"booktest/page.html",context)

#ajax使用
def area1(request):
    return render(request,'booktest/area.html')

def area2(request,id):
    if id =='0':
        lists = areasInfo.objects.filter(pid__isnull=True).values('id','title')
    else:
        lists = areasInfo.objects.get(id=int(id)).areasinfo_set.all().values('id','title')
    # lists=[]
    # print(lists)
    print(lists)
    # for i in list:
    #     lists.append([i.title,i.id])
    # print(lists)
    return JsonResponse({'data':list(lists)})

#redict缓存
@cache_page(60*10)
def textEditer(request):
    return render(request,'booktest/textEditer.html')

@cache_page(60*10)
def cache(request):
    return HttpResponse("hello")

def modelCache(request):
    return render(request,'booktest/cache.html')

def searchInfo(request):
    return render(request,'booktest/search.html')