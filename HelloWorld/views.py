from django.shortcuts import render

# Create your views here.
#coding:utf-8
from django.http import HttpResponse
def index(request):
    return render(request,"index.html",)
      # return HttpResponse(u"Hello World! 大家好！")
