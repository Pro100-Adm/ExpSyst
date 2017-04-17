html = """<form method="get">Ты знаешь что такое mmorpg?
<p><input name="-5" type="radio" value="-5">-5<input name="-4" type="radio" value="-4">-4<input name="-3" type="radio" value="-3">-3<input name="-2" type="radio" value="-2">-2<input name="-1" type="radio" value="-1">-1<input name="0" type="radio" value="0">0<input name="1" type="radio" value="1">1<input name="2" type="radio" value="2">2<input name="3" type="radio" value="3">3<input name="4" type="radio" value="4">4<input name="5" type="radio" value="5">5</p></form>"""
def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    response_body = html
    start_response(status, response_headers)
    yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
