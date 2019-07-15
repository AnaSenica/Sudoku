import model

stevila = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def pozeni_vmesnik():
    #zahtevaj izbiro težavnosti:
    stevilo = tezavnost()
    if stevilo == False:
        print('Napaka. Vpišite 1, 2 ali 3, da izberete težavnost.')
        return pozeni_vmesnik()
    else:
        print('='*52 + '\n\n')
        igra = model.nova_igra(stevilo)
        while True:
            #izpišem igro:
            izpis_igre(igra)
            #rešujem:
            vrsta = izberi_vrsto()
            stolpec = izberi_stolpec()
            stevilka = izberi_stevilko()
            ugib = igra.ugibaj(stevilka, vrsta, stolpec)
            if ugib == 'Zmaga.':
                print('='*52)
                print('\nČestitam, uspešno ste rešili sudoku!\n')
                izpisi_zmago()
                break
            elif ugib == 'Napacno.':
                print('='*52)
                print('\nNAPAČNO, ugibajte še enkrat:\n')
                pass
            elif ugib == 'Napaka 2.':
                print('='*52)
                print('\nPOZOR: Vnaprej napisanih številk ne morete spreminjati.\nPoskusite z drugim poljem:\n')
                pass
            elif ugib == 'Pravilno.':
                print('='*52)
                print('\nPRAVILNO. Ugibajte naprej:\n')
        return None


def izberi_stevilko():
    stevilka = input('\nIzberite stevilko: 1-9 (Vtipkajte število od 1 do 9 in pritisnite ENTER): ')
    if stevilka not in stevila:
        print('\nVtipkajte število od 1 do 9.')
        return izberi_stevilko()
    else:
        return int(stevilka)


def izberi_vrsto():
    vrsta = input('\nIzberite vrsto 1-9 (Vtipkajte število od 1 do 9 in pritisnite ENTER): ')
    indeks = None
    if vrsta not in stevila:
        print('\nVtipkajte število od 1 do 9.')
        return izberi_vrsto()
    else:
        indeks = int(vrsta) - 1
        return indeks

def izberi_stolpec():
    stolpec = input('\nIzberite vrsto 1-9 (Vtipkajte število od 1 do 9 in pritisnite ENTER): ')
    indeks = None
    if stolpec not in stevila:
        print('\nPOZOR: Vtipkati morate število od 1 do 9.')
        return izberi_stolpec()
    else:
        indeks = int(stolpec) - 1
        return indeks


def izpis_igre(igra):
    sudoku = igra.sudoku
    print('VRSTE\STOLPCI:', end = '')
    print('   1   2   3   4   5   6   7   8   9')
    print('-'*52)
    stevilka_vrste = 1
    for vrsta in sudoku:
        print(' '*9, end = '')
        print(stevilka_vrste, end = '')
        stevilka_vrste += 1
        print('     | ', end = '')
        for stevilka in vrsta:
            print(stevilka, end =' | ')
        print('')
        
        


def izberi_tezavnost():
    return input('Izberite težavnost:\n(1)lahko\n(2)srednje težko\n(3)težko:\n')

def tezavnost():
    tezavnost = izberi_tezavnost()
    if tezavnost == '1':
        return 15
    elif tezavnost == '2':
        return 30
    elif tezavnost == '3':
        return 50
    else:
        return False


def izpisi_zmago():
    odgovor = se_enkrat()
    if odgovor == False:
        print('Napaka. Vpišite 1 ali 2, da izberete svoje naslednje dejanje.')
        return izpisi_zmago()



def igraj_se_enkrat():
    return input('\nŽelite igrati še enkrat?\n1) Da.\n2) Ne.\n')
    
def se_enkrat():
    igra = igraj_se_enkrat()
    if igra == '1':
        return pozeni_vmesnik()
    elif igra == '2':
        print('\nHvala, da ste igrali igro. Lep dan še naprej!')
    else:
        return False



pozeni_vmesnik()