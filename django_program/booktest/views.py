from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.


def index(requst):
    #return HttpResponse('HELOW WORLD')
    text = BookInfo.objects.all()
    context = {"text":text}
    return render(requst,"booktest/index.html",context)
def show(requst,id):
    book = BookInfo.objects.get(pk=id)
    hero = book.heroinfo_set.all()
    # books = BookInfo.objects.get(btitle="中国")
    context = {"hero":hero}
    return render(requst,"booktest/show.html",context)
    pass
