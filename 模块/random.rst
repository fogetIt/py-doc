random
=======
.. code-block:: python

    import random
    seq = "qwert54321"
    print(random.choice(seq))          #: 随机取出指定序列中的 1 个元素
    print(random.sample(seq, 3))       #: 随机取出指定序列中的 n 个元素（以列表形式返回）
    print(random.random())             #: 随机生成 1 个 0-1 之间的浮点数（有下限，无上限）
    print(random.uniform(1, 20))       #: 随机生成 1 个指定范围内的浮点数（有下限，无上限）
    print(random.randint(1, 20))       #: 随机生成 1 个指定范围内的整数（包括上限）
    print(random.randrange(1, 20, 2))  #: 随机生成 1 个指定 range 范围内的整数（有下限，无上限）
    l = list(seq)
    random.shuffle(l)  #: 随机打乱指定列表的顺序
    print(l)  # ['4', 'w', 'q', '2', 'e', '1', 't', '5', 'r', '3']
