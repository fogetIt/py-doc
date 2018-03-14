除法
----
    :整数除法: 向下取整，舍去小数部分

        .. code-block:: python

            print(10 / 3, 3 / 6, 3 / -6)
    :浮点数除法: 返回浮点数

         .. code-block:: python

            print(10.0 / 3, 3.0 / 6, 3.0 / -6)
    :地板除: 向下取整，浮点数小数部分变为 0

        .. code-block:: python

            print(10 // 3, 10.0 // 3, 3.0 // 6, -3.0 // 6)
    :精确除法: 返回真实的商（总是浮点型）

        .. code-block:: python

            # 这一句必须放在文件首部
            from __future__ import division
            print(10 / 3)


divmod(x, y) -> (x//y, x%y)
----------------------------
