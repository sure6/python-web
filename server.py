# coding=utf-8
"""
date: 2021/7/8 23:05
author: lee sure
"""
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
from wsgiref.simple_server import make_server

from hellopython import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()