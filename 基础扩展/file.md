
|换行符    |操作系统   |
|:--------|:---------|
|'\n'     |Unix      |
|'\r'     |Mac       |
|'\r\n'   |Windows   |
|'U'或'rU'|兼容三种系统|

##### `file()`是一个类，功能等于`open()`
- Python2 建议用`open`
- Python3 没有`file`

##### 打开文件
```python
f = open(name[, mode[, buffering]]) # -> file object，创建文件对象
# f = file(name[, mode[, buffering]])
"""
name    path/to/file.**，默认当前路径
mode    权限(对应操作类型)
    r, 读(默认)
    w, 覆盖写
    a, 追加写
    rb, 二进制读
    wb, 二进制写
    rU, 带有标准换行符的读
    Ua, 带有标准换行符的写
buffering    缓冲
"""

# 用codecs.open，替代open打开文件，避免中文是乱码
import codecs
f = codecs.open(
    filename,
    mode='rb',
    encoding=None,
    errors='strict',
    buffering=1
)
# 读取unicode字符串
f.read(size=None)
f.close()
```

**对一个不存在的文件进行操作，如果权限是读权限会报错，但如果是写的权限就会创建文件。**

##### 读取文件(mode='r')
```python
# 打开一个一次性消耗对象
f = open('***', 'r')

# 通过赋值保存读取的对象
s = f.read([size])    # -> string
s = readline([size])  # -> string
l = readlines([size]) # -> list of strings

# 在for循环中直接使用文件对象进行迭代
for line in open("***"):
    print line
```

##### 写(mode='a'/'w')
```python
f = open("***", "w")
f.write(str)                      # -> None
f.writelines(sequence_of_strings) # -> None
```

##### 关闭并保存文件
```python
f = open("***")
"""
多次关闭不报错
如果不close()，就要等垃圾回收时，自动释放资源。程序执行很长时间，或并发很大时可能耗尽资源，会导致死锁。
"""
f.close()  # -> None/integer

# 使用with，不用写关闭语句
with open("***") as file:
    data = file.read()
```


##### truncate – 清空文件，请小心使用该命令。
##### seek(offset[, whence]) -> None. 移动文件对象当中的指针0 开头，1 当前，2 尾部
##### tell() -> current file position, an integer (may be a long integer).返回当前指针位置
