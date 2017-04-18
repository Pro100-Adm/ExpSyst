from cgi import parse_qs
from exp_syst_calc import *
html = """<form method="get">Ты знаешь что такое mmorpg?<input name="Answer1"></input><br>
<form method="get">Ты играл в The Elder Scrolls 5: Skyrim?<input name="Answer2"></input><br>
<form method="get">Ты играл в Warcraft 3?<input name="Answer3"></input><br>
<form method="get">Готов ли ты к ежемесячным платежам за игру?<input name="Answer4"></input><br>
<form method="get">Готов ли ты к единовременному платежу за игру?<input name="Answer5"></input><br>
<form method="get">Готов ли ты проводить большую часть времени в игре за скучными занятиями?<input name="Answer6"></input><br>
<form method="get">Нравится ли тебе "корейская стилистика?<input name="Answer7"></input><br>
<form method="get">Готов ли ты в любой момент потерять всё и начать сначала?<input name="Answer8"></input><br><button>OK</button></form>
Введите значения в интервале от 0 до 1 в формате '0.1'."""
def wsgi_app(environ, start_response): 
    response_headers = [('Content-type', 'text/html; charset=UTF-8')]
    response_body = html
    start_response(status, response_headers)
    yield response_body.encode()
    
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
