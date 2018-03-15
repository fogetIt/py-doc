##### WSGI(Web Server Gateway Interface)
- `Python Web`服务器网关接口
    + 基于`CGI`标准，提升可移植`Web`应用开发的共同点
    + 只要求`Web`开发者`实现一个函数，就可以响应HTTP请求`
    + 只是一份`静态服务器`与`Web`框架之间的接口标准，并没有定义如何去实现
    + 最`pythonic`的接口标准，类似于`Java`中的`servlet API`
    + 解决`Web`应用框架和`Web`服务器之间选择的限制
    + 在`PEP(Python Enhancement Proposal)333`中定义并被许多框架实现，其中包括`django`
- 由专门的`web`服务器实现接受、解析、发送`HTTP`请求、响应的底层代码
- 让`Python`专注于编写`Web`业务（生成`HTML`文档），不接触`TCP`连接、`HTTP`原始请求和响应格式

##### 自从`WSGI`被开发出来以后，许多其它语言中也出现了类似接口
- 2003：Python WSGI
- 2007：Ruby Rack
- 2008：Lua WSAPI
- 2009：Javs JSGI
- 2009：Perl PSGI


##### [流程示意图](wsgi.png)


##### Python Paste
- `WSGI`底层工具集
    + 包括多线程、SSL和基于Cookies、sessions等的验证库
- 可以用Paste方便地搭建自己的Web框架
