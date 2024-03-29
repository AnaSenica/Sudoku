import bottle
import model

SKRIVNOST = 'igrica'
#bottle.TEMPLATE_PATH.insert(0, "c:\\Users\\Alojz\\Documents\\Ana\\Študij\\1. letnik\\UVP\\PROJEKTNA NALOGA\\Sudoku\\Sudoku\\views")
#DATOTEKA_S_STANJEM = "c:\\Users\\Alojz\\Documents\\Ana\\Študij\\1. letnik\\UVP\\PROJEKTNA NALOGA\\Sudoku\\Sudoku\\stanje.json"

#sudoku = model.Sudoku(DATOTEKA_S_STANJEM)
sudoku = model.Sudoku('stanje.json')


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
    tezavnost = 20
    id_igre = sudoku.nova_igra(tezavnost)
    bottle.response.set_cookie('id_igre', id_igre, secret = SKRIVNOST, path = '/')
    bottle.redirect('/igra/')

@bottle.post('/tezavnost2/')
def nova_igra2():
    tezavnost = 40
    id_igre = sudoku.nova_igra(tezavnost)
    bottle.response.set_cookie('id_igre', id_igre, secret = SKRIVNOST, path = '/')
    bottle.redirect('/igra/')

@bottle.post('/tezavnost3/')
def nova_igra3():
    tezavnost = 60
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
    stevilo_za_ugib = (bottle.request.forms.getunicode("stevilo"))
    vrsta_za_ugib = (bottle.request.forms.getunicode("vrsta"))
    stolpec_za_ugib = (bottle.request.forms.getunicode("stolpec"))
    if stevilo_za_ugib in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        sudoku.ugibaj(id_igre, int(stevilo_za_ugib), int(vrsta_za_ugib), int(stolpec_za_ugib))
        if sudoku.igre[id_igre][1] == 'Zmaga.':
            bottle.redirect('/zmaga/')
        else:
            bottle.redirect('/igra/')
    else:
        bottle.redirect('/napaka1/')

        
@bottle.get('/zmaga/')
def zmaga():
    return bottle.template('zmaga.tpl')

@bottle.get('/napaka1/')
def napaka1():
    return bottle.template('napaka1.tpl')



bottle.run(reloader=True, debug=True)