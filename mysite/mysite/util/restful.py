# -*- coding: utf-8 -*-


# 封装restful风格的数据

import json

from django.http import HttpResponse


def error(code):

    """
    @params: code [num] 200 | 400 | 500
    @return: [dict]

    """
    if code == 200:

        return {

            'code': 200,
            'errMsg': '成功',
        }
    elif code == 400:

        return {

            'code': 400,
            'errMsg': '失败'
        }

    else:
        return {

            'code': 500,
            'errMsg': '服务器异常'
        }


def jsonp(data, code):
    """
        @desc 返回restful风格数据

        @params data [dict] 实际输出的结果
        @params code [num]  状态码 200 | 400 | 500

        @return [httpresponse]
    """
    temp = error(code)

    if type(data).__name__ != 'dict':

        data = {}
        temp = error(500)
        temp['errMsg'] = '数据必须是dict'

    result = dict(temp, **data)

    result = json.dumps(result)

    return HttpResponse(result, content_type='application/json', charset='utf-8')

