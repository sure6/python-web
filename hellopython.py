# coding=utf-8
"""
date: 2021/7/8 23:06
author: lee sure
"""
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return body.encode('utf-8')