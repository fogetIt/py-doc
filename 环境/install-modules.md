##### 配置环境变量
- `.exe`程序的搜索路径，系统通过`PATH`找到`.exe`程序，再调用`.py`文件
    1. python安装包路径;
    2. python安装包路径\Scripts;

**site-packages，第三方包安装路径**

###### setuptools
- 包管理工具，用来安装第三方包
- `Python Enterprise Application Kit(PEAK)`的一个副项目
    + 它是一组`Python distutilsde`工具的增强工具
    + 可以让程序员更方便的创建和发布`Python`包，特别是那些对其它包具有依赖性的状况下
    + `easy_install`是由`PEAK setuptools`包里带的一个命令
    + 使用`easy_install`实际上是在调用`setuptools`来完成安装模块的工作
- 安装
    + win
        * [下载](https://pypi.python.org/pypi/setuptools)`ez_setup.py`
        * python ez_setup.py
    + linux
        * sudo apt-get install python-setuptools
    + 安装完成后，`easy_install`会被自动复制到`${python}\bin`下
    + 只要配置了`PATH`，可以在终端直接运行`easy_install`命令
- 使用
    + easy_install `egg`包/模块名称/网址
    + 默认安装最新版的第三方模块
- `setuptools`功能
    + 利用`EasyInstall`自动查找、下载、安装、升级依赖包
    + 创建`Python Eggs`
    + 包含包目录内的数据文件
    + 自动包含包目录内的所有的包，而不用在`setup.py`中列举
    + 自动包含包内和发布有关的所有相关文件
    + 自动生成经过包装的脚本或`Windows`执行文件
    + 支持`Pyrex`，即在`setup.py`中列出`.pyx`文件
    + 可以部署开发模式，使项目在`sys.path`中
    + 用新命令或`setup()`参数扩展`distutils`，为多个项目发布/重用扩展；
    + 在项目`setup()`中简单声明`entry points`，创建可以自动发现扩展的应用和框架

##### pip
- 依赖`VS2008`
    + 安装`VCForPython27`
    + 或者`Micorsoft Visual C++ Compiler for Python 2.7`
- 安装
    + easy_install pip
    + python get-pip.py
    + yum -y install epel-release python-pip
- 使用
    + pip install ***
    + pip install *** --upgrade
    + pip uninstall ***
    + python -m pip install ***
    + 安装`wheel`包
        * pip install wheel
        * pip install ***.whl/http://...
- 国内镜像
    ```shell
    pip install *** -i http://mirrors.tuna.tsinghua.edu.cn/pypi/simple
    ```

##### 第三方模块安装
- 下载模块包，解压
- 进入`setup.py`所在目录
- python setup.py install

##### 模块安装提示错误：找不到python.h文件
- yum search python | grep python-devel || yum install python-devel.x86_64
- sudo apt-get install python-2.7-dev

---
##### 科学计算模块
- [numpy————数据分析](http://sourceforge.net/projects/numpy/files/NumPy/)
    - easy_install numpy
- [scipy](http://sourceforge.net/projects/scipy/files/)
- [matplotlib](http://matplotlib.org/downloads.html)

##### Anaconda
- 一个`python`的发行版，包括了`python`和很多常见的软件库
    + Python
    + [ipython](http://archive.ipython.org/release/2.3.1/ipython-2.3.1.zip)
        *  解压，进入解压包目录
        *  python setup.py install
        *  ipython在Scripts文件夹下
    + Ipython QTConsole
    + IPython Notebook
    + Spyder(IDE)

pip/conda（anaconda自带的包管理器） list，查看已经安装的包。
pip/conda install 包名，安装新的包。

#### mysql-connector-python
- `Python MySQL`官方包
- 用法和`MySQLdb`基本类

##### Twisted
- 异步网络库
- 处理网络通讯
- 架构清晰，并且包含了各种中间件接口，可以灵活的完成各种需求

##### 手动安装
- [pywin32](http://sourceforge.net/projects/pywin32/files%2Fpywin32/)
- [pycrypto](http://www.voidspace.org.uk/python/modules.shtml#pycrypto)