from cgi import parse_qs
from exp_syst_calc import *
from exp_syst_dict import *
html = """Введите значения в интервале от 0 до 1 в формате '0.1'.<br>
<form method="get">Ты знаешь что такое mmorpg?<input name="Answer1"></input><br>
<form method="get">Ты играл в The Elder Scrolls 5: Skyrim?<input name="Answer2"></input><br>
<form method="get">Ты играл в Warcraft 3?<input name="Answer3"></input><br>
<form method="get">Готов ли ты к ежемесячным платежам за игру?<input name="Answer4"></input><br>
<form method="get">Готов ли ты к единовременному платежу за игру?<input name="Answer5"></input><br>
<form method="get">Готов ли ты проводить большую часть времени в игре за скучными занятиями?<input name="Answer6"></input><br>
<form method="get">Нравится ли тебе "корейская стилистика?<input name="Answer7"></input><br>
<form method="get">Готов ли ты в любой момент потерять всё и начать сначала?<input name="Answer8"></input><br>
<form method="get">Введите термин, значение которого вы хотите узнать: <input name="word"></input><br>
<button>OK</button></form>"""
def wsgi_app(environ, start_response): 
    response_headers = [('Content-type', 'text/html; charset=UTF-8')]
    response_body = html
    status = '200 OK'
    start_response(status, response_headers)
    yield response_body.encode()
    x = []
    good=0
    d = parse_qs(environ['QUERY_STRING'])
    Answer1 = d.get('Answer1',[None])[0]
    Answer2 = d.get('Answer2',[None])[0]
    Answer3 = d.get('Answer3',[None])[0]
    Answer4 = d.get('Answer4',[None])[0]
    Answer5 = d.get('Answer5',[None])[0]
    Answer6 = d.get('Answer6',[None])[0]
    Answer7 = d.get('Answer7',[None])[0]
    Answer8 = d.get('Answer8',[None])[0]
    termin = d.get('word',[None])[0]
    x.append(Answer1)
    x.append(Answer2)
    x.append(Answer3)
    x.append(Answer4)
    x.append(Answer5)
    x.append(Answer6)
    x.append(Answer7)
    x.append(Answer8)
    if Answer1 and Answer2 and Answer3 and Answer4 and Answer5 and Answer6 and Answer7 and Answer8:
        try:
            for i in range(0,len(x)-1):
                x[i]=float(x[i])
            y=calc(x)
            if termin:
                response_body="The Elder Scrolls Online: "+str(y[0])+"<br>"+"World of Warcraft: "+str(y[1])+"<br>"+"Revelations: "+str(y[2])+"<br>"+"Blade And Soul: "+str(y[3])+"<br>"+"EVE Online: "+str(y[4])+"<br>"+"Lineage 2: "+str(y[5])+"<br>"+"Skyforge: "+str(y[6])+"<br>"+"Аллоды Онлайн: "+str(y[7])+"<br>"+"'Star Wars: Knights of the Old Republic': "+str(y[8])+"<br>"+"Tera: "+str(y[9])+"<br>"+str(termin)+": "+str(Dictionary.get(str(termin)))+"<br>"
                start_response(status, response_headers)
                yield response_body.encode()
            else:
                response_body="The Elder Scrolls Online: "+str(y[0])+"<br>"+"World of Warcraft: "+str(y[1])+"<br>"+"Revelations: "+str(y[2])+"<br>"+"Blade And Soul: "+str(y[3])+"<br>"+"EVE Online: "+str(y[4])+"<br>"+"Lineage 2: "+str(y[5])+"<br>"+"Skyforge: "+str(y[6])+"<br>"+"Аллоды Онлайн: "+str(y[7])+"<br>"+"'Star Wars: Knights of the Old Republic': "+str(y[8])+"<br>"+"Tera: "+str(y[9])+"<br>"
                start_response(status, response_headers)
                yield response_body.encode()
        except:
            response_body="Пожалуйста, введите корректные значения.<br>"
            start_response(status, response_headers)
            yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
