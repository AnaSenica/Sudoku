import bottle
import model

SKRIVNOST = 'igrica'
bottle.TEMPLATE_PATH.insert(0, "c:\\Users\\Alojz\\Documents\\Ana\\Študij\\1. letnik\\UVP\\PROJEKTNA NALOGA\\Sudoku\\Sudoku\\views")
DATOTEKA_S_STANJEM = "c:\\Users\\Alojz\\Documents\\Ana\\Študij\\1. letnik\\UVP\\PROJEKTNA NALOGA\\Sudoku\\Sudoku\\stanje.json"

sudoku = model.Sudoku(DATOTEKA_S_STANJEM)


@bottle.get('/')
def index():
    return bottle.template('naslovna_stran.tpl')

@bottle.get('/tezavnost/')
def izberi_tezavnost():
    return bottle.template('tezavnost.tpl')

@bottle.get('/pravila/')
def pravila():
    return bottle.template('pravila.tpl')

@bottle.post('/tezavnost1/')
def nova_igra1():
    tezavnost = 15
    id_igre = sudoku.nova_igra(tezavnost)
    bottle.response.set_cookie('id_igre', id_igre, secret = SKRIVNOST, path = '/')
    bottle.redirect('/igra/')

@bottle.post('/tezavnost2/')
def nova_igra2():
    tezavnost = 30
    id_igre = sudoku.nova_igra(tezavnost)
    bottle.response.set_cookie('id_igre', id_igre, secret = SKRIVNOST, path = '/')
    bottle.redirect('/igra/')

@bottle.post('/tezavnost3/')
def nova_igra3():
    tezavnost = 45
    id_igre = sudoku.nova_igra(tezavnost)
    bottle.response.set_cookie('id_igre', id_igre, secret = SKRIVNOST, path = '/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    return bottle.template('mreza.tpl', igra = sudoku.igre[id_igre][0], id_igre = id_igre, poskus = sudoku.igre[id_igre][1])

@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    stevilo_za_ugib = int(bottle.request.forms.getunicode("stevilo"))
    sudoku.ugibaj(id_igre, stevilo_za_ugib, int(vrsta), stolpec)
    bottle.redirect('/igra/')



bottle.run(reloader=True, debug=True)