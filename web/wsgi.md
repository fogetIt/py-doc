##### web application
- 浏览器发送一个`HTTP`请求
- 服务器收到请求，生成一个`HTML`文档
- 服务器把`HTML`文档作为`HTTP Body`发送给浏览器
- 浏览器收到`HTTP`响应，从`HTTP Body`取出`HTML`文档并显示

##### 静态服务器
- Apache, Nginx, Lighttpd, e.g.
- 接收用户请求，返回`HTML`

##### CGI
- `Python Web`开发最简单、原始和直接的办法
    + 用一个`Python`脚本（保存成`.cgi`文件），输出`HTML`代码
        1. 打印`Content-Type`、换行、`HTML`的起始标签
        2. 连接数据库并执行一些查询操作，获取指定数据，遍历数据生成`HTML`列表
        3. 输出`HTML`的结束标签并且关闭数据库连接
    + 用户通过浏览器访问`.cgi`文件
    + 每一个连接`fork`一个`CGI`进程

##### FastCGI
- 使用进程/线程池来处理一连串的请求
- 当`Web`服务器把环境变量和页面请求通过一个`Socket`长连接传递给`FastCGI`进程
    + 通过进程/线程池规避了`CGI`开辟新的进程的开销
    + 兼容`CGI`标准
    + 后端的任何故障不会导致`Web Server`挂掉

##### WSGI(Web Server Gateway Interface)
- `Python Web`服务器网关接口
    + 位于`web`应用程序与服务器之间，所在层的位置低于`CGI`
    + 基于`CGI`标准，提升可移植`Web`应用开发的共同点
    + 只要求`Web`开发者`实现一个函数，就可以响应HTTP请求`
    + 只是一份`静态服务器`与`Web`框架之间的接口标准，并没有定义如何去实现
    + 最`pythonic`的接口标准，类似于`Java`中的`servlet API`
    + 解决`Web`应用框架和`Web`服务器之间选择的限制
    + 在`PEP(Python Enhancement Proposal)333`中定义并被许多框架实现，其中包括`django`
- 由专门的`web`服务器实现接受、解析、发送`HTTP`请求、响应的底层代码
- 让`Python`专注于编写`Web`业务（生成`HTML`文档），不接触`TCP`连接、`HTTP`原始请求和响应格式

##### P.S.自从`WSGI`被开发出来以后，许多其它语言中也出现了类似接口
- 2003：Python WSGI
- 2007：Ruby Rack
- 2008：Lua WSAPI
- 2009：Javs JSGI
- 2009：Perl PSGI

### Python Paste
`WSGI`底层工具集，包括多线程、SSL和基于Cookies、sessions等的验证(authentication)库
可以用Paste方便地搭建自己的Web框架