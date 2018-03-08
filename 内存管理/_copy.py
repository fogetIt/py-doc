# -*- coding: utf-8 -*-
# @Date:   2016-09-20 09:18:46
# @Last Modified time: 2018-02-02 13:18:17
import copy
import gc
gc.get_referrers()

# 赋值操作（包括对象作为参数、返回值）不会开辟新的内存空间
# 只是复制了新对象的引用
# 所有复制、被复制的对象数据的操作会互相影响
list1 = ['nvjf', ['dml'], tuple('koa')]
list0 = list1
list0[0] = 'ppp'
print(list1)
print(list0)
print()

# 浅拷贝会创建新对象，其内容是原对象的引用
# 不管多么复杂的数据结构，浅拷贝都只会copy一层
# 不可变类型浅拷贝，id不变
# 可变类型浅拷贝，id改变
#
# 切片操作
list2 = list1[:]
list2[2] = 'dml'  # 第一层数据的操作不会互相影响
list2[1][0] = 'jb'  # 嵌套数据的操作会互相影响
print(list2)
print(list1)

# 工厂函数
list3 = list(list1)

# copy函数
list4 = copy.copy(list1)

# copy()方法
dict1 = {'a': 1}
set1 = set('mkki')
dict0 = dict1.copy()
set0 = set1.copy()

'''
深拷贝拷贝了对象的所有元素，包括多层嵌套的元素————不影响其它
'''
list5 = copy.deepcopy(list1)

# 删除原数据，深浅拷贝仍然在（删除的是变量名）
