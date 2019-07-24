from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(requst):
    book = BookInfo.books.get(pk=2)
    book = book.heroinfo_set.all()
    comtent = {'book':book}

    return render(requst,'booktest/index.html',comtent)

def test1(requst):
    a = requst.GET['a']
    b = requst.GET['b']
    path = requst.COOKIES
    return HttpResponse(path)


def test2(requst):
    a_list = requst.GET.getlist('a')
    
    return HttpResponse('A:%s'%a_list)
def image():
    
    pass