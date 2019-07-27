from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from .models import *
# Create your views here.
def index(request):
    return render(request,'booktest/index.html')

def posttest1(request):

    return  render(request,'booktest/posttest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upawd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    content = {'uname':uname,'upwd':upawd,'ugender':ugender,'uhobby':uhobby,'request':request}

    return render(request,'booktest/posttest2.html',content)

def cookieTest(request):
    response = HttpResponse()
    # if request.COOKIES['h1']:
    #     response.write('<h1>'+request.COOKIES['h1']+'</h1>')
    response.set_cookie('h1','passwd',10)
    return response
def sessionTest(request):
    uname = request.session.get('uname')
    upwd = request.session.get('upwd')
    content = {'uname':uname ,'upwd':upwd}
    return render(request,'booktest/sessiontest1.html',content)

def sessionTsest2(request):

    request.session['uname'] = request.POST['uname']
    request.session['upwd'] = request.POST['upwd']
    return redirect('/booktest/sessiontest')


def sessionLogOut(request):
    request.session.flush()
    return redirect('/booktest/sessiontest')

def regist(request):
    return render(request,'booktest/regist.html')

def registSave(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    request.session['uname'] = uname
    request.session['upwd'] = upwd
    if uname:
        if not len(UserInfo.objects.filter(uname=str(uname))):
            b = UserInfo.objects.inster(uname,upwd)
            b.save()
            return redirect('/booktest/sessiontest')
        return HttpResponse("<script>window.alert('你已注册');window.location.href='/booktest/regist';</script>")
    return redirect('/booktest/regist')





