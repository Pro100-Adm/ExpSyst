from cgi import parse_qs
html = """<form method="get">Ты знаешь что такое mmorpg?<input name="Answer1"></input><br>
<form method="get">Ты играл в The Elder Scrolls 5: Skyrim?<input name="Answer2"></input><br>
<form method="get">Ты играл в Warcraft 3?<input name="Answer3"></input><br>
<form method="get">Готов ли ты к ежемесячным платежам за игру?<input name="Answer4"></input><br>
<form method="get">Готов ли ты к единовременному платежу за игру?<input name="Answer5"></input><br>
<form method="get"><input name="Answer6">Готов ли ты проводить большую часть времени в игре за скучными занятиями?</input><br>
<form method="get"><input name="Answer7">Нравится ли тебе "корейская стилистика?</input><br>
<form method="get"><input name="Answer8">Готов ли ты в любой момент потерять всё и начать сначала?</input><br><button>OK</button></form>"""
def wsgi_app(environ, start_response):
    x = ['','','','','','','','']
    status = '200 OK'
    d = parse_qs(environ['QUERY_STRING'])
    Answer1 = d.get('Answer1',[None])[0]
    Answer2 = d.get('Answer2',[None])[0]
    Answer3 = d.get('Answer3',[None])[0]
    Answer4 = d.get('Answer4',[None])[0]
    Answer5 = d.get('Answer5',[None])[0]
    Answer6 = d.get('Answer6',[None])[0]
    Answer7 = d.get('Answer7',[None])[0]
    Answer8 = d.get('Answer8',[None])[0]
    x.append(Answer1)
    x.append(Answer2)
    x.append(Answer3)
    x.append(Answer4)
    x.append(Answer5)
    x.append(Answer6)
    x.append(Answer7)
    x.append(Answer8)
    response_headers = [('Content-type', 'text/html; charset=UTF-8')]
    response_body = html+str(x)
    start_response(status, response_headers)
    yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
