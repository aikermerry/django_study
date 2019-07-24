from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.

def index(request):
    list=BookInfo.newmanage.filter(pk__gt=1)

    content ={"list":list,"requst":request}

    return render(request,"booktest/index.html",content)
