##### 自省
- globals()
    + 以字典的方式返回所有全局变量
- locals()
    + 以字典的方式返回所有局部变量
- vars(object)
    + 查看对象的属性和属性值的字典对象（`__dict__`）
    + 没有给定对象时，等同于`locals()`
- e.g.
```python
# 在全局作用域中
print locals() == globals() == vars()
print globals()
"""
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__file__': '/home/zdd/github/docTree/DesignPattern/globals_test.py', '__doc__': None, '__package__': None}
"""
import os
print vars(os) == os.__dict__

# 使用命名空间判断变量是否存在
demo = 10
print 'demo' in locals().keys()
print 'demo' in dir()