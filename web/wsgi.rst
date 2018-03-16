WSGI(Web Server Gateway Interface)
==================================
    - 一份 **静态服务器** 与 **Web** 框架之间的接口标准，并没有定义如何去实现
        + 基于 **CGI** 标准，提升可移植 **Web** 应用开发的共同点
        + 最 **pythonic** 的接口标准，类似于 **Java servlet API**
        + 解决 **Web** 应用框架和 **Web** 服务器之间选择的限制
        + 在 **PEP(Python Enhancement Proposal)333** 中定义并被许多框架实现，其中包括 **django**
    - 由专门的 **web** 服务器实现接受、解析、发送 **HTTP** 请求、响应的底层代码
    - 让 **Python** 专注于编写 **Web** 业务（生成 **HTML** ），不接触 **TCP** 连接、 **HTTP** 原始请求和响应格式


WSGI 标准的 HTTP 处理
--------------------
    :application: 一个可调用对象（函数），响应 **HTTP** 请求

        - 接受两个参数（由 wsgi 服务器提供）
            :environ:        一个包含了 **WSGI** 环境（ **HTTP** 请求内容）信息的 **dict**
            :start_response: 一个发送 **response Header** ， 开始响应请求的函数，每次请求只能调用一次

                - 接受两个参数
                    - **HTTP** 状态码
                    - ``response headers list`` ，每个 **Header** 用一个包含两个 **str** 的 **tuple** 表示
        - 返回 **iterable** 作为 ``response Body``
    - 无论多么复杂的 ``python Web`` 应用，入口都是一个 **WSGI** 处理函数
    - `流程示意图 <wsgi.png>`_
    - `wsgi 应用实现示意 <wsgi_application.py>`_
    - `wsgi 服务器实现示意 <wsgi_server.py>`_


其它语言中的类似接口
------------------
    :2003: Python WSGI
    :2007: Ruby Rack
    :2008: Lua WSAPI
    :2009: Java JSGI
    :2009: Perl PSGI


Python Paste
-------------
    - **WSGI** 底层工具集
        - 包括多线程、SSL和基于Cookies、sessions等的验证库
        - 可以方便地搭建自己的Web框架
