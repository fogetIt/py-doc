# -*- coding: utf-8 -*-
# @Date:   2018-02-27 18:09:14
# @Last Modified time: 2018-03-01 16:47:10
# 正序
print('{0},{1},{2}'.format('a', 'b', 'c'), '{},{},{}'.format('a', 'b', 'c'))
# 倒序
print('{2},{1},{0}'.format('a', 'b', 'c'), '{2},{1},{0}'.format(*'abc'))
# 位置参数
print('{0},{1},{0}'.format('abra', 'cad'), '{1},{0},{1}'.format('abra', 'cad'))


# 字典参数
print('Coordinates:{latitude},{longitude}'.format(
    latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates:{latitude},{longitude}'.format(**coord))


c = 3 - 5j  # 复数参数
print(
    'The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'
).format(c)


class Point(object):  # 在类中使用

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x},{self.y})'.format(self=self)

print(str(Point(4, 2)))


coord = (3, 5)  # 元组参数
print('X:{0[0]};Y:{0[1]}'.format(coord))


print("repr() shows quotes: {!r}; str() doesn't: {!s}".format(
    'test1', 'test2'))
print('{:,}'.format(1234567890))
# {!r}{!s}{:,} -> conversion specifier 转换指示符


print('{:<30}'.format('left aligned'))  #: 左对齐
print('{:>30}'.format('right aligned'))  # : 右对齐
print('{:^30}'.format('centered'))      #: 居中对齐
print('{:*^30}'.format('centered'))     #: 填充字符

for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))


print('{:+f}; {:+f}'.format(3.14, -3.14))  # : 显示正号
print('{: f}; {: f}'.format(3.14, -3.14))  # : 空格代替正号
print('{:-f}; {:-f}'.format(3.14, -3.14))  # : 只显示负号，相当于{:f}


print("int: {0:d}; hex: {0:x}; oct: {0:#o}; bin: {0:b}; bin: {0:#b}".format(42))
# hex 十六进制
# oct 八进制
# bin 二进制
octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))
# X表示以十六进制形式输出，02表示不足两位，前面补0输出；出过两位，不影响


points = 19.5
total = 22
print('Correct answers: {:.2%}.'.format(points / total))  # 格式化成包含两位小数的百分数


import datetime
d = datetime.datetime(2010, 7, 4)
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # 格式化时间


width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width))
    print
