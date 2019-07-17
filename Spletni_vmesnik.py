import bottle
import model

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
def izberi_tezavnost():
    return bottle.template('pravila.tpl')




bottle.run(reloader=True, debug=True)