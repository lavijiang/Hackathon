# uwsgi --http :9000 --wsgi-file test_uwsgi.py
# curl http://localhost:9000

def application(env,start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello Django"]
