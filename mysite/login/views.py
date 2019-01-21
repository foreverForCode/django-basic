# -*- coding:utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse

from mysite.util import restful

from .models import LoginUser

from django.utils import timezone

# Create your views here.

def index(request):

    return restful.jsonp({'data' : '登录成功'}, 200)




