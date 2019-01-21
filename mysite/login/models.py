# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class LoginUser(models.Model):

    name_text = models.CharField(max_length=20)  # 用户名
    password = models.CharField(max_length=20)   # 密码
    pub_date = models.DateTimeField('date published')   # 生成时间

