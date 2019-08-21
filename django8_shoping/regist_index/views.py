from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from hashlib import sha1

from .models import *


# Create your views here.

def login(request):
    erroruser = request.COOKIES.get('erroruser', 0)
    errorpwd = request.COOKIES.get('errorpwd', 0)
    username = request.COOKIES.get('username', 0)
    # print(username,erroruser,errorpwd)

    username = request.session.get('username', default=username)
    password = request.session.get('password', default=0)
    keep_username = request.session.get('keep_username', default=1)

    context = {'username': username, 'password': password,
               'title': '登录', 'keep_username': keep_username, 'errorpwd': errorpwd, 'erroruser': erroruser}

    print(context)
    return render(request, 'regist_index/login.html', {'data': context})


def login_handle(request):
    global erroruser, errorpwd

    if request.method == "POST":
        erroruser = 1

        keep = request.POST.get('keep_username')
        pwd = request.POST.get('pwd')
        username = request.POST.get('username')
        if keep:
            request.session['username'] = username
            request.session['keep_username'] = keep
        else:
            # 删除当前用户的所有Session数据
            request.session.clear()
        # 验证
        check = UserInfo.objects.filter(username=username)


        response = HttpResponse()
        if check.count():
            erroruser = 0

            p = sha1()
            p.update(pwd.encode("utf-8"))
            hpwd = p.hexdigest()

            cpwd = check[0].userpassword
            # print('密码验证')
            errorpwd = 1
            if hpwd == cpwd:
                errorpwd = 0
                request.session['password']=''
                response.delete_cookie('erroruser')
                response.delete_cookie('errorpwd')
                response.set_cookie('username', username)
                user_id = check[0].id
                response.set_cookie('user_id', user_id)
                response.write("<script>window.location='/'</script>")
                return response

        response.set_cookie('erroruser', erroruser)
        response.set_cookie('errorpwd', errorpwd)
        response.set_cookie('username', username)
        response.write("<script>window.location='/user/login'</script>")
        request.session['password'] = pwd
        return response

    return HttpResponse('<h1>404出错了</h1>')


def regist(request):
    context = {'title': '注册'}
    return render(request, 'regist_index/register.html', context)


def regist_handle(requset):
    if requset.method == 'POST':
        user_name = requset.POST.get('user_name')
        pwd = requset.POST.get('pwd')
        cpwd = requset.POST.get('cpwd')
        email = requset.POST.get('email')
        # 密码加密
        p = sha1()
        p.update(pwd.encode("utf-8"))
        pwd = p.hexdigest()
        # 保存密码与账号好session
        userinfo = UserInfo()
        userinfo.username = user_name
        userinfo.userpassword = pwd
        userinfo.useremal = email
        requset.session['password'] = cpwd
        requset.session['username'] = user_name
        userinfo.save()
        return redirect(reverse('regist_index:login'))


def usercheck(request, user_name):
    check = UserInfo.objects.filter(username=user_name).count()
    return JsonResponse({'data': check})


def userCenter(request):
    global address, phonenum, phonenum, recv_user_name, username, youbian

    user_id = request.COOKIES.get('user_id')
    user_info = UserInfo.objects.filter(id=user_id)
    if user_info:
        user_info = user_info[0]
        address = user_info.address
        phonenum = user_info.phonenum
        youbian = user_info.youbian
        recv_user_name = user_info.recvusername
        username = user_info.username

    context = {'title':'用户中心','username': username, "address": address, 'phonenum': phonenum, 'youbian': youbian,
               'recv_user_name': '(%s 收)' % recv_user_name}
    print(context)
    return render(request, 'regist_index/user_center_site.html', context)


def userCenter_handle(request):
    if request.method == 'POST':
        recv_user_name = request.POST.get('recv_user_name')
        address = request.POST.get('address')
        phonenum = request.POST.get('phonenum')
        youbian = request.POST.get('youbian')
        user_id = request.COOKIES.get('user_id')
        user_info = UserInfo.objects.filter(id=user_id)
        userinfo = user_info[0]
        userinfo.address = address
        userinfo.recvusername = recv_user_name
        userinfo.youbian = youbian
        userinfo.phonenum = phonenum
        userinfo.save()
        return redirect(reverse('regist_index:userCenter'))
    return HttpResponse('<h1>404出错了</h1>')
