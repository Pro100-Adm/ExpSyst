from cgi import parse_qs
html = '<form method="get">Ты знаешь что такое mmorpg?<input name="Answer1"></input><button>Next</button></form>'
def wsgi_app(environ, start_response):
    status = '200 OK'
    d = parse_qs(environ['QUERY_STRING'])
    Answer1 = d.get('Answer1',[None])[0]
    x = []
    x.append(Answer1)
    response_headers = [('Content-type', 'text/html';'charset', 'utf-8')]
    response_body = html
    if Answer1:
        response_body = '<form method="get">Ты играл в The Elder Scrolls 5 Skyrim?<input name="Answer2"></input><button>Next</button></form>'
    start_response(status, response_headers)
    yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
