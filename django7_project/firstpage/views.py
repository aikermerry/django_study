from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from .models import *
from django.conf import settings


# Create your views here.
def index(request):
    user = UserInfo
    data = user.manage.filter(is_delete=0)

    context = {'data': data}
    return render(request, 'firstpage/index.html', context)


def test1(request):
    values = request.GET.get('key')
    context = {'values': values}
    return HttpResponse(values)


def test2(request):
    name = request.POST.get('name')
    pid = request.POST.get('pid')
    context = {'name': name, 'pid': pid}
    return render(request, 'firstpage/test2.html', context)


# session会话
def test3(request):
    name = request.session.get('name')
    id_card = request.session.get('id_card')
    context = {'name': name, "id_card": id_card}
    return render(request, 'firstpage/test3.html', context)


def login(requset):
    return render(requset, 'firstpage/login.html')


def login_handle(request):
    request.session['name'] = request.POST.get('name')
    request.session['id_card'] = request.POST.get('id_card')
    request.session.set_expiry(0)
    return redirect(reverse('index:test3'))


def logout(request):
    request.session.flush()
    return redirect(reverse('index:test3'))


def upload_index(request):
    return render(request, 'firstpage/upload.html')


def updata_img(request):
    if request.method == 'POST':
        img = request.FILES['imgs']
        context = {'imgname': img.name}
        img_path_name = '%s/%s' % (settings.MEDIA_ROOT, img.name)
        with open(img_path_name, 'wb') as f:
            for i in img.chunks():
                f.write(i)

            return render(request, 'firstpage/img_show.html', context)

def ajax_index(request):
    return render(request,'firstpage/ajax_index.html')
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ajax1(request):

    usename = UserInfo.manage.all()
    print(list(usename.values()))
    return JsonResponse({"data":list(usename.values())})
