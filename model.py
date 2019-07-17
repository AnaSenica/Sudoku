import random
import json

stevilke = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zacetek = 'Z'

class Plosca:
        
    def __init__(self): 
        tabela = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            tabela.append(vrstica)
        
        self.tabela = tabela
        self.preveri_ce_je_rekurzija_predolga = []

        slovar = {}
        for i in range(9):
            for j in range(9):
                indeks = (i, j)
                slovar[indeks] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        self.seznam_uporabnih_stevil = slovar
        self.indeks = (0,0)

        
    def preglej_vrstico(self, stevilo, vrstica):
        if stevilo in self.tabela[vrstica]:
            return False
        else:
            return True
    

    def preglej_stolpec(self, stevilo, stolpec):
        stevila_v_stolpcu = []
        for i in range(9):
            stevila_v_stolpcu.append(self.tabela[i][stolpec])
        if stevilo in stevila_v_stolpcu:
            return False
        else:
            return True
    

    def v_katerem_kvadratu(self, indeks):
        '''Podamo indeks vrstice ali stolpca stevila, ki nas zanima. 
        Funkcija vrne seznam vrst ali stolpcev, ki nastopijo v kvadratu,
        v katerem se to stevilo nahaja.'''
        vrsta_ali_stolpec_v_kvadratu = []
        indeks_vs = indeks // 3
        for i in range(9):
            if i // 3 == indeks_vs:
                vrsta_ali_stolpec_v_kvadratu.append(i)
            else:
                pass
        return vrsta_ali_stolpec_v_kvadratu
        

    def preglej_kvadrat(self, stevilo, vrstica, stolpec):
        stevila_v_kvadratu = []
        vrstice_v_kvadratu = self.v_katerem_kvadratu(vrstica)
        stolpci_v_kvadratu = self.v_katerem_kvadratu(stolpec)
        for i in vrstice_v_kvadratu:
            for j in stolpci_v_kvadratu:
                stevila_v_kvadratu.append(self.tabela[i][j])
        if stevilo in stevila_v_kvadratu:
            return False
        else:
            return True
        
    def naslednji_indeks(self):
        sez = list(self.indeks)
        if sez[1] == 8:
            sez[1] = 0
            sez[0] += 1
            return tuple(sez)
        else:
            sez[1] += 1
            return tuple(sez)


    def prejsnji_indeks(self):
        sez = list(self.indeks)
        if sez[1] == 0:
            sez[1] = 8
            sez[0] -= 1
            return tuple(sez)
        else:
            sez[1] -= 1
            return tuple(sez) 


    def sudoku(self, indeks):
        '''Program se ustavi, ko je tabela polna. Za vsak indeks preveri, če lahko da na dano mesto v tabeli neko število.
        Če ja, število postavi tja in gre na naslednji indeks. Če ne, preveri drugo število, sproti že porabljene možnosti
        briše iz seznama možnih števil. Če je ta seznam prazen, pa na danem mestu ni nobenega števila, se vrnem eno mesto
        nazaj, pobrišem tisto število in tja postavim drugo število.
        Problem: rekurzija je včasih predolga, zato sem jo omejilana 950 klicev. Če je rekurzija predolga, funkcija vrne
        'Predolga rekurzija'.'''
    
        self.indeks = indeks
        if len(self.preveri_ce_je_rekurzija_predolga) == 960:
            return 'Predolga rekurzija'
        elif self.tabela[8][8] != None:
            return self.tabela
        elif self.seznam_uporabnih_stevil[self.indeks] == []:
            self.seznam_uporabnih_stevil[self.indeks] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.indeks = self.prejsnji_indeks()
            sez = list(self.indeks)
            vrsta = sez[0]
            stolpec = sez[1]
            stevilo_na_prejsnjem_indeksu = self.tabela[vrsta][stolpec]
            self.seznam_uporabnih_stevil[self.indeks].remove(stevilo_na_prejsnjem_indeksu)
            self.tabela[vrsta][stolpec] = None
            self.preveri_ce_je_rekurzija_predolga.append(0)
            return self.sudoku(self.indeks)
        else:
            sez = list(self.indeks)
            vrsta = sez[0]
            stolpec = sez[1]
            stevilo = random.choice(self.seznam_uporabnih_stevil[self.indeks])
            
            if self.preglej_vrstico(stevilo, vrsta) == True and self.preglej_stolpec(stevilo, stolpec) == True and self.preglej_kvadrat(stevilo, vrsta, stolpec) == True:
                self.tabela[vrsta][stolpec] = stevilo
                indeks = self.naslednji_indeks()
                self.preveri_ce_je_rekurzija_predolga.append(0)
                return self.sudoku(indeks)
            else:
                self.seznam_uporabnih_stevil[self.indeks].remove(stevilo)
                self.preveri_ce_je_rekurzija_predolga.append(0)
                return self.sudoku(self.indeks)



