##### knowledge
- “一次性消耗”对象
    ```python
    """
    redis_client.lpush(), queue.get(), file.read()
    获取的都是“一次性消耗”对象(每次获取的都是新的迭代数据)
    """
    """
    在需要多次使用“一次性消耗”对象的情况下，需要先将其赋值给变量，保存起来
    """
    seq_item = queue.get()
    if seq_item:
        func(seq_item)
    """
    “一次性消耗”对象，用于 while 循环，不能同时用在“条件表达式”/“循环体”中
    """
    while redis_client.lpush():
        func(redis_client.lpush()) # Error
    ```

