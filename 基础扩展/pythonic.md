##### 三目运算
- java/javascript: (expression)? (true value): (false value)
- e.g.
    ```python
    print filter(lambda i: True if i % 2 else False, range(10))
    ```

##### 链式比较
- e.g.
    ```python
    print 1 <= 3 < 10
    ```

##### 字符串反转
- e.g.
    ```python
    print 'mklouy'[::-1]
    ```

##### 字符串列表连接
- `string.join()`常用于连接列表里的字符串，十分高效，且不会犯错
- e.g.
    ```python
    print ' '.join(["Python", "is", "good"])
    ```
