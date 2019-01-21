# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

"""
    /login/v1  [POST] params[username, password]  登录接口
    
"""


urlpatterns = [

    url(r'^$', views.index, name='index'),
    # url(r'^/v1$', views.login, name='login')
]