class PripravljenaMreza:

    def __init__(self, tezavnost):
        self.tezavnost = tezavnost
        self.polna_plosca = self.pripravi_polno_plosco()
        self.resitve = self.izbrisana_mesta()
        self.pripravljena_plosca = self.pripravi_sudoku()


    def pripravi_polno_plosco(self):
        plosca = Plosca()
        polna_plosca = plosca.sudoku(plosca.indeks)
        if polna_plosca == 'Predolga rekurzija':
            return self.pripravi_polno_plosco()
        else:
            return polna_plosca


    def nakljucna_mesta(self):
        izbiram_med = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        stevilo1 = random.choice(izbiram_med)
        stevilo2 = random.choice(izbiram_med)
        mesto = [stevilo1, stevilo2]
        return mesto
    

    def izbrisana_mesta(self):
        seznam = []
        stevilo = self.tezavnost
        while len(seznam) < stevilo:
            mesto = self.nakljucna_mesta()
            if mesto not in seznam:
                seznam.append(mesto)
            else:
                pass
        return seznam


    def pripravi_sudoku(self):
        prazni_prostori = self.resitve
        mreza = self.kopija_mreze(self.polna_plosca)
        for prostor in prazni_prostori:
            vrsta = prostor[0]
            stolpec = prostor[1]
            mreza[vrsta][stolpec] = '_'
        return mreza
        

    def kopija_mreze(self, mreza):
        nova_mreza = []
        for vrsta in mreza:
            nova_mreza.append([stevilka for stevilka in vrsta])
        return nova_mreza
            

class Igra:

    def __init__(self, tezavnost, polna = None, sudoku = None, resitve = None):
        self.tezavnost = tezavnost
        if polna == None and sudoku == None and resitve == None:
            self.mreza = PripravljenaMreza(self.tezavnost)
            self.polna = self.mreza.polna_plosca
            self.sudoku = self.mreza.pripravljena_plosca
            self.resitve = self.mreza.resitve
        else:
            self.polna = polna
            self.sudoku = sudoku
            self.resitve = resitve
        

    def ugibaj(self, stevilka, vrsta, stolpec):
        mozne_resitve = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if stevilka not in mozne_resitve:
            return 'Napaka 1.'
        elif [vrsta, stolpec] not in self.resitve:
            return 'Napaka 2.'
        elif self.polna[vrsta][stolpec] == stevilka:
            self.sudoku[vrsta][stolpec] = stevilka
            if self.zmaga():
                return 'Zmaga.'
            else:
                return 'Pravilno.'
        else:
            self.sudoku[vrsta][stolpec] = stevilka
            return 'Napacno.'


    def zmaga(self):
        if self.sudoku == self.polna:
            return True
        else:
            return False


class Sudoku:

    def __init__(self, datoteka_s_stanjem):
        '''V self.igre sta pod id-ji shranjena igra in stanje. '''
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem


    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding = 'utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre) : (Igra(igre[id_igre]['tezavnost'], igre[id_igre]['polna_mreza'], igre[id_igre]['resevana_mreza'], igre[id_igre]['resitve']), igre[id_igre]['stanje']) for id_igre in igre}
        return
    #POPRAVI: pravi, da je preveč oklepajev. Poskusi popraviti, da bodo rešitve zapisane kot nabor, ne kot slovar!!!

    def zapisi_igro_v_datoteko(self):
        '''Iz self.igre zapiše vse elemente v datoteko.'''
        with open(self.datoteka_s_stanjem, 'w', encoding = 'utf-8') as f:
            igre = {}
            for id_igre, (igra, stanje) in self.igre.items():
                igre[id_igre] = {'tezavnost': igra.tezavnost, 'polna_mreza': igra.polna, 'resevana_mreza': igra.sudoku, 'resitve': igra.resitve, 'stanje': stanje}
            json.dump(igre, f)
        return


    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self, tezavnost):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = Igra(tezavnost)
        self.igre[id_igre] = (igra, zacetek)
        self.zapisi_igro_v_datoteko()
        return id_igre

    
    def ugibaj(self, id_igre, stevilka, vrsta, stolpec):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(stevilka, vrsta, stolpec)
        self.igre[id_igre] = (igra, novo_stanje)
        self.zapisi_igro_v_datoteko()
        return





def nova_igra(tezavnost):
    return Igra(tezavnost)


#jaz = Sudoku("c:\\Users\\Alojz\\Documents\\Ana\\Študij\\1. letnik\\UVP\\PROJEKTNA NALOGA\\Sudoku\\Sudoku\\stanje.json")
#jaz.nova_igra(3)
#print(jaz.igre)
#print(jaz.igre[0][0].tezavnost)
#print(jaz.datoteka_s_stanjem)
#jaz.nova_igra(4)
#print(jaz.igre)
#print(jaz.igre[0][0].sudoku)
#jaz.ugibaj(0, 3, 4, 5)












