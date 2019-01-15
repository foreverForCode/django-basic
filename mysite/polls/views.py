from django.shortcuts import render

import redis

from django_redis import get_redis_connection

from django.http import HttpResponse

def index(request):

    print request

    conn = get_redis_connection("default")

    conn.hset('kkk', 'age', 18)


    return HttpResponse(conn.hget('kkk', 'age'))

# Create your views here.
