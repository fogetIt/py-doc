# -*- coding: utf-8 -*-
# @Date:   2018-03-15 15:19:51
# @Last Modified time: 2018-03-15 15:20:52

# 通过 uwsgi 运行该文件
# uwsgi --http :8001 --wsgi-file wsgi.py
# 浏览器访问 localhost:8001


def application(environ, start_response):
    print(environ)  #: {'LESS': '-R', 'QT4_IM_MODULE': 'fcitx',...}
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


'''
通过 WSGI
    从 environ dict 拿到 HTTP 请求信息
    然后构造 HTML 
    通过 start_response() 发送 Header 
    最后返回 Body

整个 application() 函数本身没有涉及到任何解析 HTTP 的部分
底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了

application() 函数必须由 WSGI 服务器来调用，传来参数 environ 和 startt_response

wsgiref
    用纯 Python 编写的 WSGI 服务器的参考实现
    完全符合 WSGI 标准，但是不考虑任何运行效率，仅供开发和测试使用
'''
