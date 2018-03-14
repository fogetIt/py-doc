##### nginx--->uwsgi--->django/flask
`nginx`处理所有静态请求，然后将所有非静态请求通过`uwsgi`传递给`python`程序来进行处理

##### install
```bash
pip install uwsgi
uwsgi --version
killall -9 uwsgi
```

##### uwsgi.ini
```ini
[uwsgi]
; http = host:port   # connect browser
; stats = host:port  # stats server
socket = host:port   # connect nginx
chdir = ...          # path to project
module = ...         # wsgi file
; wsgi-file = ...
callable = app       # wsgi callable func
virtualenv = ...     # virtualenv dir
master = true        # main process
processes = 2        # processes number
; workers = 2
gevent = 100         # gevent greenlets number
; threads = 100      # threads number
pidfile = ...        # which pid file
vacuum = true        # autoremove unix-socket-file and pid-file if close
daemonize = ...      # backstage run, print log to file or UDP server
py-autoreload = 1    # autoreload if *.py be modified
```

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

