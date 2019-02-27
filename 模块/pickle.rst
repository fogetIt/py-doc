.. code:: python

    import sys
    PY2 = sys.version_info.major == 2
    if len(sys.argv) > 1:
        # cPickle 用法与 pickle 几乎完全相同，基于 c 语言编写，速度是 pickle 的 1000 倍
        if PY2:
            import cPickle as pickle
        else:
            import _pickle as pickle
    else:
        import pickle


    class Cls(object):
        some_bool = True
        some_str  = 'egg'


    # 对象 <-> 字符串
    obj = Cls()
    pickle_string = pickle.dumps(obj)
    print(pickle_string)
    obj = pickle.loads(pickle_string)
    print(obj.some_bool, obj.some_str)

    # 存储到文件
    obj = Cls()
    fn = 'a.pkl'
    with open(fn, 'wb') as f:
        pickle.dump(obj, f)
    with open(fn, 'rb') as f:
        obj = pickle.load(f)
        print(obj.some_bool, obj.some_str)
