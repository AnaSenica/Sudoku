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
        

    def v_redu_plosca(self):
        plosca = None
        while plosca is None:
            plosca = self.poskusna_plosca()
        return plosca

#tole je treba še enkrat:
    def poskusna_plosca(self):
        for i in range(9):
            for j in range(9):
                stevilo = random.choice(stevilke)
                if self.preglej_vrstico(stevilo, i) == True and self.preglej_stolpec(stevilo, j) == True and self.preglej_kvadrat(stevilo, i, j) == True:
                    self.tabela[i][j] = stevilo
                else:
                    self.tabela[i][j] = None
        return self.tabela



#    def prva_vrstica(self):
#        tabela = self.oblika_tabele()
#        vrstica = tabela[0]
#        for j in range(8):
#            stevilka = None
#            while stevilka in vrstica:
#                stevilka = random.choice(stevilke) 
#            vrstica[j] = stevilka
#        for i in stevilke:
#            if i not in vrstica:
#                vrstica[8] = i
#            else:
#                pass
#        return vrstica

#    def druga_vrstica(self):
#        tabela = self.oblika_tabele()
#        tabela[0] = self.prva_vrstica()
#        for k in range(9):
#            if k == 0:
#                pass
#            else:
#                for j in range(8):
#                    pass
#        return tabela

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
        




jst = Plosca()
jst.tabela[4][6] = 3
jst.tabela[5][8] = 5
print(jst.tabela)
print(jst.preglej_vrstico(3, 4))
print(jst.preglej_vrstico(None, 4))
print(jst.preglej_stolpec(None, 4))
print(jst.preglej_stolpec(0, 4))
print(jst.preglej_kvadrat(3, 4, 8))
print(jst.preglej_kvadrat(5, 5, 8))
print(jst.preglej_kvadrat(3, 4, 2))
print(jst.poskusna_plosca())
#print(jst.v_redu_plosca())
    
            


