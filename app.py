from cgi import parse_qs
html = """<form method="get">Ты знаешь что такое mmorpg?<input name="Answer1"></input><br>
<form method="get">Ты играл в The Elder Scrolls 5: Skyrim?<input name="Answer2"></input><br>
<form method="get">Ты играл в Warcraft 3?<input name="Answer3"></input><br>
<form method="get">Готов ли ты к ежемесячным платежам за игру?<input name="Answer4"></input><br>
<form method="get">Готов ли ты к единовременному платежу за игру?<input name="Answer5"></input><br>
<form method="get">Готов ли ты проводить большую часть времени в игре за скучными занятиями?<input name="Answer6"></input><br>
<form method="get">Нравится ли тебе "корейская стилистика?<input name="Answer7"></input><br>
<form method="get">Готов ли ты в любой момент потерять всё и начать сначала?<input name="Answer8"></input><br><button>OK</button></form>"""
def wsgi_app(environ, start_response):
    x = []
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
    response_body = html
    if Answer1 and Answer2 and Answer3 and Answer4 and Answer5 and Answer6 and Answer7 and Answer8:
        ver_var_Teso = {0:0.1, 1:1, 2:1, 5:1, 7:0}
        ver_var_WoW = {0:0.1, 1:1, 3:1, 4:1, 7:0}
        ver_var_Rev = {0:0.5, 1:1, 7:0.8}
        ver_var_BnS = {0:0.3, 1:1, 7:0.7}
        ver_var_EVE = {0:0.1, 1:1, 8:0.6, 7:0}
        ver_var_Lin = {0:0.1, 1:1, 6:1, 7:0.6}
        ver_var_Sky = {0:0.1, 1:1, 6:1, 7:0.5}
        ver_var_All = {0:0.1, 1:1, 6:1, 7:0.4}
        ver_var_Star = {0:0.1, 1:1, 7:0}
        ver_var_Tera = {0:0.1, 1:1, 6:1, 7:0.3}
        for i in range(0,len(x)-1):
            for j in range(0,len(ver_var_Teso)-1):
                if i==list(ver_var_Teso.keys())[j]:
                    Teso = x[i]*list(ver_var_Teso.values())[j]
            for k in range(0,len(ver_var_WoW)-1):
                if i==list(ver_var_WoW.keys())[k]:
                    WoW = x[i]*list(ver_var_WoW.values())[k]
            for l in range(0,len(ver_var_Rev)-1):
                if i==list(ver_var_Rev.keys())[l]:
                    Rev = x[i]*list(ver_var_Rev.values())[l]
            for m in range(0,len(ver_var_BnS)-1):
                if i==list(ver_var_BnS.keys())[m]:
                    BnS = x[i]*list(ver_var_BnS.values())[m]
            for n in range(0,len(ver_var_EVE)-1):
                if i==list(ver_var_EVE.keys())[n]:
                    EVE = x[i]*list(ver_var_EVE.values())[n]
            for o in range(0,len(ver_var_Lin)-1):
                if i==list(ver_var_Lin.keys())[o]:
                    Lin = x[i]*list(ver_var_Lin.values())[o]
            for p in range(0,len(ver_var_Sky)-1):
                if i==list(ver_var_Sky.keys())[p]:
                    Sky = x[i]*list(ver_var_Sky.values())[p]
            for q in range(0,len(ver_var_All)-1):
                if i==list(ver_var_All.keys())[q]:
                    All = x[i]*list(ver_var_All.values())[q]
            for r in range(0,len(ver_var_Star)-1):
                if i==list(ver_var_Star.keys())[r]:
                    Star = x[i]*list(ver_var_Star.values())[r]
            for s in range(0,len(ver_var_Tera)-1):
                if i==list(ver_var_Tera.keys())[s]:
                    Tera = x[i]*list(ver_var_Tera.values())[s]
        response_body = html  
    start_response(status, response_headers)
    yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
