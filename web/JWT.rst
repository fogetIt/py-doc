J(SON )W(EB )T(oken)
====================

:头信息: header

    - 指定 JWT 使用的签名算法
    - e.g.
        .. code-block:: json

            {
                "typ": "JWT",
                "alg": "HS256"
            }
:消息体: payload/claims

    - 存储一些其他业务逻辑所必要的 ``非敏感`` 信息
    - 建议声明的字段
        :iss: 签发者
        :aud: 接收方
        :sub: 面向的用户
        :iat: 签发时间
        :exp: 过期时间（必须大于签发时间）
        :nbf: 在什么时间之前不可用的
        :jti: 唯一身份标识

            -主要用来作为一次性 token ，从而回避重放攻击
:签名: signature

    :未签名的令牌: ``base64url_encode(header).base64url_encode(payload)``

    - HS256(secret_key, 未签名的令牌)
    - 服务端用来鉴定 ``未签名的令牌`` 是否被篡改
- ``base64url_encode(header).base64url_encode(payload).base64url_encode(signature)``
**使用**
::
    JWT 常常被用作保护服务端的资源
    客户端通常将 JWT 通过 HTTP Authorization header 发送给服务端
    服务端使用自己保存的 key 计算、验证签名以判断该 JWT 是否可信

:无状态 JWT: JWT 中存储所有认证授权信息，服务端不存储任何相关数据
:有状态 JWT: JWT 中存储认证授权信息的 ID ，具体数据存储在服务端

**JWT 适合一次性的命令认证**
    颁发一个有效期极短的 JWT ，即使暴露了危险也很小
    由于每次操作都会生成新的 JWT ，因此也没必要保存 JWT ，真正实现无状态
    过期时间可以设到凌晨少人访问时失效，以免用户使用过程中失效而丢失数据
    尽量 https
:缺点:
    - 登录状态信息续签问题
    - 用户主动注销


CSRF
-----

:跨站点请求伪造: 用户同时登陆多个网站，攻击站点恶意使用用户凭据去执行某些动作

        :跨站攻击: 攻击站点利用用户浏览器中的认证信息在其它网站上完成某些操作
        :登录 CSRF: 攻击站点利用用户浏览器中用的认证信息登录到其它站点
