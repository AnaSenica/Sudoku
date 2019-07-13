import model

lojtrice = '##########################################\n'

def pozeni_vmesnik():
    #zahtevaj izbiro težavnosti:
    stevilo = tezavnost()
    if tezavnost == False:
        return 'Napaka. Vpišite: "lahko", "srednje težko" ali "težko"'
    else:
        igra = model.nova_igra(stevilo)


def izberi_tezavnost():
    return input('Izberite težavnost: lahko, srednje težko, težko:')

def tezavnost():
    tezavnost = izberi_tezavnost()
    if tezavnost == 'lahko':
        return 15
    elif tezavnost == 'srednje tezko':
        return 30
    elif tezavnost == 'tezko':
        return 50
    else:
        return False


pozeni_vmesnik()