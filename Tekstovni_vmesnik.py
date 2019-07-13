import model

stevila = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def pozeni_vmesnik():
    #zahtevaj izbiro težavnosti:
    stevilo = tezavnost()
    if stevilo == False:
        print('Napaka. Vpišite: 1, 2 ali 3')
        return pozeni_vmesnik()
    else:
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
                izpisi_zmago()
                break
            elif ugib == 'Napacno.':
                print('Napačno, ugibajte še enkrat.')
                pass
            elif ugib == 'Napaka 2.':
                print('Že obstoječe mreže ne morete spreminjati.')
                pass
        return None



def izberi_stevilko():
    stevilka = input('\nIzberite stevilko: 1-9: ')
    if stevilka not in stevila:
        print('\nVtipkajte število od 1 do 9.')
        return izberi_stevilko()
    else:
        return int(stevilka)


def izberi_vrsto():
    vrsta = input('\nIzberite vrsto 1-9: ')
    indeks = None
    if vrsta not in stevila:
        print('\nVtipkajte število od 1 do 9.')
        return izberi_vrsto()
    else:
        indeks = int(vrsta) - 1
        return indeks

def izberi_stolpec():
    stolpec = input('\nIzberite vrsto 1-9: ')
    indeks = None
    if stolpec not in stevila:
        print('\nVtipkajte število od 1 do 9.')
        return izberi_stolpec()
    else:
        indeks = int(stolpec) - 1
        return indeks


def izpis_igre(igra):
    sudoku = igra.sudoku
    for vrsta in sudoku:
        print('')
        for stevilka in vrsta:
            print(stevilka, end ='')
            print(' ', end ='')


def izberi_tezavnost():
    return input('Izberite težavnost: (1)lahko, (2)srednje težko, (3)težko: ')

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
    print('Čestitam, uspešno ste rešili sudoku!')



pozeni_vmesnik()