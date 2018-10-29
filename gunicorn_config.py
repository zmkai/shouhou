import psycogreen.gevent


psycogreen.gevent.patch_psycopg()


bind = "0.0.0.0:18100"
backlog = 256
workers = 4
worker_class = "gevent"
worker_connections = 100
max_requests = 300
keepalive = 300
timeout = 30
graceful_timeout = 30