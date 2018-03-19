`nginx`处理所有静态请求，然后将所有非静态请求通过`uwsgi`传递给`python`程序来进行处理

##### install
```bash
pip install uwsgi
uwsgi --version
killall -9 uwsgi
```

##### [uwsgi 配置文件](uwsgi.ini)
##### [nginx 配置文件](uwsgi.conf)

##### Django + uwsgi
```shell
uwsgi \
    --http :8001 \
    --chdir ${django project dir} \
    --wsgi-file ***/wsgi.py \
    --master \
    --processes 4 \
    --threads 2 \
    --stats 127.0.0.1:9191
```