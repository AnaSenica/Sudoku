import random

stevilke = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
        mesto = (stevilo1, stevilo2)
        return mesto
    

    def izbrisana_mesta(self):
        slovar = {}
        stevilo = self.tezavnost
        polna_plosca = self.polna_plosca
        while len(slovar) < stevilo:
            mesto = self.nakljucna_mesta()
            vrsta = mesto[0]
            stolpec = mesto[1]
            if mesto not in slovar:
                slovar[mesto] = polna_plosca[vrsta][stolpec]
            else:
                pass
        return slovar 


    def naredi_slovar_iz_mreze(self, mreza):
        slovar = {}
        for i in range(9):
            for j in range(9):
                slovar[(i, j)] = mreza[i][j]
        return slovar 


    def pripravi_sudoku(self):
        prazni_prostori = self.izbrisana_mesta()
        mreza = self.naredi_slovar_iz_mreze(self.polna_plosca)
        nova_mreza = {}
        for mesto in mreza:
            if mesto in prazni_prostori:
                nova_mreza[mesto] = '_'
            else:
                nova_mreza[mesto] = mreza[mesto]
        return nova_mreza

def narisi(mreza, sudoku):
    for vrsta in mreza:
        print('')
        for stevilka in vrsta:
            print(stevilka, end ='')
            print(' ', end ='')
    print('\n\n#######RESITEV########')
    for vrsta in sudoku:
        print('')
        for stevilka in vrsta:
            print(stevilka, end ='')
            print(' ', end ='')
        
        




jst = Plosca()
#print(jst.seznam_uporabnih_stevil)
#print(jst.indeks)
#print(jst.seznam_uporabnih_stevil[jst.indeks])
#print(jst.sudoku(jst.indeks))
jaz2 = PripravljenaMreza(5)
print(jaz2.polna_plosca)
print('')
print(jaz2.izbrisana_mesta())
print('')

mreza = jaz2.polna_plosca
sudoku = jaz2.pripravi_sudoku()
print(mreza)
print(sudoku)
#narisi(mreza, sudoku)
