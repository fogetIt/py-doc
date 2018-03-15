# -*- coding: utf-8 -*-
# @Date:   2018-03-15 15:42:37
# @Last Modified time: 2018-03-15 15:42:52
"""
wsgi 服务器
python2 下运行此文件
"""
from wsgiref.simple_server import make_server
from wsgi_application import application


httpd = make_server("localhost", 8000, application)
print("Serving HTTP on port 8000...")

if __name__ == '__main__':
    # 监听 HTTP 请求
    httpd.serve_forever()
