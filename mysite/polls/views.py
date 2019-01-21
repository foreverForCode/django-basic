# -*- coding: utf-8 -*-

from django_redis import get_redis_connection

from mysite.util import restful

def index(request):

    conn = get_redis_connection("default")

    conn.hset('kkk', 'age', 18)

    res = {
        'data': conn.hget('kkk', 'age')
    }

    return restful.jsonp(res, 200)

def detail(request, question_id):

    china = '防守打法'

    str = "You're looking at question %s." %question_id

    data = {
        'data': china
    }

    return restful.jsonp(data, 200)

# def results(request, question_id):
#
#     return HttpResponse(question_id)
#
# def vote(request, question_id):
#
#     return HttpResponse(question_id)

# Create your views here.
