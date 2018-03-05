`python`内置装饰器
=================

##### @property
- 把一个方法变成属性调用（只能访问、不能修改）
- 可以添加`getter, setter, deleter`
    + `@method.setter,@method.getter,@method.deleter`
    + `property(fget=None, fset=None, fdel=None, doc=None)`

##### @staticmethod
- 类似静态语言中的`静态方法`，将外部函数集成到类体中
    + 可以访问类成员（使用`ClsName.attr`）
    + 不可以访问实例成员（没有`self`）
- 不需要实例化即可调用
    + 可以被`类对象`调用
    + 可以被`实例对象`调用
- 静态方法不绑定（类或实例）对象
    + Cls().static_func.__self__ -> error
- 静态方法如果不覆盖，就无法改变
    + 可以使用`@staticmethod`覆盖
    + 也可以作为普通类属性`self`覆盖

##### @classmethod
- 和类相关的方法，隐式地传入类变量（`cls`）作为第一参数，避免硬编码类名
    + 可以访问类成员（使用`cls.attr`）
    + 不可以访问实例成员（没有`self`）
- 不需要实例化即可调用
    + 可以被`类对象`调用
    + 可以被`实例对象`调用
- 类方法绑定类对象
    + Cls().class_func.__self__ -> Cls
- 工厂方法：使用`@staticmethod`/`@classmethod`创建类的实例，例如一些预处理
- e.g.
    ```python
    class A(object):

        @classmethod
        def test(cls, *args, **kwargs):
            ...

        # equals
        test = classmethod(test)
    ```